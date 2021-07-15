from lxml import html
import requests
import json
import os, sys

HOLOLIVE_DATA_PATH = "../_data/hololive.json"
OUPUT_PATH         = "../_data/holovideo.json"

NUMBER_OF_LATEST_VIDEOS = 3

#Set API_KEY this should be stored in an environment variable called YT_API
API_KEY = os.getenv("YT_API", "None")

if API_KEY == "None":
	sys.exit("API_KEY variable is not set, try running . ./set_api_key.sh")

#Extract relevant data from a playlist request
#Here we select the fields: in snippet object in the items array 
#Select: publishedAt, title, thumbnails (obj), resourceId.videoId
#Video is the snippet object in the youtube api
class Video:
	def __init__(self, publishedAt, title, thumbnail, videoId):
		self.publishedAt = publishedAt
		self.title = title
		self.thumbnail = thumbnail
		self.videoId = videoId

	def toJson(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=4)

	def print(self):
		print("Video Data")
		print("title: " + self.title)
		print("publishedAt: " + self.publishedAt)
		#print("thumbnails: " + self.thumbnails)
		print("videoId: " + self.videoId)
		print("\n")


#Convert a url to an playlistId.
#This is done by just changing the second letter from a C to a U.
def convert_url_to_playlistId(url):
	url_list = list(url)
	url_list[1] = 'U'
	return "".join(url_list)

#Gets the channel urls from an json file
def get_yt_channel_url():
	with open(HOLOLIVE_DATA_PATH) as file:
		holo_data = json.loads(file.read())
		playlistIds = []
		for member in holo_data:
			playlistIds.append(
				convert_url_to_playlistId(
					member["url"].split("/")[-1]
				)
			)
	return playlistIds

#Gets the latest videos, [Youtube Data API] Quota Cost: 1
def get_latest_videos(playlistId, num):
	YOUTUBE_API_PLAYLIST = "https://www.googleapis.com/youtube/v3/playlistItems"
	query = "?part=snippet&playlistId=" + playlistId + "&maxResults=" + str(num) + "&key=" + API_KEY

	res = requests.get(YOUTUBE_API_PLAYLIST + query).json()
	return res

def main():
	all_channels = []

	# Get the channelIds and convert them to playlistIds.
	playlistIds = get_yt_channel_url()
	
	for id in playlistIds:
		# Request the latest videos from the youtube data api.
		items = get_latest_videos(id, NUMBER_OF_LATEST_VIDEOS)["items"]
	
		# Latest videos from one holomember
		channel_videos = []

		# Extract the info we want from "items"
		for item in items:
			snippet = item["snippet"]
			channel_videos.append(Video(snippet["publishedAt"], snippet["title"], snippet["thumbnails"]["medium"], snippet["resourceId"]["videoId"]))

		all_channels.append(channel_videos)

	with open(OUPUT_PATH, "w") as outfile:
		json.dump(all_channels, outfile, indent=4, default=lambda o: o.__dict__, ensure_ascii=False)
	

if __name__ == "__main__":
    main()
from lxml import html
import requests
import json

HOLOLIVE_DATA_PATH = "_data/hololive.json"
API_KEY = ""


#Extract relevant data from a playlist request
#Here we select the fields: in items array select snippet.publishedAt, snippet.title, snippet.thumbnails
class Video:
	pass

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

#Get the 1-5 latest videos
def get_latest_videos(playlistId, num):
	YOUTUBE_API_PLAYLIST = "https://www.googleapis.com/youtube/v3/playlistItems"
	query = "?part=snippet&playlistId=" + playlistId + "&maxResult=" + str(num) + "&key=" + API_KEY
	
	res = requests.get(YOUTUBE_API_PLAYLIST + query)
	
	print()

def main():
	playlistIds = get_yt_channel_url()
	#print(playlistIds)

	get_latest_videos(playlistIds[1], 2)


if __name__ == "__main__":
    main()





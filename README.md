## HoloLinks

**get_yt_data.py** - handles all yt request, save it in an json that acts as the db.
the rest of the site is static and only displays the data from the json db file.

the site will be regenerated when there is a change in the json db file.
this can be done by **entr** or **get_yt_data.py**

TODO:
- See who is live and upcoming videos!
- 3 Latest videos from each member

#### See who is live and upcoming videos!
- Get The data (Search.list)
- Save it in a Object

---

#### 3 Latest videos from each member
get_yt_data.py will make a request for the data

TODO:
- Convert a youtube channel link to "uploaded", change the C to a U.
- Create an object for holding the return data
- Save the object in an json file

Example Url:

	https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=UU1opHUrw8rvnsadT-iGp7Cg&maxResult=3&key=APIKEY

Gets the three latest videos from aqua!

Design / Function:
- Each members picture on the left in a row each.
- to the right of the picture the 3 latest videos.
- the ability to change the order either from a file or in the ui.
## HoloLinks

A static site with links to holomembers channels, also shows the latest videos.

---

TODO:
1. Show who is live, and show the upcoming videos
	- The youtube API does not make this easy...
2. Add a nijisanji page or create a fork for with nijisanji.
3. Activate github pages, and host it on github.
4. Create instructions for how to build and generate a local version.

---

**get_yt_data.py** - currently gets the 3 latest videos.

To regenerate the site when .json is updated we can use **entr** or do it in **get_yt_data.py**.
See if github pages has the ability to run scripts.

#### To Get Upcoming and Live status 
- Get The data (Search.list) (Cost: 100)
- Save it in a Object
import json
import requests
import initial_data
import sqlite3
import sys

# response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + first_artist)
# print(json.dumps(response.json(), indent=2))

artist_id = '1249595'
# collectionId = '168376392'
# artist_id = '120199'
# artist_id = '909253'
response = requests.get("https://itunes.apple.com/lookup?id=" + artist_id + "&entity=song") # &limit=3
# response = requests.get("https://itunes.apple.com/lookup?collectionId=" + collectionId + "&entity=song")
# o = response.json()
# print(json.dumps(response.json(), indent=2))


# for result in o["results"]:
#     print(result["artistId"])

o = response.json()
del o["results"][0]

# print(json.dumps(o, indent=2))


for result in o["results"]:
    artistId = result["artistId"]
    collectionId = result["collectionId"]
    trackId = result["trackId"]
    artistName = result["artistName"]
    collectionName = result["collectionName"]
    trackName = result["trackName"]
    releaseDate = result["releaseDate"]
    # except KeyError:
    #     continue
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS songdata(artistId, collectionId, trackId, "
        "artistName, collectionName, trackName, releaseDate)")
    # con.commit()
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("INSERT INTO songdata VALUES(?, ?, ?, ?, ?, ?, ?)", (artistId, collectionId, trackId, artistName,
                collectionName, trackName, releaseDate))
    # con.commit()
    res = cur.execute("SELECT * FROM songdata")
    # con.commit()
    all_res = res.fetchall()
    print(all_res)
    cur.execute("DROP TABLE IF EXISTS songdata")
    # con.commit()
    con.close()

# to set correctly date
# for result in o["results"]:
#     date = result["releaseDate"]
#     releaseDate = date[:4]
#     print(releaseDate)

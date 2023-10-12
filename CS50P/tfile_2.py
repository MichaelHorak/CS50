import json
import requests
import initial_data
#
# selected_genre = 'Rock'
# selected_artists = artists_by_genre[selected_genre]
# artist_ids = []
# for artist in selected_artists:
#     print(artist)

# for artist in selected_artists:
#     response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
#     o = response.json()
#     result = o["results"]
#     artist_id = result[0]['artistId']
#     # print(artist_id)
#
#     artist_ids.append(artist_id)
#
# print(artist_ids)


# for i in range(0, len(selected_artists)):
#     artist = selected_artists[i]
#     response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + first_artist)
# first_artist = selected_artists[0]
# response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + first_artist)
# print(json.dumps(response.json(), indent=2))

# o = response.json()
#
# for result in o["results"]:
#     print(result["artistId"])

# "artistId": 44984,

# result = o["results"]
# artist_id = result[0]['artistId']
# print(artist_id)
# artist_ids = []
# artist_ids.append(artist_id)

artist_id = '44984'
# artist_id = '120199'
# artist_id = '909253'
response = requests.get("https://itunes.apple.com/lookup?id=" + artist_id + "&entity=album")
# https://itunes.apple.com/search?lookup?id=44984
# https://itunes.apple.com/search?lookup?id=909253
# https://itunes.apple.com/lookup?id=909253
print(json.dumps(response.json(), indent=2))

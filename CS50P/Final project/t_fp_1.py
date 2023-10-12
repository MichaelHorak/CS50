import json
import requests
from initial_data import *
import sqlite3

artist_ids = []


def main():
    # select the genre
    selected_genre = introduction()
    print(f"You selected {selected_genre}.")
    # based on the genre we generate a list of artists' itunes ids to request more data
    generate_artist_ids(selected_genre)
    # use artists' ids to return data from itunes & save in a sqlite db
    generate_data(artist_ids)


# select the genre
def introduction():
    print("Welcome to Michael's Music Quiz!")
    print("Test your knowledge about your favourite genre.")
    print("Please select a genre from the following options:")
    for i, genre in enumerate(genres):
        print(i + 1, genre)

    # Get user's genre choice
    genre_choice = input("Enter the number of your chosen genre: ")
    selected_genre = genres[(int(genre_choice)-1)]
    return selected_genre


# based on the genre we generate a list of artists' itunes ids to request more data
def generate_artist_ids(genre):
    selected_artists = artists_by_genre[genre]
    for artist in selected_artists:
        response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
        o = response.json()
        result = o["results"]
        artist_id = result[0]['artistId']
        artist_ids.append(artist_id)
    return artist_ids


# use artists' ids to return data from itunes & save in a sqlite db
def generate_data(artist_ids):
    for artist in artist_ids:
        str_artist = str(artist)
        response = requests.get("https://itunes.apple.com/lookup?id=" + str_artist + "&entity=song&limit=8")
        # send a request to itunes to return artist's songs
        o = response.json()
        del o["results"][0]
        for result in o["results"]:
            # vars to save in the database
            artist_id = result["artistId"]
            collection_id = result["collectionId"]
            track_id = result["trackId"]
            artist_name = result["artistName"]
            collection_name = result["collectionName"]
            track_name = result["trackName"]
            # releaseDate = result["releaseDate"]
            date = result["releaseDate"]
            release_date = date[:4]

            # open database
            con = sqlite3.connect("music.db")
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS songdata(artist_id, collection_id, track_id, "
                "artist_name, collection_name, track_name, releaseDate)")
            con = sqlite3.connect("music.db")
            cur = con.cursor()
            # insert data into the database
            cur.execute("INSERT INTO songdata VALUES(?, ?, ?, ?, ?, ?, ?)",
                        (artist_id, collection_id, track_id, artist_name,
                         collection_name, track_name, release_date))
            res = cur.execute("SELECT * FROM songdata")
            all_res = res.fetchall()
            print(all_res)
            cur.execute("DROP TABLE IF EXISTS songdata")
            # con.commit()
            con.close()


# don't forget to close the connection and drop all tables once the score is printed


if __name__ == "__main__":
    main()

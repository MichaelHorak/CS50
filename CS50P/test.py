import json
import requests


artist_ids = []


def main():
    selected_genre = introduction()
    print(f"You selected {selected_genre}.")

    # selected_artists = artists_by_genre[selected_genre]
    # print(f"Selected artists of the genre: {selected_artists}")

    generate_artist_ids(selected_genre)
    print(artist_ids)


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

    # 1) Retrieve data from the iTunes API.


def generate_artist_ids(genre):
    selected_artists = artists_by_genre[genre]
    for artist in selected_artists:
        response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
        o = response.json()
        result = o["results"]
        artist_id = result[0]['artistId']
        # artist_id = result[0]['amgArtistId']
        artist_ids.append(artist_id)
    return artist_ids


if __name__ == "__main__":
    main()

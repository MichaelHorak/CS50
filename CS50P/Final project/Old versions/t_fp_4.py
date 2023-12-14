from initial_data import *
import requests
import sqlite3

artist_ids = []


class Quiz:
    def __init__(self):
        self.score = 0

    def __str__(self):
        return f"Your score is {self.score}"

    @staticmethod
    def introduction():
        print("Welcome to Michael's Brilliant Music Quiz!")
        print("Test your knowledge about your favourite genre.")
        print("Please select a genre from the following options:")
        for i, genre in enumerate(genres):
            print(i + 1, genre)

        # Get user's genre choice
        genre_choice = input("Enter the number of your chosen genre and press <enter>: ")
        selected_genre = genres[(int(genre_choice) - 1)]
        return selected_genre

    def generate_data(self, selected_genre):
        selected_artists = artists_by_genre[selected_genre]
        for artist in selected_artists:
            response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
            o = response.json()
            result = o["results"]
            artist_id = result[0]['artistId']
            artist_ids.append(artist_id)

        for artist in artist_ids:
            str_artist = str(artist)
            # response = requests.get("https://itunes.apple.com/lookup?id=" + str_artist + "&entity=song&limit=8")
            response = requests.get("https://itunes.apple.com/lookup?id=" + str_artist + "&entity=song")
            # print(json.dumps(response.json(), indent=2))

            # send a request to itunes to return artist's songs
            o = response.json()
            del o["results"][0]
            for result in o["results"]:
                try:
                    date = result["releaseDate"]
                    # vars to save in the database
                    artist_name = result["artistName"]
                    collection_name = result["collectionName"]
                    track_name = result["trackName"]
                    # releaseDate = result["releaseDate"]
                    # date = result["releaseDate"]
                    release_date = date[:4]
                    unwanted_albums = ['special edition', 'deluxe edition', 'single', 'soundtrack', 'motion picture',
                                       'collection', 'remastered']
                    for album in unwanted_albums:
                        if album in collection_name:
                            continue
                        else:
                            self.insert_into_db(artist_name, collection_name, track_name, release_date)
                except KeyError:
                    # skips result if it does not include releaseDate
                    continue

    @staticmethod
    def insert_into_db(artist_name, collection_name, track_name, release_date):
        # open database
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS song_data(artist_name TEXT, collection_name TEXT, track_name TEXT, "
            "release_date INTEGER)")
        # insert data into the database
        cur.execute("INSERT INTO song_data VALUES(?, ?, ?, ?)",
                    (artist_name, collection_name, track_name, release_date))
        # SELECT ALL
        # res = cur.execute("SELECT * FROM song_data")
        # all_res = res.fetchall()
        # print(all_res)
        con.commit()
        con.close()

    def generate_questions(self):
        ...

    def update_score(self):
        self.score += 1

    @staticmethod
    def delete_db_table():
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS song_data")
        con.commit()
        con.close()


class Question:
    @staticmethod
    def get_line_from_db():
        # get data from database
        # open database
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM song_data ORDER BY RANDOM() LIMIT 1')
        # res = cur.execute("SELECT * FROM song_data ORDER BY RANDOM() LIMIT 1")
        results = cur.fetchall()
        con.commit()
        # print(results)
        con.close()
        # format result data
        for result in results:
            key_data = list(result)
        artist_id, collection_id, track_id, artist_name, collection_name, track_name, release_date = key_data
        return artist_id, collection_id, track_id, artist_name, collection_name, track_name, release_date

    def display_question(self):
        # question & answers?
        ...

    def get_user_input(self):
        ...
        # print question & answers

    # get data for question
    # correct answer
    # generate pool
    # shuffle pool
    # handle input - answer after printing
    # update score if answer is correct


def main():
    quiz = Quiz()
    selected_genre = quiz.introduction()
    print(f"You selected {selected_genre}.")
    print(f"Loading data...\n")
    quiz.generate_data(selected_genre)

    q1 = Question()
    q1_artist_id, q1_collection_id, q1_track_id, q1_artist_name, q1_collection_name, q1_track_name, q1_release_date \
        = q1.get_line_from_db()
    # at the end always drop the table
    quiz.delete_db_table()


if __name__ == "__main__":
    main()

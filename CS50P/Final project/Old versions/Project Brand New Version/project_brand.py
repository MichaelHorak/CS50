from initial_data import *
import requests
import sqlite3
import random


DATABASE_FILE = "./music.db"
artist_ids = []


class Score:
    def __init__(self):
        self.score = 0

    def update_score(self, result):
        self.score += result

    def get_score(self):
        return self.score


class Question:
    def __init__(self):
        self.answer_pool = ""
        self.correct_answer = ""

    @staticmethod
    def get_line_from_db():
        # get data from database
        # open database
        con = connect_database()
        cur = con.cursor()
        cur.execute('SELECT * FROM song_data ORDER BY RANDOM() LIMIT 1')
        results = cur.fetchall()
        con.commit()
        con.close()
        print("Results:", results)  # Add this line to print the results
        # format result data
        return results[0]

    def answers_input(self, score):
        print(self.correct_answer)
        for i in range(len(self.answer_pool)):
            print(f"{i + 1} {self.answer_pool[i]}")
        # user's input
        answer = input("Enter the number of your answer and press <enter>: ")
        # if user's input is correct, add a point
        if self.answer_pool[int(answer) - 1] == self.correct_answer:
            result = 1
            print(f"Answer {self.correct_answer} is correct.")
        else:
            print(f"Wrong, the correct answer is {self.correct_answer}.")
            result = 0
        score.update_score(result)
        print(f"Your score is {score.get_score()}")


class Question1(Question):
    def __init__(self):
        data = Question.get_line_from_db()
        self.artist_name, self.collection_name, self.track_name, self.release_date = data
        # save the correct answer
        self.correct_answer = self.artist_name
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 \
                = super().get_line_from_db()
            # check for duplicate data
            if self.artist_name2 not in self.answer_pool:
                if self.artist_name2 != self.correct_answer:
                    self.answer_pool.append(self.artist_name2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"Who is the artist of the song {self.track_name} on the album {self.collection_name} from " \
               f"{self.release_date}?"


class Question2(Question):
    def __init__(self):
        def __init__(self):
            self.artist_name, self.collection_name, self.track_name, self.release_date = Question.get_line_from_db()
        # save the correct answer
        self.correct_answer = self.collection_name
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 \
                = super().get_line_from_db()
            # check for duplicate data
            if self.collection_name2 not in self.answer_pool:
                if self.collection_name2 != self.correct_answer:
                    self.answer_pool.append(self.collection_name2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"Which album features the song {self.track_name} by {self.artist_name}?"


def main():
    selected_genre, genre_choice = introduction()
    # quiz.generate_data(selected_genre)
    generate_data(selected_genre, genre_choice)
    # initiate score
    score = Score()

    # q1
    q1 = Question1()
    print(q1)
    q1.answers_input(score)

    # q2
    q2 = Question2()
    print(q2)
    q2.answers_input(score)

    # at the end always drop the table
    delete_db_table()


def connect_database():
    con = sqlite3.connect(DATABASE_FILE)
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS song_data(artist_name TEXT, collection_name TEXT, track_name TEXT,
        release_date INTEGER)
    ''')
    con.commit()
    return con


def introduction():
    print("Welcome to Michael's Brilliant Music Quiz!")
    print("Test your knowledge about your favourite genre.")
    print("Please select a genre from the following options:")
    for i, genre in enumerate(genres):
        print(i + 1, genre)

    # Get user's genre choice
    while True:
        try:
            genre_choice = int(input("Enter the number of your chosen genre and press <enter>: "))
            if genre_choice in range(1, len(genres) + 1):
                selected_genre = genres[(int(genre_choice) - 1)]
                print(f"You selected {selected_genre}")
                return selected_genre, genre_choice
        except ValueError:
            print(f"Enter a number between 1 and {len(genres)}")
            pass


def generate_data(selected_genre, genre_choice):
    print("Gathering data...\n")
    selected_artists = artists_by_genre[selected_genre]
    # search itunes with artist names
    for artist in selected_artists:
        response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
        o = response.json()
        result = o["results"]
        artist_id = result[0]['artistId']
        artist_ids.append(artist_id)

    # send a request to itunes to return artist's songs
    for artist in artist_ids:
        str_artist = str(artist)
        response = requests.get("https://itunes.apple.com/lookup?id=" + str_artist + "&entity=song")
        # print(json.dumps(response.json(), indent=2))

        o = response.json()
        del o["results"][0]
        for result in o["results"]:
            try:
                date = result["releaseDate"]
                # vars to save in the database
                artist_name = result["artistName"]
                collection_name = result["collectionName"]
                track_name = result["trackName"]
                release_date = date[:4]
                # Filter out albums we don't want in db
                # Check if any unwanted pattern is in album
                if not has_unwanted_pattern(collection_name) and artist_name in genres[(int(genre_choice) - 1)]:
                    insert_into_db(artist_name, collection_name, track_name, release_date)

            except KeyError:
                # skips result if it does not include date
                continue


def has_unwanted_pattern(album):
    unwanted_patterns = [
        'special edition',
        'deluxe edition',
        'single',
        'soundtrack',
        'motion picture',
        'collection',
        'remastered',
        'remaster',
        'mix',
        'expanded edition'
    ]

    return any(pattern in album.lower() for pattern in unwanted_patterns)


def insert_into_db(artist_name, collection_name, track_name, release_date):
    # open database
    con = connect_database()
    cur = con.cursor()

    # Check if table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", ('song_data',))
    table_exists = cur.fetchone()

    if not table_exists:
        # Create table if it doesn't exist
        cur.execute('''
            CREATE TABLE song_data(artist_name TEXT, collection_name TEXT, track_name TEXT,
            release_date INTEGER)
        ''')

    # insert data into the database
    cur.execute("INSERT INTO song_data VALUES(?, ?, ?, ?)",
                (artist_name, collection_name, track_name, release_date))

    con.commit()
    con.close()



def update_score(score, result):
    score = score + result
    print(f"Score: {score}")
    return score


def delete_db_table():
    con = connect_database()
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS song_data")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()

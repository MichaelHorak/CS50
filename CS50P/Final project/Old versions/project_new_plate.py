from initial_data import *
import requests
import sqlite3
import random
import os

artist_ids = []


class Quiz:
    def __init__(self):
        self.score = 0
        self.result = ""
        self.answer_pool = ""
        self.correct_answer = ""
        self.key_data = ""

    def generate_questions(self):
        intro_phrases = [
            "Time to show off your knowledge!",
            "Let's test your musical expertise:",
            "Here's a brain-teaser for you:",
            "Get ready for some trivia!",
            "Can you crack this one?",
            "It's question time!",
            "Here's your next challenge:",
            "Let's move on to the next question:",
            "Here's a puzzler for you:",
            "Are you up for this challenge?",
            "Let's see if you know this one:",
            "Ready for the next question?",
            "Here's a challenge for you:",
            "Can you guess this?",
            "It's quiz time!",
            "Get ready for a new question:",
            "Let's dive into the next one:",
            "Here comes another question:",
            "Are you prepared for this?"
        ]
        questions = [
            Question1(),
            # Question2(),
            # Question3(),
            # Question4(),
            # Question5(),
            # Question6(),
            # Question7(),
            # Question8(),
            # Question9(),
            # Question10()
        ]
        # random.shuffle(questions)
        for question in questions:
            intro_phrase = random.choice(intro_phrases)
            print(intro_phrase)
            # print(question)
            # self.result = self.answers_input()
            # self.update_score()

    def answers_input(self):
        # print(self.correct_answer)
        for i in range(len(self.answer_pool)):
            print(f"{i + 1} {self.answer_pool[i]}")
        # user's input
        answer = input("Enter the number of your answer and press <enter>: ")
        # if user's input is correct, add a point
        if self.answer_pool[int(answer) - 1] == self.correct_answer:
            self.result = 1
            print(f"Answer {self.correct_answer} is correct.")
        else:
            print(f"Wrong, the correct answer is {self.correct_answer}.")
            self.result = 0
        return self.result

    def update_score(self):
        self.score += self.result
        print(f"Score: {self.score}\n")

    def get_line_from_db(self):
        try:
            print(f"Connecting to database at: {os.path.join(os.getcwd(), '/music.db')}")
            # con = sqlite3.connect(os.path.join(os.getcwd(), "../music.db"), timeout=10)
            # con = sqlite3.connect("/music.db")
            con = sqlite3.connect("music.db")
            cur = con.cursor()
            cur.execute('''
            SELECT * 
            FROM songdata 
            ORDER BY RANDOM() 
            LIMIT 1
            ''')
            results = cur.fetchall()
            con.commit()
            con.close()
            if results:
                for result in results:
                    self.key_data = list(result)
                artist_name, collection_name, track_name, release_date = self.key_data
                return artist_name, collection_name, track_name, release_date
            else:
                print("No data found in the database.")
                return None
        except Exception as e:
            print(f"Error occurred while fetching data from the database: {e}")
            return None

    def answers_input(self):
        # print(self.correct_answer)
        for i in range(len(self.answer_pool)):
            print(f"{i + 1} {self.answer_pool[i]}")
        # user's input
        answer = input("Enter the number of your answer and press <enter>: ")
        # if user's input is correct, add a point
        if self.answer_pool[int(answer) - 1] == self.correct_answer:
            self.result = 1
            print(f"Answer {self.correct_answer} is correct.")
        else:
            print(f"Wrong, the correct answer is {self.correct_answer}.")
            self.result = 0
        return self.result


class Question1(Quiz):
    def __init__(self):
        super().__init__()

        results = super().get_line_from_db()
        print(results)

        # self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        # # save the correct answer
        # self.correct_answer = self.artist_name
        # self.answer_pool = [self.correct_answer]
        # # gather other options
        # while len(self.answer_pool) < 4:
        #     self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
        #     # check for duplicate data
        #     if self.artist_name2 not in self.answer_pool:
        #         if self.artist_name2 != self.correct_answer:
        #             self.answer_pool.append(self.artist_name2)
        # # shuffle answers
        # random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWho is the artist of the song {self.track_name} on the album " \
               f"{self.collection_name} from {self.release_date}?"


class Question2(Quiz):
    ...


def main():
    selected_genre, genre_choice = introduction()
    delete_db_file()  # Delete the file first
    create_db_table()  # Create the table
    generate_data(selected_genre, genre_choice)

    quiz = Quiz()
    quiz.generate_questions()


def introduction():
    print("Welcome to Michael's Brilliant Music Quiz!")
    print("Test your knowledge about your favourite genre.")
    print("Please select a genre from the following options:")
    for i, genre in enumerate(genres):
        print(i + 1, genre)
    # get user selected genre
    while True:
        try:
            genre_choice = int(input("Enter the number of your chosen genre and press <enter>: "))
            if genre_choice in range(1, len(genres) + 1):
                selected_genre = genres[(int(genre_choice) - 1)]
                print(f"You selected {selected_genre}")
                return selected_genre, genre_choice
        except ValueError:
            pass


def generate_data(selected_genre, genre_choice):
    print(f"Gathering data...\n")
    selected_artists = artists_by_genre[selected_genre]
    for artist in selected_artists:
        response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
        o = response.json()
        result = o["results"]
        # print(f"Results for artist {artist}: {result}")
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
                # Check if any unwanted pattern is in collection_name
                if not has_unwanted_pattern(collection_name) and artist_name in genres[(int(genre_choice) - 1)]:
                    insert_into_db(artist_name, collection_name, track_name, release_date)

            except KeyError:
                # skips result if it does not include releaseDate
                continue

        # print(f"Inserted data for artist: {artist_name}, collection: {collection_name}, "
        #       f"track: {track_name}, release date: {release_date}")


def insert_into_db(artist_name, collection_name, track_name, release_date):
    try:
        # print("\nInserting data into the database...")
        # open database
        con = sqlite3.connect("music.db")
        # con = sqlite3.connect(os.path.join(os.getcwd(), "music.db"))
        # con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "../music.db"))
        # print("\nDatabase connected successfully")
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS songdata (
                artist_name TEXT,
                collection_name TEXT,
                track_name TEXT,
                release_date INTEGER
            )
        ''')
        # print("\nTable created successfully")
        # insert data into the database
        cur.execute("INSERT INTO songdata VALUES(?, ?, ?, ?)",
                    (artist_name, collection_name, track_name, release_date))
        # print(f"Inserted data: {artist_name}, {collection_name}, {track_name}, {release_date}")
        # SELECT ALL
        # res = cur.execute("SELECT * FROM song_data")
        # all_res = res.fetchall()
        # print(all_res)
        con.commit()
        con.close()
        # print("\nDatabase connection closed")
    except Exception as e:
        print(f"Error occurred: {e}")


def has_unwanted_pattern(collection_name):
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

    return any(pattern in collection_name.lower() for pattern in unwanted_patterns)


def delete_db_table():
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS songdata")
    con.commit()
    con.close()


def create_db_table():
    try:
        con = sqlite3.connect("music.db")
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS songdata (
                artist_name TEXT,
                collection_name TEXT,
                track_name TEXT,
                release_date INTEGER
            )
        ''')
        con.commit()
        con.close()
        print("Table created successfully")
    except Exception as e:
        print(f"Error occurred: {e}")


def delete_db_file():
    try:
        os.remove("music.db")
        print("Database file deleted successfully.")
    except FileNotFoundError:
        print("Database file not found.")


if __name__ == "__main__":
    main()

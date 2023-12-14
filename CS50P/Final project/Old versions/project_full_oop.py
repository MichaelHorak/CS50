from initial_data import *
import requests
import sqlite3
import random
import re
import os


class Quiz:
    def __init__(self):
        self.score = 0
        self.selected_genre = ""
        self.selected_artists = ""
        self.response = ""
        self.o = ""
        self.result = ""
        self.artist_id = ""
        self.artist_ids = []
        self.str_artist = ""
        self.date = ""
        # vars to save in the database
        self.artist_name = ""
        self.collection_name = ""
        self.track_name = ""
        self.release_date = ""
        # filter out albums we don't want in db
        self.unwanted_albums = ""
        self.key_data = ""
        self.genre_choice = ""

    def introduction(self):
        print(f"Artists by genre: {artists_by_genre}")
        print("Welcome to Michael's Brilliant Music Quiz!")
        print("Test your knowledge about your favourite genre.")
        print("Please select a genre from the following options:")
        for i, genre in enumerate(genres):
            print(i + 1, genre)

        # Get user's genre choice
        self.genre_choice = input("Enter the number of your chosen genre and press <enter>: ")
        self.selected_genre = genres[(int(self.genre_choice) - 1)]
        print(f"You selected {self.selected_genre}")
        print(f"Gathering data...\n")

    def generate_data(self):
        # print(f"Selected genre: {self.selected_genre}")
        # print(f"Selected artists: {self.selected_artists}")
        self.selected_artists = artists_by_genre[self.selected_genre]

        # Add this line to create the table if it doesn't exist
        for artist in self.selected_artists:
            self.response = requests.get("https://itunes.apple.com/search?entity=musicArtist&term=" + artist)
            self.o = self.response.json()
            self.result = self.o["results"]
            # print(f"Results for artist {artist}: {self.result}")
            self.artist_id = self.result[0]['artistId']
            self.artist_ids.append(self.artist_id)
        # print(f"Artist IDs: {self.artist_ids}")
        # print("Artist IDs:", self.artist_ids)

        # send a request to itunes to return artist's songs
        for artist in self.artist_ids:
            self.str_artist = str(artist)
            self.response = requests.get("https://itunes.apple.com/lookup?id=" + self.str_artist + "&entity=song")
            # print(json.dumps(response.json(), indent=2))

            self.o = self.response.json()
            del self.o["results"][0]
            for result in self.o["results"]:
                try:
                    self.date = result["releaseDate"]
                    # vars to save in the database
                    self.artist_name = result["artistName"]
                    self.collection_name = result["collectionName"]
                    self.track_name = result["trackName"]
                    self.release_date = self.date[:4]
                    # Filter out albums we don't want in db
                    # Check if any unwanted pattern is in collection_name
                    if not has_unwanted_pattern(self.collection_name) and self.artist_name in genres[
                        (int(self.genre_choice) - 1)]:
                        self.insert_into_db()

                except KeyError:
                    # skips result if it does not include releaseDate
                    continue

            # print(f"Inserted data for artist: {self.artist_name}, collection: {self.collection_name}, "
            #       f"track: {self.track_name}, release date: {self.release_date}")

    def insert_into_db(self):
        try:
            # print("Inserting data into the database...")
            # open database
            # con = sqlite3.connect("music.db")
            # con = sqlite3.connect(os.path.join(os.getcwd(), "music.db"))
            con = sqlite3.connect("../music.db")

            # print("Database connected successfully")
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS song_data (
                    artist_name TEXT,
                    collection_name TEXT,
                    track_name TEXT,
                    release_date INTEGER
                )
            ''')
            # print("Table created successfully")
            # insert data into the database
            cur.execute("INSERT INTO song_data VALUES(?, ?, ?, ?)",
                        (self.artist_name, self.collection_name, self.track_name, self.release_date))

            # print(f"Inserted data: {self.artist_name}, {self.collection_name}, {self.track_name}, {self.release_date}")

            # SELECT ALL
            # res = cur.execute("SELECT * FROM song_data")
            # all_res = res.fetchall()
            # print(all_res)
            con.commit()
            con.close()
            # print("Database connection closed")
        except Exception as e:
            print(f"Error occurred: {e}")

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
        questions = [Question1(),
                     # Question2(), Question3(), Question4(), Question5(), Question6(), Question7(),
                     # Question8(), Question9(), Question10()
                     ]
        # random.shuffle(questions)
        for question in questions:
            intro_phrase = random.choice(intro_phrases)
            print(intro_phrase)
            print(question)
            self.result = question.answers_input()
            self.update_score()

        # q7 = Question7()
        # print(q7)
        # self.result = q7.answers_input()
        # self.update_score()


    @staticmethod
    def delete_db_table():
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS song_data")
        con.commit()
        con.close()

    def update_score(self):
        self.score += self.result
        print(f"Score: {self.score}\n")


class Question:
    def __init__(self):
        self.answer_pool = ""
        self.correct_answer = ""
        self.key_data = ""
        self.result = 0

    # @staticmethod
    def get_line_from_db(self):
        try:
            # print(f"Connecting to database at: {os.path.join(os.getcwd(), '../music.db')}")
            con = sqlite3.connect("../music.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM song_data ORDER BY RANDOM() LIMIT 1')
            results = cur.fetchall()
            con.commit()
            con.close()
            if results:
                for result in results:
                    self.key_data = list(result)
                artist_name, collection_name, track_name, release_date = self.key_data
                return artist_name, collection_name, track_name, release_date
            else:
                # print("No data found in the database.")
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


class Question1(Question):
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


class Question2(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        # save the correct answer
        self.correct_answer = self.collection_name
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
            # check for duplicate data
            if self.collection_name2 not in self.answer_pool:
                if self.collection_name2 != self.correct_answer:
                    self.answer_pool.append(self.collection_name2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWhich album features the song {self.track_name} by {self.artist_name}?"


class Question3(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        # save the correct answer
        self.correct_answer = self.artist_name
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
            # check for duplicate data
            if self.artist_name2 not in self.answer_pool:
                if self.artist_name2 != self.correct_answer:
                    self.answer_pool.append(self.artist_name2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWho is the artist of the album {self.collection_name} from {self.release_date}?"


class Question4(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        self.correct_answer = self.release_date
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
            # check for duplicate data
            if self.release_date2 not in self.answer_pool:
                if self.release_date2 != self.correct_answer:
                    self.answer_pool.append(self.release_date2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nIn which year was the album {self.collection_name} by {self.artist_name}" \
               f" released?"


class Question5(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        self.correct_answer = self.release_date
        self.answer_pool = [self.correct_answer]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
            # check for duplicate data
            if self.release_date2 not in self.answer_pool:
                if self.release_date2 != self.correct_answer:
                    self.answer_pool.append(self.release_date2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nIn which year was the song {self.track_name} by {self.artist_name} released?"


class Question6(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        self.correct_answer = self.track_name
        self.answer_pool = [self.correct_answer]
        self.artist_pool = [self.artist_name]
        # gather other options
        while len(self.answer_pool) < 4:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
            # check for duplicate data
            if self.artist_name2 not in self.artist_pool:
                if self.track_name2 != self.correct_answer:
                    self.answer_pool.append(self.track_name2)
                    self.artist_pool.append(self.artist_name2)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWhich song is by {self.artist_name}?"


class Question7(Question):
    def __init__(self):
        super().__init__()
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        # get three songs by the same artist
        cur.execute('''SELECT track_name, artist_name FROM song_data WHERE artist_name = (SELECT artist_name FROM 
        song_data GROUP BY artist_name HAVING COUNT(DISTINCT track_name) >= 3 ORDER BY RANDOM() LIMIT 1) ORDER BY RANDOM() 
        LIMIT 3;''')
        results = cur.fetchall()
        self.answer_pool = [result[0] for result in results]
        self.artist_name = results[0][1]
        # get another song that is by a different artist
        cur.execute('''SELECT track_name, artist_name FROM song_data WHERE artist_name != ? ORDER BY RANDOM() LIMIT 1; 
        ''', (self.artist_name,))
        results = cur.fetchone()
        self.correct_answer, x = results
        con.close()
        self.answer_pool.append(self.correct_answer)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWhich song is NOT by {self.artist_name}?"


class Question8(Question):
    def __init__(self):
        super().__init__()
        self.artist_name, self.collection_name, self.track_name, self.release_date = super().get_line_from_db()
        self.artist_name2 = self.artist_name
        while self.artist_name2 == self.artist_name:
            self.artist_name2, self.collection_name2, self.track_name2, self.release_date2 = super().get_line_from_db()
        # correct answer
        if self.release_date < self.release_date2:
            self.correct_answer = self.collection_name
        elif self.release_date > self.release_date2:
            self.correct_answer = self.collection_name2
        else:
            self.correct_answer = "Both were released in the same year."
        # answers
        self.answer_pool = [self.collection_name, self.collection_name2, "Both were released in the same year."]
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWhich was released first: the album {self.collection_name} by " \
               f"{self.artist_name} or the album {self.collection_name2} by {self.artist_name2}?"


class Question9(Question):
    def __init__(self):
        super().__init__()
        # first just get the released_year
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute('SELECT track_name, artist_name, release_date FROM song_data WHERE release_date = (SELECT '
                    'release_date FROM song_data GROUP BY release_date HAVING COUNT(DISTINCT artist_name) >= 3 ORDER BY'
                    ' RANDOM() LIMIT 1) ORDER BY RANDOM() LIMIT 3')
        results = cur.fetchall()
        con.commit()
        con.close()
        self.song_pool = [result[0] for result in results]
        self.correct_answer = results[0][2]
        self.answer_pool = [self.correct_answer]
        # fill up the pool
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(f'SELECT DISTINCT release_date FROM song_data WHERE release_date != {self.correct_answer} ORDER BY RANDOM() LIMIT 3')
        results = cur.fetchall()
        con.commit()
        con.close()
        self.answer_pool.extend([result[0] for result in results])
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nThe songs {self.song_pool[0]}, {self.song_pool[1]}, and {self.song_pool[2]} " \
               f"are from year:"


class Question10(Question):
    def __init__(self):
        super().__init__()
        # establishing the artist with 3 or more albums
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(f"SELECT artist_name, COUNT(DISTINCT collection_name) AS album_count FROM song_data GROUP BY "
                    f"artist_name HAVING album_count >=3 ORDER BY RANDOM() LIMIT 1")
        self.results = cur.fetchall()
        con.commit()
        con.close()
        self.artist_name = self.results[0][0]
        # now save three albums by this artist
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(f"SELECT DISTINCT collection_name FROM song_data WHERE artist_name = '{self.artist_name}' ORDER BY "
                    f"RANDOM() LIMIT 3")
        self.results = cur.fetchall()
        con.commit()
        con.close()
        self.collection_name1 = self.results[0][0]
        self.collection_name2 = self.results[1][0]
        self.collection_name3 = self.results[2][0]
        self.answer_pool = [self.collection_name1, self.collection_name2, self.collection_name3]
        # and one album by another artist
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(f"SELECT DISTINCT collection_name FROM song_data WHERE artist_name != '{self.artist_name}' ORDER BY"
                    f" RANDOM() LIMIT 1")
        self.results = cur.fetchall()
        con.commit()
        con.close()
        self.collection_name4 = self.results[0][0]
        self.correct_answer = self.collection_name4
        self.answer_pool.append(self.correct_answer)
        # shuffle answers
        random.shuffle(self.answer_pool)

    def __str__(self):
        return f"{self.correct_answer}\nWhich of the following albums is NOT part of {self.artist_name}'s discography?"


def main():
    print(os.getcwd())
    quiz = Quiz()
    quiz.introduction()
    # print("Connecting to the database...")
    quiz.generate_data()
    # print("Before generating questions...")
    quiz.generate_questions()

    # always include at the end
    # quiz.delete_db_table()


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


if __name__ == "__main__":
    main()

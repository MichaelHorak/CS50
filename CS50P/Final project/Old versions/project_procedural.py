import json
import requests
from initial_data import *
import sqlite3
import random
from random import shuffle

artist_ids = []
user_score = 0


def main():
    # select the genre
    selected_genre, genre_choice = introduction()
    generate_data(selected_genre, genre_choice)
    generate_questions()
    # first question
    # score = generate_first_question(user_score)
    # print(f"Your score is {score}.\n")

    # closing db & deleting the table with data
    delete_db_table()


# select the genre
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
            print(f"Enter a number between 1 and {len(genres)}")
            pass


# use artists' ids to return data from itunes & save in a sqlite db
def generate_data(selected_genre, genre_choice):
    print("Gathering data...\n")
    selected_artists = artists_by_genre[selected_genre]
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
                artist = result["artistName"]
                album = result["collectionName"]
                song = result["trackName"]
                date = date[:4]
                # Filter out albums we don't want in db
                # Check if any unwanted pattern is in album
                if not has_unwanted_pattern(album) and artist in genres[(int(genre_choice) - 1)]:
                    insert_into_db(artist, album, song, date)

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


def insert_into_db(artist, album, song, date):
    try:
        con = sqlite3.connect("../music.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS songdata(artist TEXT, album TEXT, song TEXT, date INTEGER)")
        # insert data into the database
        cur.execute("INSERT INTO songdata VALUES(?, ?, ?, ?)",
                    (artist, album, song, date))
        con.commit()
        con.close()
    except Exception as e:
        print(f"Error occurred: {e}")


def generate_questions():
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
        question_1(),
    ]

    shuffle(questions)

    score = 0

    for question in questions:
        intro_phrase = random.choice(intro_phrases)
        print(intro_phrase)

        result = question()

        score += result
        print(f"Score: {score}\n")

    print(f"Final Score: {score}")


def question_1():
    results = get_line_from_db()
    print(results)

    # return 1 for correct
    return 1
    # artistId, collectionId, trackId, artistName, collectionName, trackName, releaseDate = select_data_for_question()
    # # save correct answer
    # correct_answer = artistName
    # # gather the other options
    # answer_pool = [correct_answer]
    # while len(answer_pool) < 4:
    #     # open database
    #     con = sqlite3.connect("music.db")
    #     cur = con.cursor()
    #     cur.execute('SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1')
    #     # res = cur.execute("SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1")
    #     results = cur.fetchall()
    #     con.commit()
    #     # print(results)
    #     con.close()
    #     # format result data
    #     for result in results:
    #         key_data = list(result)
    #     artistId2, collectionId2, trackId2, artistName2, collectionName2, trackName2, releaseDate2 = key_data
    #     if artistName2 not in answer_pool:
    #         if artistName2 != correct_answer:
    #             answer_pool.append(artistName2)
    # # shuffle answers
    # random.shuffle(answer_pool)
    # # print correct answer for testing
    # print(correct_answer)
    # # print question
    # print(f"Who is the artist of the song {trackName} on the album {collectionName} from {releaseDate}?")
    # # generate answers
    # user_score = answers_and_outcome(answer_pool, correct_answer, user_score)
    # return user_score


def get_line_from_db():
    # get data from database
    # open database
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1')
    # res = cur.execute("SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1")
    results = cur.fetchall()
    con.commit()
    print(results)
    con.close()
    # format result data
    for result in results:
        key_data = list(result)
        print(key_data)
    artist, album, song, date = key_data
    return artist, album, song, date


def answers_and_outcome(answer_pool, correct_answer, user_score):
    for i in range(len(answer_pool)):
        print(f"{i + 1} {answer_pool[i]}")
    # user's input
    answer = input("Enter the number of your answer and press <enter>: ")
    # if user's input is correct, add a point
    if answer_pool[int(answer) - 1] == correct_answer:
        user_score += 1
        print(f"Answer {correct_answer} is correct.")
    else:
        print(f"Wrong, the correct answer is {correct_answer}.")
    return user_score


# don't forget to close the connection and drop all tables once the score is printed
def delete_db_table():
    con = sqlite3.connect("../music.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS songdata")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()

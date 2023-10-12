import json
import requests
from initial_data import *
import sqlite3
import random


artist_ids = []
user_score = 0


def main():
    # select the genre
    selected_genre = introduction()
    print(f"You selected {selected_genre}.")
    print(f"Loading data...\n")
    # based on the genre we generate a list of artists' itunes ids to request more data
    generate_artist_ids(selected_genre)
    # use artists' ids to return data from itunes & save in a sqlite db
    generate_data(artist_ids)
    # first question
    score = generate_first_question(user_score)
    print(f"Your score is {score}.\n")
    # second question
    score = generate_second_question(score)
    print(f"Your score is {score}.\n")
    # closing db & deleting the table with data
    delete_db_table()


# select the genre
def introduction():
    print("Welcome to Michael's Music Quiz!")
    print("Test your knowledge about your favourite genre.")
    print("Please select a genre from the following options:")
    for i, genre in enumerate(genres):
        print(i + 1, genre)

    # Get user's genre choice
    genre_choice = input("Enter the number of your chosen genre and press <enter>: ")
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
                artist_id = result["artistId"]
                collection_id = result["collectionId"]
                track_id = result["trackId"]
                artist_name = result["artistName"]
                collection_name = result["collectionName"]
                track_name = result["trackName"]
                # releaseDate = result["releaseDate"]
                # date = result["releaseDate"]
                release_date = date[:4]
                insert_into_db(artist_id, collection_id, track_id, artist_name, collection_name, track_name,
                               release_date)
            except KeyError:
                # skips result if it does not include releaseDate
                continue


def insert_into_db(artist_id, collection_id, track_id, artist_name, collection_name, track_name, release_date):
    # open database
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS songdata(artist_id INTEGER, collection_id INTEGER, track_id INTEGER, "
        "artist_name TEXT, collection_name TEXT, track_name TEXT, release_date INTEGER)")
    # insert data into the database
    cur.execute("INSERT INTO songdata VALUES(?, ?, ?, ?, ?, ?, ?)",
                (artist_id, collection_id, track_id, artist_name,
                 collection_name, track_name, release_date))
    # SELECT ALL
    # res = cur.execute("SELECT * FROM songdata")
    # all_res = res.fetchall()
    # print(all_res)
    con.commit()
    con.close()


def generate_first_question(user_score):
    artistId, collectionId, trackId, artistName, collectionName, trackName, releaseDate = select_data_for_question()
    # save correct answer
    correct_answer = artistName
    # gather the other options
    answer_pool = [correct_answer]
    while len(answer_pool) < 4:
        # open database
        con = sqlite3.connect("music.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1')
        # res = cur.execute("SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1")
        results = cur.fetchall()
        con.commit()
        # print(results)
        con.close()
        # format result data
        for result in results:
            key_data = list(result)
        artistId2, collectionId2, trackId2, artistName2, collectionName2, trackName2, releaseDate2 = key_data
        if artistName2 not in answer_pool:
            if artistName2 != correct_answer:
                answer_pool.append(artistName2)
    # shuffle answers
    random.shuffle(answer_pool)
    # print correct answer for testing
    print(correct_answer)
    # print question
    print(f"Who is the artist of the song {trackName} on the album {collectionName} from {releaseDate}?")
    # generate answers
    user_score = answers_and_outcome(answer_pool, correct_answer, user_score)
    '''
    print(f"1. {answer_pool[0]}")
    print(f"2. {answer_pool[1]}")
    print(f"3. {answer_pool[2]}")
    print(f"4. {answer_pool[3]}")
    # Who is the artist of the song '[Song Title]' on the album '[Album Name]
    # user's input
    answer = input("Enter the number of your answer and press <enter>: ")
    # if user's input is correct, add a point
    if answer_pool[int(answer)-1] == correct_answer:
        user_score += 1
        print(f"Answer {correct_answer} is correct.")
    else:
        print(f"Wrong, the correct answer is {correct_answer}")
    '''
    return user_score


def generate_second_question(user_score):
    # get data from database
    artistId, collectionId, trackId, artistName, collectionName, trackName, releaseDate = select_data_for_question()
    # save correct answer
    correct_answer = collectionName
    # select wrong options / albums
    answer_pool = [correct_answer]
    while len(answer_pool) < 4:
        # open database
        con = sqlite3.connect("music.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1')
        # res = cur.execute("SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1")
        results = cur.fetchall()
        con.commit()
        # print(results)
        con.close()
        # format result data
        for result in results:
            key_data = list(result)
        artistId2, collectionId2, trackId2, artistName2, collectionName2, trackName2, releaseDate2 = key_data
        if collectionName2 not in answer_pool:
            if collectionName2 != correct_answer:
                answer_pool.append(collectionName2)
    # shuffle answers
    random.shuffle(answer_pool)
    # print correct answer for testing
    print(correct_answer)
    # print question
    print(f"Which album features the song {trackName} by {artistName}?")
    # generate answers
    user_score = answers_and_outcome(answer_pool, correct_answer, user_score)
    return user_score


def select_data_for_question():
    # get data from database
    # open database
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1')
    # res = cur.execute("SELECT * FROM songdata ORDER BY RANDOM() LIMIT 1")
    results = cur.fetchall()
    con.commit()
    # print(results)
    con.close()
    # format result data
    for result in results:
        key_data = list(result)
    artistId, collectionId, trackId, artistName, collectionName, trackName, releaseDate = key_data
    return artistId, collectionId, trackId, artistName, collectionName, trackName, releaseDate


def answers_and_outcome(answer_pool, correct_answer, user_score):
    print(f"1. {answer_pool[0]}")
    print(f"2. {answer_pool[1]}")
    print(f"3. {answer_pool[2]}")
    print(f"4. {answer_pool[3]}")
    # user's input
    answer = input("Enter the number of your answer and press <enter>: ")
    # if user's input is correct, add a point
    if answer_pool[int(answer)-1] == correct_answer:
        user_score += 1
        print(f"Answer {correct_answer} is correct.")
    else:
        print(f"Wrong, the correct answer is {correct_answer}.")
    return user_score


# don't forget to close the connection and drop all tables once the score is printed
def delete_db_table():
    con = sqlite3.connect("music.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS songdata")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()

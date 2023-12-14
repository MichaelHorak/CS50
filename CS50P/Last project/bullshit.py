import requests
import sqlite3
import random

artist_ids = []

genres = ['Rock', 'Pop', 'Hip-Hop/Rap', 'Country', 'Nu Metal', 'Arabic Pop', 'Jazz']
artists_by_genre = {
    'Rock': [
        'The Beatles', 'Led Zeppelin', 'Queen', 'Rolling Stones', 'Pink Floyd',
        'Nirvana', 'U2', 'Jimi Hendrix', 'David Bowie', 'The Who',
        'AC/DC', 'Radiohead', 'Eagles', 'Aerosmith', 'The Doors'
    ],
    'Pop': [
        'Michael Jackson', 'Madonna', 'Beyoncé', 'Justin Bieber', 'Taylor Swift',
        'Ed Sheeran', 'Rihanna', 'Bruno Mars', 'Katy Perry', 'Adele',
        'Mariah Carey', 'Ariana Grande', 'Elton John', 'Whitney Houston', 'Prince'
    ],
    'Hip-Hop/Rap': [
        'Kendrick Lamar', 'Drake', 'Jay-Z', 'Eminem', 'Kanye West',
        'Lil Wayne', 'Nas', 'Snoop Dogg', 'Tupac Shakur', 'Notorious B.I.G.',
        'J. Cole', 'Travis Scott', 'Chance the Rapper', 'OutKast', 'Run-DMC'
    ],
    'Country': [
        'Johnny Cash', 'Dolly Parton', 'Willie Nelson', 'Taylor Swift', 'Garth Brooks',
        'George Strait', 'Kenny Rogers', 'Shania Twain', 'Carrie Underwood', 'Tim McGraw',
        'Blake Shelton', 'Reba McEntire', 'Alan Jackson', 'Brad Paisley', 'Luke Bryan'
    ],
    'Nu Metal': [
        'Linkin Park', 'Limp Bizkit', 'Korn', 'System of a Down', 'Slipknot',
        'Deftones', 'Papa Roach', 'Disturbed', 'Mudvayne', 'Static-X',
        'P.O.D.', 'Incubus', 'Staind', 'Sevendust', 'Rage Against the Machine'
    ],
    'Arabic Pop': [
        'Amr Diab', 'Nancy Ajram', 'Tamer Hosny', 'Elissa', 'Haifa Wehbe',
        'Fairuz', 'Kazem Al Saher', 'Sherine Abdel-Wahab', 'Assala Nasri', 'Samira Said',
        'Saber Rebai', 'Nawal El Zoghbi', 'Myriam Fares', 'Wael Kfoury', 'Majida El Roumi'
    ],
    'Jazz': [
        'Miles Davis', 'John Coltrane', 'Louis Armstrong', 'Duke Ellington', 'Charlie Parker',
        'Billie Holiday', 'Thelonious Monk', 'Ella Fitzgerald', 'Dave Brubeck', 'Oscar Peterson',
        'Sarah Vaughan', 'Art Blakey', 'Count Basie', 'Dizzy Gillespie', 'Stan Getz'
    ]
}


def main():
    selected_genre, genre_choice = introduction()
    generate_data(selected_genre, genre_choice)
    # generate_questions()
    delete_db_table()


def introduction():
    print("FUCK YOU")
    print("SELECT GENRE")
    for i, genre in enumerate(genres):
        print(i + 1, genre)

    # get user selected genre
    while True:
        try:
            genre_choice = int(input("Piss off and press <enter>: "))
            if genre_choice in range(1, len(genres) + 1):
                selected_genre = genres[(int(genre_choice) - 1)]
                print(f"Fuck {selected_genre}")
                return selected_genre, genre_choice
        except ValueError:
            print(f"Enter a fucking number between 1 and {len(genres)}")
            pass


def generate_data(selected_genre, genre_choice):
    print("Gathering fucking data...\n")
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


def question_generator():
    ...


def question1():
    ...


def delete_db_table():
    con = sqlite3.connect("../music.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS songdata")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()

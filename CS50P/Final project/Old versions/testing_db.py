# import os
#
# # Get the current working directory
# current_directory = os.getcwd()
#
# # List the files in the current directory
# files_in_directory = os.listdir(current_directory)
#
# # Check if 'music.db' is in the list of files
# if 'music.db' in files_in_directory:
#     print("'music.db' found in the current directory.")
# else:
#     print("'music.db' not found in the current directory.")

# V2
# import sqlite3
#
# # Connect to the database
# con = sqlite3.connect("music.db")
# cur = con.cursor()
#
# # Check if the 'song_data' table exists
# cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='song_data';")
# table_exists = cur.fetchone()
#
# # Close the connection
# con.close()
#
# # Print the result
# if table_exists:
#     print("'song_data' table exists in 'music.db'.")
# else:
#     print("'song_data' table does not exist in 'music.db'.")

# V3

import sqlite3

con = sqlite3.connect("../music.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS song_data(artist_name TEXT, collection_name TEXT, track_name TEXT, release_date INTEGER)")
cur.execute("INSERT INTO song_data VALUES (?, ?, ?, ?)", ("Test Artist", "Test Collection", "Test Track", 2023))
con.commit()
cur.execute("SELECT * FROM song_data")
result = cur.fetchall()
print(result)
con.close()

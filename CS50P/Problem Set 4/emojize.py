import emoji
# In a file called emojize.py,
# implement a program that prompts the user for a str in English
user_data = input("Input: ")
# converting any codes (or aliases) therein to their corresponding emoji.
if user_data == ':thumbsup:':
    user_data = ':thumbs_up:'
# and then outputs the emojized version of that str
print(emoji.emojize(user_data))


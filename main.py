# x = input("Enter time: ")
# y = x.split(":")
#
# a = float(y[0])
#
# b = y[1]
# b = float(b)
# b = b/60
#
# c = a + b
# print(c)
# print(type(c))

def main():
    # get time from user
    answer = input('What time is it? ')
    # call the convert function
    time = convert(answer)
    # breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print('breakfast time')
    # lunch between 12:00 and 13:00
    elif time >= 12 and time <= 13:
        print('lunch time')
    # dinner between 18:00 and 19:00
    elif time >= 18 and time <= 19:
        print('dinner time') 
def convert(time):
    # get hour and minute
    hours, minutes = time.split(":")
    # convert time into a float number
    new_minute = float(minutes) / 60
    # return the result to main function
    return float(hours) + new_minute


if __name__ == "__main__":
    main()


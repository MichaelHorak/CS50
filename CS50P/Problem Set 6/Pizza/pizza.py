import sys
from tabulate import tabulate


def main():
    verify_input()

    try:
        with open(sys.argv[1], 'r') as file:
            # for line in file:
            # print(tabulate(file, tablefmt='grid'))
            file_list = []
            table = []

            for line in file:
                file_list.append(line)

            item = file_list[0].strip().split(",")
            headers = item
            del file_list[0]
            for item in file_list:
                table.append(item.split(","))

            print(tabulate(table, headers, showindex='false', tablefmt='grid'))

        # outputs a table formatted as ASCII art using tabulate
        # Format the table using the library’s grid format

    # if the specified file does not exist, the program should instead exit via sys.exit
    except FileNotFoundError:
        sys.exit('File does not exist')


def verify_input():
    # If the user does not specify exactly one command-line argument
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    # if the specified file’s name does not end in .csv
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()

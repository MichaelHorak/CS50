import sys
import csv

students = []


def main():
    verify_input()

    try:
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = row['name']
                full_name = full_name.replace(' ', '')
                last, first = full_name.split(',')
                house = row['house']
                students.append({'first': first, 'last': last, 'house': house})

    # if the specified file does not exist, the program should instead exit via sys.exit
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in students:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})
        # writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        # writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        # for student in students:
        #     writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        #     writer.writerow({'first': student['first'], 'last': student['last'], 'house': student['house']})


def verify_input():
    # If the user does not specify exactly one command-line argument
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    # if the specified file’s name does not end in .csv
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')


if __name__ == "__main__":
    main()

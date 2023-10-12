filename = input("Enter name of a file: ")
filename = filename.strip()
filename = filename.lower()

match filename:
    case s if s.endswith('.gif'):
        print('image/gif')
    case s if s.endswith('.jpg'):
        print('image/jpeg')
    case s if s.endswith('.jpeg'):
        print('image/jpeg')
    case s if s.endswith('.png'):
        print('image/png')
    case s if s.endswith('.pdf'):
        print('application/pdf')
    case s if s.endswith('.txt'):
        print('text/plain')
    case s if s.endswith('.zip'):
        print('application/zip')
    case _:
        print("application/octet-stream")

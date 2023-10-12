from watch import parse


def main():
    youtube()


def youtube():
    assert parse("<iframe src=\"http://www.youtube.com/embed/xvFZjo5PgG0\"></iframe>") == "https://youtu.be/xvFZjo5PgG0"
    assert parse("<iframe src=\"http://www.google.com/\"></iframe>") == None


if __name__ == "__main__":
    main()

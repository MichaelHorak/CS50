import re

# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# should return https://youtu.be/xvFZjo5PgG0
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# should return https://youtu.be/xvFZjo5PgG0
# <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
# should return none


def main():
    print(parse(input("HTML: ")))
    # parse(input("HTML: "))


def parse(s):
    try:
        # expect str
        if re.search(r"<iframe (.)*</iframe>", s):
            # value of src of an iframe
            suffix = re.search(r"http(?:s)?://(?:www.)?youtube.com/embed/([a-zA-Z0-9]*)", s)
            # extract youtube url
            # print(suffix.group(1))
            # print(suffix.group(2))
            # print(suffix.group(3))
            youtube_suffix = (suffix.group(1))
            # return youtu.be as str
            return "https://youtu.be/" + youtube_suffix
    except AttributeError:
        return None
# value of src will be in ""
# if no URL return None


if __name__ == "__main__":
    main()

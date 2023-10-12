import re

url = input("URL: ").strip()
# print(url)
# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")


# V2 re.sub
# re.sub(pattern, repl, string, count=0, flags=0)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")


# V3 re.search ?:
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(1))

# V4 filtering out the username
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# re.split(pattern, string, maxsplit=0,
# re.findall(pattern, string, flag=0

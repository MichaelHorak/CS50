import re

email = input("What's your email? ").strip()

# if '@' in email and '.' in email:
#     print('Valid')
# else:
#     print('Invalid')


# V2
# username, domain = email.split('@')
#
# if username and ('.' in domain):
#     print('Valid')
# else:
#     print('Invalid')


# V3
# username, domain = email.split('@')
#
# if username and domain.endswith('.edu'):
#     print('Valid')
# else:
#     print('Invalid')


# V4 using RE
# if re.search('..*@..*', email):
#     print('Valid')
# else:
#     print('Invalid')

# .     any character except a newline
# *     0 or more repetitions
# +     1 or more repetitions
# ?     0 or 1 repetition
# {m}   m repetitions
# {m,n} m-n repetitions


# V5 regex 2
# if re.search(r'.+@.+\.edu', email):
#     print('Valid')
# else:
#     print('Invalid')

# ^ matches the start of the string
# $ matches the end of the string just before the newline
# at the end of the string


# V6 regex 3 ^ $
# if re.search(r"^.+@.+\.edu$", email):
#     print('Valid')
# else:
#     print('Invalid')

# NOT WORKING


# V7 regex [] [^]
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print('Valid')
# else:
#     print('Invalid')

# [] set of characters
# [^] complementing the set (anything except), anything but these characters


# V8 [a-zA-Z0-9_] = \w
# if re.search(r"^\w+@\w+\.edu$", email):
#     print('Valid')
# else:
#     print('Invalid')

# \d      decimal digit
# \D      not a decimal digit
# \s      whitespace characters
# \S      not a whitespace character
# \w        word character ... as well as numbers and the underscore
# \W        not a word character
# A|B       either A or B
# (...)     a group
# (?:...)   non-capturing version
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL


# V9 flags IGNORECASE
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#     print('Valid')
# else:
#     print('Invalid')

# malan@cs50.harvard.edu
# malan@something.cs50.harvard.edu
# malan@harvard.edu


# V10 grouping ideas together
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#     print('Valid')
# else:
#     print('Invalid')

# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)

# V11 validating user input
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')

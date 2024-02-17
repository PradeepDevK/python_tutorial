import re

#^ it's actually sets up the position for match
#it tells the computer that the match must start from this particular point


string = "9python-file"
pattern = r"^91"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
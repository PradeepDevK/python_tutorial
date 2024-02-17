import re

#+ preceeding it must be present at least one time

string = "acc"
pattern = "ab+c"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
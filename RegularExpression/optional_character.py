import re

#? any character which precedes the optional meta-character may or may not be 
#present in the particular string


string = "python-file"
pattern = "python-?file"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
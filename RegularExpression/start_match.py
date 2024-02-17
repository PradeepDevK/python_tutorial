#import regular expression
import re

string = "ababc"
pattern="a"

#match first character
if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')

string1 = "babc"

#search look pattern till end of the string
if re.search(pattern, string):
    print('Macth found')
else:
    print('Match not found')
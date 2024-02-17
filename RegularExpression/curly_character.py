import re

#{...} A curly brace, tells the computer to repeat the preceding character, 
#as many number of times as the value inside the bracket


string = "abbbcc"
pattern = "ab{2}c"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
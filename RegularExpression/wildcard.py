import re

#Notation (.) In states that the . symbol can take place of any other symbol


string = "abbvcc"
pattern = "ab.c"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
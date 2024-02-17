import re

#^ it's actually sets up the position for match
#it tells the computer that the match must start from this particular point


# string = "132313213"
# pattern = r"\d{5}"    #digit characters

# string = "python"
# pattern = r"\D"     #non-digit characters

# string = "python123"
# pattern = r"\w"   #alphanumeric

#Python python
string = "Python"
#pattern = r"[Pp]ython"
pattern = r"[a-zA-Z]"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
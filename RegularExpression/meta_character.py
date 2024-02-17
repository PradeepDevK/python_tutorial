import re

#Most letters & characters match themselves

#Meta Characters: *,+,{...},.,?,^

#* preceding it is present 0 or more times
string = "acbbbccc"
pattern = "ab*c"

if re.match(pattern, string):
    print('Macth found')
else:
    print('Match not found')
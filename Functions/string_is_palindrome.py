word = "mam"

print(word[0])

l = len(word)

#looping through the letters
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-i-1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True

if palindrome_flag:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
word = "mam"

def check_palindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]:
            return False
        
    return True

result = check_palindrome(word)
if result:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")
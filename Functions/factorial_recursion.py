#factorial of 3 is 3*2*1 = 6

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(4))
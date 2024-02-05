n = int(input('Enter numerator'))
d = int(input('Enter denominator'))

result = 0

try:
    result = n / d
except ZeroDivisionError:
    print("Cannot divide number ny zero")
else:
    print(result)
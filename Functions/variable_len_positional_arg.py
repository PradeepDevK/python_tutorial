def add (a, b):
    return a + b

print(add(2, 3))

def add1 (*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add1(2, 3, 4, 10))
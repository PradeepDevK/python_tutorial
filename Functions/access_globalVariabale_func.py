count = 10

def increment():
    global count
    count += 1
    print(count)

increment()
print(count)
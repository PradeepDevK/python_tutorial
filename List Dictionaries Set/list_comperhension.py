a = [1, 2, 3, 4, 5, 6, 7, 8]

result1 = list(map(lambda x: x * 2, a))
print(result1)

# with list comperhension
result2 = [x * 2 for x in a]
print(result2)

#   whenever you are dealing with complex data go with lambda else go with list comperhension



for x in range(5):
    print(x)
    # To don't show the display the a break point here and stop
    if x == 4:
        break
else:
    print("This is the else block")
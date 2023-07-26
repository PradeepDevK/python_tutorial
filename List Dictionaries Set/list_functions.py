fruits = ['Apple', 'Mango', 'Peach', 'Orange', 'Watermelon', 'Grape']
print(fruits)

print("length", len(fruits))

fruits.insert(1, "PineApple")
print(fruits)

fruits.insert(5, "JackFruit")
print(fruits)

fruits.append("Berry")
print(fruits)

#fruits.append(["Guava", "Apricot"]) #making one list inside another list (i.e. nested list)
fruits.extend(["Guava", "Apricot"])
print(fruits)

fruits.remove("Orange")
print(fruits)

fruits.pop()
print(fruits)

print(fruits.index("Peach"))

numbers = [1, 2, 4, 5, 6, 90, 30]
print(numbers)

print(max(numbers))

print(min(numbers))
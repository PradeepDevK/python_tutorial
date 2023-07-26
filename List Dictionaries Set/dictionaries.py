people = {
    "John": 32,
    "Rob": 40,
    "Tim": 20
}

print(people)

print(people["Rob"]) #the key case sensitive here

print(people["Tim"])

#the key can be eiter number / string
people_id = {
    1: "John",
    2: "Rob",
    3: "Tim"
}

print(people_id)

print(people_id[2])

people_id[3] = "Mike" #dictionary mutability
print(people_id)
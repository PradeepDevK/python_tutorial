seta = { 1, 2, 3, 4, 5 }

print(seta)

seta.add(6)

seta.add(2) #it'll not raise a error instead it'll remove duplicate

print(seta)

seta.remove(1)

#seta.remove(20) you will get an error bcoz remove is still search 20 to remove from set

seta.discard(20) #this will not raise an error

print(seta)

seta.pop() #pops out random element from set

print(seta)

seta.clear() #delete all the element from set

print(seta)
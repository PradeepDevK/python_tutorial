s = {'John', 'Rob', 'Mike'}
print('John' in s)
print('Tim' in s)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

print(seta | setb) #union of set

#intersection of two sets (common values)
print(seta & setb)

#difference
print(seta - setb)
print(setb - seta)

#symmetric difference
print(seta ^ setb)
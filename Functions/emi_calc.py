#formual to calculate EMI
#P * R * (1 + R)^N / [(1+R)^N-1]

def emi_calculator(principal, rate, time):
    r = rate / 12 / 100
    emi = (principal * r * (1 + r)**time) / ((1 + r)**time - 1)
    return emi

print(emi_calculator(2000000, 8.75, 180))
print(180 * 20000)
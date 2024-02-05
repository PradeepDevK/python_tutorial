def circle(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference

a,c = circle(10)

print("area", a)
print("circumference", c)
def area_of_circle(radius, pi = 3.14):
    value = pi * radius*radius
    return value

def cost(circle_area, cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost

calcualted_area = area_of_circle(10)
print(calcualted_area)

tc = cost(calcualted_area, 2)
print(tc)
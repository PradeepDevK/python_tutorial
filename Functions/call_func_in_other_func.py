def area_of_circle(radius, pi = 3.14):
    value = pi * radius*radius
    return value

def cost(circle_area, cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost

tc = cost(area_of_circle(10), 2)
print(tc)
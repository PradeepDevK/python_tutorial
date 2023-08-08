products = {
    'phone': 100,
    'tablet': 200,
    'laptop': 300,
    'journal': 400
}

print(products)

product = input("Enter the product to check price: ")
print(f"price of the {product} is {products[product]}")

add_product = input("Enter the product you want to add: ")
add_price = input(f"Enter the price for {add_product}: ")

products[add_product] = add_price

print(f"Product succeddfully updated, here is the updated list {products}")
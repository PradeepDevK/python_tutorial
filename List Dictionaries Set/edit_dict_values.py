products = {
    'phone': 100,
    'tablet': 200,
    'laptop': 300,
    'journal': 400
}

print(products)

edit_product = input("Enter product for which you want to change the price: ")
edit_price = input(f"Enter the new price for {edit_product}: ")

products[edit_product] = int(edit_price)

print(products)
products = {
    'phone': 100,
    'tablet': 200,
    'laptop': 300,
    'journal': 400
}

print(products)

del_product = input("Enter the name of product to be deleted: ")
del products[del_product]

print(f"Product deleted, here are the updated products {products}")
products = ['phone', 'tablet', 'laptop', 'journal']

#displaying products
print(f"Current list of item: {products}")

#asking user to remove a product
remove_item = input("Enter product to remove from the above list: ");
products.remove(remove_item)

#displaying the entire list after removing the item
print(f"Current list of item: {products}")

#code to add product
add_item = input("Enter product to add: ")
products.append(add_item)

#displaying the entire list after adding the item
print(f"Current list of item: {products}")

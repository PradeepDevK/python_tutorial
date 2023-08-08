products = ['phone', 'tablet', 'laptop', 'journal']

#displaying products
print(f"Current list of item: {products}")

#add a product 
add_item = input("Enter product to add: ")

add_after = input(f"after which product do you want to place {add_item}: ")

index = products.index(add_after)
print(index)

products.insert(index + 1, add_item)

#displaying products
print(f"Current list of item: {products}")

def  product(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


product(name = "iphone", price = 700)
product(name = "ipad", price = 400, description = "This is an Ipad")

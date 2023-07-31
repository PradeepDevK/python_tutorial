prices = {
    'iphone': 500,
    'ipad': 400
}

new_prices = {
    'iphone': 600,
    'imac': 1500
}

print(prices)
print(new_prices)

prices.update(new_prices)
print(prices)

prices.pop("ipad")
print(prices)
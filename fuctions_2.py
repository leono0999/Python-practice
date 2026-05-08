def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate / 100
    return discount_amount

item_price = 80
rate = 25

saved = calculate_discount(item_price, rate)
print(saved)
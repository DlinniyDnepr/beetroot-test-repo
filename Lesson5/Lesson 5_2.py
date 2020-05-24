print('Task 2\n')
"""
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.

"""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {}
for fruit, value in stock.items():
    if fruit in prices:
         total_price[fruit] = int(stock[fruit]) * int(prices[fruit])
print(f"Total price of fruits will be: \n{total_price}")
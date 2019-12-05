def charge(price):
    def calc(num):
        return price * num
    return calc


child = charge(400)
adult = charge(1200)

price1 = child(3)
price2 = adult(2)

print(price1)
print(price2)
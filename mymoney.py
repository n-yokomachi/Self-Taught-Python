import exchange

yen = 25000
rate = 114.22
charge = 1.0
dollar = exchange.yen2dollar(yen , rate, charge)
print(f"{dollar :,.2f}ドル")

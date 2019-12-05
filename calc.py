def calc(func, arg = 1):
    price = func(arg)
    return price

def child(arg):
    return 400 * arg

def adult(arg):
    return 1200 * arg

age = 12
num = 3

if age < 16:
    price = calc(child, num)
else:
    price = calc(adult, num)

print(f"{age}歳, {num}人は, {price}円です")

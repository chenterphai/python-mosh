
x = 18
if x > 17:
    print("x is greater than")
else:
    print("x is less")

# otherwise
isHot = True
isCold = True
if isHot:
    print("it's a hot day")
elif isCold:
    print("it's a cold day")
else:
    print("it's a lovely day")

# Exercise
price = 1000000
hasGoodCredit = True
if hasGoodCredit:
    downPayment = price * 0.1
else:
    downPayment = price * 0.2

print(f"Down Payment; $ {downPayment}")

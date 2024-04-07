weight = float(input("Enter your weight: "))
unit = input("Enter unit: ")
if unit.upper() == 'L':
    w = weight * 0.45
    print(f"Your weight is {w} kilos")
else:
    w = weight / 0.45
    print(f"Your weight is {w} bs")

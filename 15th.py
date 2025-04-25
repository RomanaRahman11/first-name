weight = int(input('Weight: '))
unit = input('(L)bs or (k)g:')
if unit.upper() == "K":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

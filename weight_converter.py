user_weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)kg? ')
if unit.upper() == "L":
    print(f"Your weight is {user_weight * 0.453} kilograms")
elif unit.upper() == "K":
    print(f"Your weight is {user_weight * 2.2046} pounds")

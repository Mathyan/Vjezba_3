a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))
rac = str(input("Unesite racunsku operaciju(+,-,*,/): "))
if rac == "+":
    print(f"{a} + {b} = {a+b}")
elif rac == "*":
    print(f"{a} * {b} = {a*b}")
elif rac == "-":
    print(f"{a} - {b} = {a-b}")
elif rac == "/":
    if b == 0 : print("Nemozete djeliti sa nulom")
    else: print(f"{a} / {b} = {a/b}")
else:print("Niste unijeli racunsku.")
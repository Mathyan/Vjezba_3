from math import sqrt
print("Rjesenja ax^2 + bx + c = 0")
a=float(input("Unesite koeficijent a: "))
b=float(input("Unesite koeficijent b: "))
c=float(input("Unesite koeficijent c: "))
if a == 0: 
    print("Ovo nije kvadratna jednadžba")
    exit()
D = b**2-4*a*c
if D>0:
    print(f"Kod a={a},b={b},c={c} x1 = {(-b+sqrt(D))/(2*a)}, te x2 = {(-b-sqrt(D))/(2*a)}")
elif D<0:
    print(f"Kod a={a},b={b},c={c} jednadzba nema realnij rjesenja")
else:
    print(f"Kod a={a},b={b},c={c} x={-b/(2*a)}")
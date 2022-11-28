from math import sqrt
strA = float(input("Unesite duljinu stranice A: "))
strB = float(input("Unesite duljinu stranice B: "))
strC = float(input("Unesite duljinu stranice C: "))
if (strA + strB >= strC) and (strB + strC >= strA) and (strA + strC >= strB):
    print(f"Povrsina trokuta sa stranicama duljine {strA},{strB},{strC} je {0.25*sqrt((strA**2+strB**2+strC**2)**2-2*(strA**4+strB**4+strC**4))} .")
else: print("Unesene dimenzije ne sacinjavaju trokut.")
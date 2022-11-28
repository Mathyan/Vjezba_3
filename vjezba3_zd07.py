from math import log
baza=float(input("Unesite bazu log : "))
broj=float(input("Unesite broj: "))
if broj<=0 or baza <=1: 
    print('Logaritam nije tocno upisan')
    exit()
print(f"log{baza} {broj} = {log(broj,baza)}")
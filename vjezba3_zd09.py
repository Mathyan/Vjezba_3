littera = input("Upisite veliko ili malo slovo: ")
if len(littera)>1: print("Niste upisali jedno slovo")
elif 'a'<=littera<='z':
    print(f"Slovo {littera} je malo te ima ASCI kod {ord(littera)}")
elif 'A'<=littera<='Z':
    print(f"Slovo {littera} je veliko te ima ASCI kod {ord(littera)}")
else:
    print(f"Znak {littera} ne pripada engleskoj abecedi te ima ASCI kod {ord(littera)}")
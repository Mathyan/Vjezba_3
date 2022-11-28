bod = int(input('Upisite broj bodova od 0 do 100: '))
if bod>=0 and bod <= 100:
    if bod<60: print(f"Broj bodova {bod} odgovara ocjeni nedovoljan.")
    elif bod<70: print(f"Broj bodova {bod} odgovara ocjeni dovoljan.")
    elif bod<80: print(f"Broj bodova {bod} odgovara ocjeni dobar.")
    elif bod<90: print(f"Broj bodova {bod} odgovara ocjeni vrlo dobar.")
    else: print(f"Broj bodova {bod} odgovara ocjeni odlican.")
else:print(("Bodovi ne odgovaraju bodovnom rangu."))
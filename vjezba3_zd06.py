broj=int(input("Unesite dekadski broj: "))
baza=int(input("Unesite bazu: "))
if baza == 2: print(f'Dekadski {broj} je u binarnom obliku {bin(broj)}')
elif baza == 8: print(f'Dekadski {broj} je u oktalnom obliku {oct(broj)}')
elif baza == 16: print(f'Dekadski {broj} je u heksadecimalnom obliku {hex(broj)}')
else: print('Nsite upisali odgovarajucu bazu.')
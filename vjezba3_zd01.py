x = int(input("Upisite x koordinatu: "))
y = int(input("Upisite y koordinatu: "))
if x>0 and y>0 :
    print(f'Tocka ({x},{y}) nalazi se u I. kvadrantu.')
elif x<0 and y>0 :
    print(f'Tocka ({x},{y}) nalazi se u II. kvadrantu.')
elif x<0 and y<0 :
    print(f'Tocka ({x},{y}) nalazi se u III. kvadrantu.')
elif x>0 and y<0 :
    print(f'Tocka ({x},{y}) nalazi se u IV. kvadrantu.')
else: print("Koordinate ({x},{y}) se nalaze u sredini")
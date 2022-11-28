rijec=[]
for i in range(5):
    rijec.append(input(f"Upisite znak broj {1+i} "))
a=rijec[0]
b=rijec[0]
c=rijec[0]
d=rijec[0]
e=rijec[0]
rijec = "".join(rijec)
if rijec==rijec[::-1]:
    print(f"Rijec {rijec} je palindom") 
print(f"Prvi znak rijeci {rijec} {a} ima memorijusku lokaciju {id(a)}") 
print(f"Drugi znak rijeci {rijec} {b} ima memorijusku lokaciju {id(b)}")    
print(f"Treci znak rijeci {rijec} {c} ima memorijusku lokaciju {id(c)}")    
print(f"Cetvrti znak rijeci {rijec} {d} ima memorijusku lokaciju {id(d)}")    
print(f"Peti znak rijeci {rijec} {e} ima memorijusku lokaciju {id(e)}")       
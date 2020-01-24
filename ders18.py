
#döngü yapıları

liste= [1,2,3,4,5,6]

for a in liste:
    print(a)
    


listes = [1,2,3,4,5]

toplam = 0

for a in listes:
    toplam += a
    print(toplam)
    
    
aqua = [1,2,3,4,5,6,7,8,9]

for a in aqua:
    if a % 2 != 0:
        print(a)

spiderman = [(1,2),(3,4),(5,6)]

for a,b in spiderman:
    print(a,b)



sozluk = {"cem" :"ben","narcos" :"erdem","bundy" :"faruk"}
for i,j in sozluk.items():
    print(i,j)

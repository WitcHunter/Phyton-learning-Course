# list comprehension

       

    
Cem = [i for i in range(0,51) if i % 2 == 0 and i % 10 == 0]
print(Cem)


listeQ = [(1,2),(3,4),(5,6)]
liste = [i*j for i,j in listeQ]
print(liste)


liste2 = [[1,5,9],[3,5,7],[2,5,8]]

for i in liste2:
    for j in i:
        print(j)
listeM = [x for i in liste2 for x in i]
print(listeM)

listeW = [i**2 for i in range(1,11)]
print(listeW)


Japonya_gidecek_liste = input("İsminizi giriniz:")

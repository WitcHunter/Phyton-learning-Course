"""
@author: user
"""

def enumYapma(liste):
    boşliste = list()
    for i in range(len(liste)):
        boşliste.append((i,liste[i]))
    return boşliste

print(enumYapma(["Mert","Ahmet","Enes"]))

for i,j in enumYapma(["cem","gökhan","Fatma"]):
    print("{}.elemanda : {} isim var".format(i,j))
    

a = list(enumerate(["istanbul","ankara","izmir"]))
print(a)

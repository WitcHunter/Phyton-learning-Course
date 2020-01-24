"""
@author: user
"""
#dosya yazma sistemi 2 (ders 38 )
try:
    file = open("TNT.txt","r")
    print(file.readline() ,end= "")
    print(file.readline() ,end = "")
    print(file.readline() ,end= "")
    liste= file.readlines()
    print(liste)
    for i in liste:
        print(i)
    file.close()
except FileNotFoundError:
    print("Böyle bir dosya bulunmamaktadır.")

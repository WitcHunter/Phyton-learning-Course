# Ders 27 örnekler


def Tamsayıbölenleri(sayı):
    liste = list()
    for i in range(1,sayı+1):
        if sayı % i == 0:
            liste.append(i)
    return liste

print(Tamsayıbölenleri(845865))

            
        
    


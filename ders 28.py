# -*- coding: utf-8 -*-
"""
ALTO TECLAW
ODO(ONLY DREAM ON!)
"""
#ebob(30,15) = 15
#ekok(30,20) = 60

def ebob(a,b):
    kucuksayı= min(a,b)
    ortak_bölenler = list()
    for i in range (1,kucuksayı+1):
        if a % i == 0 and b % i ==0 :
            ortak_bölenler.append(i)
    ortak_bölenler.sort(reverse =True)
    return ortak_bölenler[0]
    

def ekok(a,b):
    pass




print(ebob(1560,475))



#Ûders çok verimsizdi bir daha dinlenilecek


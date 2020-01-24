# -*- coding: utf-8 -*-
"""
Created BY : ALTO TECHLAW

"""
def fonksiyon():
    liste = [x for x in range(100) if x % 6 ==0 ]
    print(liste)
    
fonksiyon()

def fonksiyon(belirle):
    listee = [x for x in range(40) if x % belirle ==0]
    print(listee)
fonksiyon(8)


def foncition(*args):
    toplam = 0
    for i in args:
        toplam += i
        return toplam
    
print(foncition(18,78))
#VİDEO DAKİ GİBİ HEPSİNİ TOPLAMIYOR SADECE ÖNDEWKİ PARAMETREYİ  TOPLUYOR.


def dairealan(r,PI = 3.1415 ):
    return PI*(r**2)


print(dairealan(4,PI=3))

















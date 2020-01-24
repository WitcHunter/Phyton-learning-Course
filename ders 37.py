# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:03:30 2019

@author: user
"""
dosya = open("Recommend.txt","a")
while True:
    yazı=input("Çıkmak için 'q'yazınız\n.Hatırlatma giriniz\nHatırlatmayı gir:")
    if yazı =='q':
        break
    dosya.write("\n{}".format(yazı))
    
dosya.close()


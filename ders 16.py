# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 01:48:42 2019

@author: user
"""

#If/ else blokları

a = 4
b = 3
if b > a:
    print("{}>{}".format(a,b))
    
    
print("bu değer artık doğru bir karar verirse bu artık yazılsın.değilse x.")

c = int(input("c değerini giriniz:"))
d = int(input(" d değerini giriniz:"))
if c>d:
    print("{} > {}".format(c,d))
    print("liverpool")
elif c==d:
    print("{}={}".format(c,d))
    print("CARL YOUNGER")
    
elif c<d:
    print("{}<{}".format(c,d))
    
girilensayı = int(input("sayı giriniz:"))
if girilensayı % 2 == 0:
    print("bu sayı çifttir.")
else:
    print("girilen sayı tektir")

    

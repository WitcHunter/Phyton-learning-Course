4
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:43:28 2019

@author: user
"""


vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))

hesap = vize * 0.4 + final * 0.6
toplam_puan = print("toplam puanınız:",hesap)
if(hesap >=90):
    print("Harf notunuz:ALLAH KATINA MI ÇIKTIN MÜBAREK.")
elif(hesap >=85):
    print("Harf notunuz:HHHAAAHH GÜZELLLLLLL")
elif(hesap >=80):
    print("Harf notunuz:BUĞRA KULLANDIĞIN CONDOM AŞKINA BU NASIL NOT")
elif(hesap >=75):
    print("Harf notunuz BB")
elif(hesap >=70):
    print("Harf notunuz ")
elif(hesap >=65):
    print("Harf notunuz:Lan sen fare kovalarken ben kedi s*kiyordum")
elif(hesap >=50):
    print("Harf notunuz:AAAAğh BÖYLE BİR ŞEY OLABİLİR Mİ YA")
else:
    print("Harf notunuz:KALDINIZ SÜRTÜKLER.HAHHA PARANIZI ÖDEYİN.SOORRR!")
    
    
    
    
    
    
    
    

hesap = """1.toplama
           2.cikarma
           3.carpma
           4.bolme
           5.karesini alma
           6.karekokunu alma
           cikmak q tusunua basin
           """
secim =float(input("yapmak istediginiz islemi giriniz :"))
if secim == 1 :
    sayi1=float(input("birinci sayinizi giriniz :"))
    sayi2= float(input("ikinci sayinizi giriniz :"))
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)
elif secim == 2 :
    sayi3=float(input("birinci sayinizi giriniz :"))
    sayi4= float(input("ikinci sayinizi giriniz :"))
    print(sayi3,"-",sayi4,"=",sayi3-sayi4)
elif secim == 3 :
    sayi5=float(input("birinci sayinizi giriniz :"))
    sayi6= float(input("ikinci sayinizi giriniz :"))
    print(sayi5,"x",sayi6,"=",sayi5*sayi6)
elif secim == 4 :
    sayi7=float(input("birinci sayinizi giriniz :"))
    sayi8= float(input("ikinci sayinizi giriniz :"))
    print(sayi7,"/",sayi8,"=",sayi7/sayi8)
elif secim == 5:
    sayi9=float(input("birinci sayinizi giriniz :"))
    print(sayi9,"^  =",sayi9**2)
elif secim == 6 :
    sayi10=float(input("birinci sayinizi giriniz :"))
    print(sayi10,"in koku = ",sayi10**0.5)





    
    
# -*- coding: utf-8 -*-
"""
@author: user          COMPANY

"""
import sqlite3

baglantı = sqlite3.connect("PANKHUSH COMPANY")
imleç = baglantı.cursor()

def tablo_oluştur():
    imleç.execute("create table if not exists g(Name TEXT,Sallary TEXT,PART TEXT)")
    baglantı.commit()
    
def tablo_veri_ekle(Name,Sallary,PART):
    imleç.execute("insert into  g values(?,?,?)",(Name,Sallary,PART))
    baglantı.commit()
    
def tablo_veri_çek():
    imleç.execute("Select * From g")
    
    veriler = imleç.fetchall()
    print(veriler)
    for i in veriler:
        print(i)
        
tablo_oluştur()
while True:
    veri = input("Veri eklemek için 1,çıkmak için 'q'ya basınız.")
    if veri == 'q':
        break
    Name = input("isim giriniz:")
    Sallary = input("sallary:")
    PART= input("part:")
    tablo_veri_ekle(Name,Sallary,PART)
    
    
    
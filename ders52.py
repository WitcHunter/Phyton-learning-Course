"""
@author: user
"""
import sqlite3
baglantı = sqlite3.connect("Hukuk kitapları.db")
isaretci = baglantı.cursor()

def tablo_oluştur():
    isaretci.execute("create table if not exists K(KitabınAdı TEXT,Kitabınyazarı TEXT,Kitabınalanı TEXT,Kitabınsayfasayısı INT)")
    baglantı.commit()
def tabloya_veri_ekle(KitabınAdı,Kitabınyazarı,Kitabınalanı,Kitabınsayfasayısı):
    isaretci.execute("insert into K values(?,?,?,?)",(KitabınAdı,Kitabınyazarı,Kitabınalanı,Kitabınsayfasayısı))
    baglantı.commit()
    
def tablodan_veri_çek():
    isaretci.execute("Select * From K")
    veriler =isaretci.fetchall()
    for i in veriler:  
        print(i)

tablo_oluştur()
tabloya_veri_ekle("türk anayasa HukukuGenel Esaslar","K.GÖZLER","ANAYASA",390)
tablodan_veri_çek()
baglantı.close()


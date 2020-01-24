#KTO UNIVERSITY SIMULATION
import time as zaman
import sqlite3

class öğrenci():
    def __init__(self):
        self.baglantı = sqlite3.connect("KTO SIMULATION")
        self.işaret = self.baglantı.cursor()
        self.tablo_oluştur()
    def tablo_oluştur(self):
       
        self.işaret.execute("Create table if not exists A(Kişi TEXT,Harf_notu TEXT,Durum TEXT)")
        self.baglantı.commit()
    def tablo_veri_ekle(self,Kişi,Harf_notu,Durum):
        self.işaret.execute("insert into A values(?,?,?)",(Kişi,Harf_notu,Durum))
        self.baglantı.commit()
        
    def tablo_veri_çek(self):
        self.işaret.execute("select * from A")
        veri = self.işaret.fetchall()
        for i in veri :
            print(i)
        self.baglantı.commit()
    def tablo_güncelle(self,isim,yeniisim):
        self.işaret.execute("update A set =? where = ?",(yeniisim,isim))
        self.baglantı.commit()
    def tablo_veri_sil(self,isim):
        self.işaret.execute("delete from A where kişi =?",(isim))
        self.baglantı.commit()
    def Nothesaplama(self,vize,final):
        durum = vize*0.4 + final*0.6
        return durum
    def başarıdurumu(self,durum):
        if durum > 90:
            return "AA"
        elif durum > 85:
            return "AB"
        elif durum > 80:
            return "BB"
        elif durum > 75:
            return "CB"
        elif durum > 70:
            return "CC"
        elif durum > 65:
            return "DC"
        elif durum > 60:
            return "DD"
        else:
            return "FF Dersten Kaldınız" 
                
öğrenci = öğrenci()
while True:
    seçim = input("""
   ***************WELCOME TO DATABASE OF KTO UNIVERSITY***************  
    Veri eklemek için herhangi bir tuşa basınız.Çıkmak için 'q' ya basınız.
    """)
    
    if seçim == 'q':
        break
    
    isim = input("Öğrencinin Adını ve Soyadını giriniz:")
    vize = float(input("vize notunu giriniz:"))
    final = float(input("final notunu giriniz:"))
    print("Hesaplanıyor...",end="")
    
    for i in range(3):
        zaman.sleep(2)
        print(".",end="")
    print("Başarıyla veri tabanına işlenmiştir.")
    durum = öğrenci.Nothesaplama(vize,final)
    Harf_not = öğrenci.başarıdurumu(durum)
    if durum > 60:
        öğrenci.tablo_veri_ekle(isim,Harf_not,"BAŞARILI$")
    else:
        öğrenci.tablo_veri_ekle(isim,Harf_not,"BAŞARISIZ#")
                                
        
       

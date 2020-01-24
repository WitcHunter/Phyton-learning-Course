import time as zaman

""" ufak örnekler """


#döngüleri işlemeye çalışacağız.

print("WELCOME TO LAWBANK.LAWBANK always choices the special customers by itself.That's only presto manifesto\nFOUNDER:CEM ÖZDEMİR\tCEO:ERDEM GÖK\nPlease get into the Card:")
choice = input("If you want get into the card you must choice C,ıf you want get out the card you must choice Q:")
mevcutpara = 4000


if(choice == "C"):
    for i in range(2):
        print("Please loading... SOOOORRRRRRR.Where is my Money? :)",end = "")
        print(".",end = "")
        zaman.sleep(1)
        while True:
            secenek = int(input(""""
            ***************************************
            1-KARTA PARA YÜKLE
            2-KARTTAN PARA ÇEK 
            3-HESAP ÖZETİ 
            4-KART İPTALİ
            5-ÇIKIŞ
            ***************************************
            
            
            """))
            
            while secenek < 1 or secenek > 5:
                secenek = int(input("Belirtilen değer aralığında giriniz!:"))
            if secenek == 1:
                miktar = int(input("Miktarı giriniz:"))
                mevcutpara += miktar
                print("kartınız okunuyor...",end ="")
            elif secenek == 2:
                miktar = int(input("Çekmek istediğiniz miktarı yazınınız:"))
                mevcutpara -= miktar
                
            elif secenek == 3:
                print("""
                ADI:CEM
                SOYADI:ÖZDEMİR
                YAŞI:21
                DOĞUM TARİHİ:25.10.1998
                OKUDUĞU ÜNİVERSİTE:4.SINIFTA İNŞALLAH TORONTO
                IBN :22229999111003322445075
                BAKİYE : {}
                
                
                """.format(miktar))
                
            elif secenek == 4:
                print("Geçici olarak kart iptali durdurulmuştur.Nazik tavrınızdan dolayı teşekkürler")
                
            elif secenek == 5:
                break


                
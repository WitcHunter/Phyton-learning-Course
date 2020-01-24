""" ALTO  hata yakalama"""
while True:
    try:
        kontrol = input("Çıkmak için 'Q' basınız.Devam etmek için 'b' ye basınız.")
        if kontrol == 'Q':
            break
        sayı1 = int(input("Birinci sayıyı giriniz:"))
        sayı2 = int(input("İkici sayıyı giriniz:"))
        print("{}/{} ={}".format(sayı1,sayı2,sayı1/sayı2))
    except:
        print("Hata yaptınız!")
    finally:
        print("Abracadabra")
        
        

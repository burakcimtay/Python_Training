from datetime import datetime as dt

def urun_ekle(secim):
    
    if (secim == "1"):
        urun_adi=input("Urun adi giriniz: ")
        urun_fiyati=input("Urun fiyati giriniz: ")
        sehir=input("Sehir giriniz: ")
        durum=input("Urun durumunu giriniz: ")
        tel_no=input("Telefon Numaraniz: ")
        ad_soyad=input("Adiniz, Soyadiniz: ")
        bugun=dt.today()
        with open("satilik_urunler.txt", "a+") as urun:
            urun.write("Urun Adi: {}\nUrun Fiyati: {}\nSehir: {}\nDurum: {}\nTelefon Numarasi: {}\nAd-Soyad: {}\nUrun Ekleme Tarihi: {}\n\n".format(urun_adi,urun_fiyati,sehir,
                                                                                                                                        durum,tel_no,ad_soyad, bugun))
        urun.close()

def urun_sil():
    
    print("Urunler:\n\n")
    satilik=open("satilik_urunler.txt", "r+")
    for satir in satilik:
        print(satir)
    satilik.close()
    
    i=0
    silinecek_satir=int(input("Hangi Urunu Satin Almak Istiyorsunuz?: \n\n"))
    silinecek_satir=silinecek_satir*8-7
    with open("satilik_urunler.txt", "r") as sil:
        yedek=sil.readlines()
        
        with open("satilik_urunler.txt", "w") as silinen:
            sayac=1
            for satir in yedek:
                
                if sayac!=silinecek_satir:
                    silinen.write(satir)
                    sayac=sayac+1
                    
                if sayac==silinecek_satir:
                    i=i+1
                    if i==9:
                        sayac=sayac+1
                        
        with open("sepet.txt", "w") as sepet:
            sayac=1
            for satir in yedek:
                if sayac==silinecek_satir:
                    sepet.write(satir)
                sayac=sayac+1
                
def fatura():
    with open("sepet.txt", "r+") as sepet:
        yedek=sepet.readlines()
        with open("fatura.txt", "w") as ftr:
            for satir in yedek:
                ftr.write(satir)
        sepet.write("")
        
            

while True:
    islemler="1- Urun satmak istiyorum.\n2- Urun almak istiyorum.\n"
    print(islemler)
    secim=input("Hangi Islemi Yapmak Istiyorsunuz?:\n\n")

    if secim=="1":
        urun_ekle(secim)
    elif secim=="2":
        urun_sil()
        fatura()
    elif (secim=="q"):
        break
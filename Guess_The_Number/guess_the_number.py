import random

sayi=random.randint(1,10)
count=0
kullanici_verisi=0.0

while(True):
    kullanici_verisi=int(input("Tahmininiz: "))
    count=count+1
    if(kullanici_verisi==sayi):
        print("Doğru Bildiniz.\nDeneme Sayiniz: {}".format(count))
        break
    elif(kullanici_verisi!=sayi):
        print("Yanlis Tahmin.")
    elif(kullanici_verisi==99):
        break
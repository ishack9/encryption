import random
import time

zaman=time.localtime()
saniye = zaman.tm_sec


kharf="abcdefghijklmnoprstuvyzqwx"
bharf="ABCDEFGHIJKLMNOPRSTUVYZQWX"
sayılar="0123456789"
semboller="[]{}*;&!/,.-+$#?"


uzunluk=int(input("Şifre Kaç Haneli Olsun :"))
a=int(input("Saniye Gir :"))

while uzunluk >= 91:
    print("En fazla 90 haneli seçebilirsiniz!")
    uzunluk=int(input("Şifre Kaç Haneli Olsun :"))


all = kharf+bharf+sayılar+semboller
parola ="".join(random.sample(all, uzunluk))
print("==============================================")
print(parola)
print("==============================================")

def backtime():
    
    b=a
    
    while (b > 0):
        
        all = kharf+bharf+sayılar+semboller
        parola ="".join(random.sample(all, uzunluk))
        time.sleep(1)
        b -= 1

    if b == 0:
        print(parola)
        print("==============================================")

while True :
    backtime()


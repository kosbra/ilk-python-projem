#tahmin_oyunu.py
import random

def sayi_uret():
    return random.randint(1, 100)

def oyun_baslat():
    hedef = sayi_uret()
    deneme_sayisi = 0
    print("--- Sayı Tahmin Oyununa Hoş Geldin! ---")
    
    while True:
        try:
            tahmin = int(input("1-100 arasında bir tahmin girin: "))
            deneme_sayisi += 1
            
            if tahmin < hedef:
                print("Daha yüksek!")
            elif tahmin > hedef:
                print("Daha düşük!")
            else:
                print(f"Tebrikler! {deneme_sayisi}. denemede bildin.")
                break
        except ValueError:
            print("Lütfen sadece rakam girin!")

oyun_baslat()
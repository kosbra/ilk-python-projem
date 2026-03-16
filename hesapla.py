def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b != 0:
        return a / b
    else:
        return "Hata: Sıfıra bölünemez!"

while True:
    print("\n--- Gelişmiş Hesap Makinesi ---")
    print("İşlemler: 1:+, 2:-, 3:*, 4:/ (Çıkış için 'q')")
    
    secim = input("Seçimin: ")

    if secim.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    if secim in ('1', '2', '3', '4'):
        try:
            s1 = float(input("Birinci sayı: "))
            s2 = float(input("İkinci sayı: "))
            
            if secim == '1': print(f"Sonuç: {topla(s1, s2)}")
            elif secim == '2': print(f"Sonuç: {cikar(s1, s2)}")
            elif secim == '3': print(f"Sonuç: {carp(s1, s2)}")
            elif secim == '4': print(f"Sonuç: {bol(s1, s2)}")
            
        except ValueError:
            print("Hata: Lütfen geçerli sayılar gir!")
    else:
        print("Geçersiz seçim!")
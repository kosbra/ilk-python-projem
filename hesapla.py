# Gelişmiş Hesap Makinesi
sayi1 = float(input("Birinci sayıyı gir: "))
sayi2 = float(input("İkinci sayıyı gir: "))

print("\nİşlemler: 1:Topla(+), 2:Çıkar(-), 3:Çarp(*), 4:Böl(/)")
secim = input("Seçimin (1/2/3/4): ")

if secim == '1':
    print(f"Sonuç: {sayi1 + sayi2}")
elif secim == '2':
    print(f"Sonuç: {sayi1 - sayi2}")
elif secim == '3':
    print(f"Sonuç: {sayi1 * sayi2}")
elif secim == '4':
    if sayi2 != 0:
        print(f"Sonuç: {sayi1 / sayi2}")
    else:
        print("Hata: Bir sayı sıfıra bölünemez!")
else:
    print("Geçersiz seçim yaptınız!")
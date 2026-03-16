while True:
    print("\n--- Hesap Makinesi (Çıkmak için 'q' tuşuna basın) ---")
    
    secim = input("Yapmak istediğiniz işlem (1:+, 2:-, 3:*, 4:/ veya q): ")

    if secim.lower() == 'q':
        print("Programdan çıkılıyor, iyi günler!")
        break

    if secim in ('1', '2', '3', '4'):
        try:
            sayi1 = float(input("Birinci sayıyı gir: "))
            sayi2 = float(input("İkinci sayıyı gir: "))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")
            continue

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
                print("Hata: Sıfıra bölünemez!")
    else:
        print("Geçersiz seçim!")
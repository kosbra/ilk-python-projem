import tkinter as tk
import random

# 1. Puanları saklayacağımız bir sözlük (Dictionary) oluşturuyoruz
puanlar = {"Galatasaray": 0, "Fenerbahçe": 0}

def mac_yap():
    ev_skor = random.randint(0, 5)
    dep_skor = random.randint(0, 5)
    
    # Skoru ekrana yazdırıyoruz
    sonuc_etiketi.config(text=f"Galatasaray {ev_skor} - {dep_skor} Fenerbahçe")
    
    # 2. Puan Mantığı: Kim kazandıysa +3, beraberlikte +1
    if ev_skor > dep_skor:
        puanlar["Galatasaray"] += 3
        yorum_etiketi.config(text="Galatasaray kazandı!", fg="orange")
    elif dep_skor > ev_skor:
        puanlar["Fenerbahçe"] += 3
        yorum_etiketi.config(text="Fenerbahçe kazandı!", fg="darkblue")
    else:
        puanlar["Galatasaray"] += 1
        puanlar["Fenerbahçe"] += 1
        yorum_etiketi.config(text="Dostluk kazandı (Berabere)!", fg="gray")
    
    # 3. Görsel Tabloyu Güncelleme
    tablo_etiketi.config(text=f"GS: {puanlar['Galatasaray']} Puan | FB: {puanlar['Fenerbahçe']} Puan")

pencere = tk.Tk()
pencere.title("Derbi Puan Takip Sistemi")
pencere.geometry("450x400")

tk.Label(pencere, text="🏆 Süper Lig Simülatörü", font=("Arial", 16, "bold")).pack(pady=15)

# Puan Durumu Alanı
tablo_etiketi = tk.Label(pencere, text="GS: 0 Puan | FB: 0 Puan", font=("Arial", 12, "bold"), bg="yellow")
tablo_etiketi.pack(pady=5)

buton = tk.Button(pencere, text="Maçı Oynat", command=mac_yap, font=("Arial", 12), bg="green", fg="white")
buton.pack(pady=15)

sonuc_etiketi = tk.Label(pencere, text="Maç bekleniyor...", font=("Arial", 14))
sonuc_etiketi.pack(pady=10)

yorum_etiketi = tk.Label(pencere, text="", font=("Arial", 12, "italic"))
yorum_etiketi.pack(pady=10)

pencere.mainloop()
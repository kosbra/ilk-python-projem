#super_lig_sim.py
import tkinter as tk
from tkinter import messagebox
import random

# 1. Takımlar ve "Logo" Emojileri
takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
logolar = {"Galatasaray": "🦁", "Fenerbahçe": "🐦", "Beşiktaş": "🦅", "Trabzonspor": "🌊"}
puanlar = {takim: 0 for takim in takimlar}
toplam_mac = 0

def lig_maci_yap():
    global toplam_mac
    
    # Sezon bittiyse yeni maç yaptırma
    if toplam_mac >= 12:
        sampiyonu_ilan_et()
        return

    ev_sahibi, deplasman = random.sample(takimlar, 2)
    ev_skor = random.randint(0, 4)
    dep_skor = random.randint(0, 4)
    
    # Görsel skor (Logolarla birlikte)
    skor_metni = f"{logolar[ev_sahibi]} {ev_sahibi} {ev_skor} - {dep_skor} {deplasman} {logolar[deplasman]}"
    sonuc_etiketi.config(text=skor_metni)
    
    # Puan Dağıtımı
    if ev_skor > dep_skor:
        puanlar[ev_sahibi] += 3
    elif dep_skor > ev_skor:
        puanlar[deplasman] += 3
    else:
        puanlar[ev_sahibi] += 1
        puanlar[deplasman] += 1
    
    toplam_mac += 1
    tabloyu_guncelle()
    
    # 12. maçtan sonra otomatik bitir
    if toplam_mac == 12:
        sampiyonu_ilan_et()

def tabloyu_guncelle():
    sirali_liste = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)
    tablo_metni = "🏆 PUAN DURUMU 🏆\n" + "-"*30 + "\n"
    for takim, puan in sirali_liste:
        tablo_metni += f"{logolar[takim]} {takim}: {puan} Puan\n"
    tablo_etiketi.config(text=tablo_metni)

def sampiyonu_ilan_et():
    sirali = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)
    sampiyon = sirali[0][0]
    puan = sirali[0][1]
    messagebox.showinfo("Sezon Bitti!", f"TEBRİKLER!\n\n{logolar[sampiyon]} {sampiyon} {puan} puanla ŞAMPİYON OLDU!")

# Arayüz Ayarları
pencere = tk.Tk()
pencere.title("Süper Lig Sezon Simülatörü")
pencere.geometry("450x550")

tk.Label(pencere, text="⚽ Pro Lig Yönetimi", font=("Arial", 18, "bold"), fg="darkgreen").pack(pady=10)

tablo_etiketi = tk.Label(pencere, text="", font=("Courier", 12, "bold"), justify="left", bg="#f0f0f0", width=35, relief="ridge")
tablo_etiketi.pack(pady=10)

buton = tk.Button(pencere, text="Haftanın Maçını Oynat", command=lig_maci_yap, font=("Arial", 12, "bold"), bg="blue", fg="white", height=2)
buton.pack(pady=20)

sonuc_etiketi = tk.Label(pencere, text="Sezonu başlatmak için butona basın!", font=("Arial", 11, "italic"))
sonuc_etiketi.pack(pady=10)

tabloyu_guncelle()
pencere.mainloop()
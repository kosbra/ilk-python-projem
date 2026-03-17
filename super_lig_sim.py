#super_lig_sim.py
import tkinter as tk
import random

# 1. Takımlar ve Puan Durumu
takimlar = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
puanlar = {takim: 0 for takim in takimlar}

def lig_maci_yap():
    # Rastgele iki takım seç (aynı takım olmasın)
    ev_sahibi, deplasman = random.sample(takimlar, 2)
    
    ev_skor = random.randint(0, 4)
    dep_skor = random.randint(0, 4)
    
    skor_metni = f"{ev_sahibi} {ev_skor} - {dep_skor} {deplasman}"
    sonuc_etiketi.config(text=skor_metni)
    
    # Puan Dağıtımı
    if ev_skor > dep_skor:
        puanlar[ev_sahibi] += 3
    elif dep_skor > ev_skor:
        puanlar[deplasman] += 3
    else:
        puanlar[ev_sahibi] += 1
        puanlar[deplasman] += 1
    
    tabloyu_guncelle()

def tabloyu_guncelle():
    # Puanları yüksekten düşüğe sıralayalım (Biraz ileri seviye ama şık durur)
    sirali_liste = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)
    
    tablo_metni = "🏆 PUAN DURUMU 🏆\n" + "-"*25 + "\n"
    for takim, puan in sirali_liste:
        tablo_metni += f"{takim}: {puan} Puan\n"
    
    tablo_etiketi.config(text=tablo_metni)

# Görsel Arayüz
pencere = tk.Tk()
pencere.title("4 Takımlı Süper Lig")
pencere.geometry("400x500")

tk.Label(pencere, text="⚽ Mini Lig Simülatörü", font=("Arial", 16, "bold")).pack(pady=10)

tablo_etiketi = tk.Label(pencere, text="Puanlar yükleniyor...", font=("Courier", 12), justify="left", bg="lightgrey", width=30)
tablo_etiketi.pack(pady=10)

buton = tk.Button(pencere, text="Yeni Maç Oynat", command=lig_maci_yap, font=("Arial", 12, "bold"), bg="blue", fg="white")
buton.pack(pady=20)

sonuc_etiketi = tk.Label(pencere, text="Haftanın maçını başlatın!", font=("Arial", 13, "italic"))
sonuc_etiketi.pack(pady=10)

# İlk açılışta tabloyu bir kez göster
tabloyu_guncelle()

pencere.mainloop()
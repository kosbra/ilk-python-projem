#Maç sonucu tahmin edici
import tkinter as tk
import random

def mac_yap():
    ev_skor = random.randint(0, 5)
    dep_skor = random.randint(0, 5)
    sonuc_etiketi.config(text=f"Galatasaray {ev_skor} - {dep_skor} Fenerbahçe")
    
    if ev_skor > dep_skor:
        yorum_etiketi.config(text="Ev sahibi kazandı!", fg="orange")
    elif dep_skor > ev_skor:
        yorum_etiketi.config(text="Deplasman kazandı!", fg="darkblue")
    else:
        yorum_etiketi.config(text="Beraberlik!", fg="gray")

pencere = tk.Tk()
pencere.title("Mini Lig Simülasyonu")
pencere.geometry("400x300")

tk.Label(pencere, text="Haftanın Derbisi", font=("Arial", 16, "bold")).pack(pady=20)

buton = tk.Button(pencere, text="Maçı Oynat", command=mac_yap, font=("Arial", 12), bg="green", fg="white")
buton.pack(pady=10)

sonuc_etiketi = tk.Label(pencere, text="Maç bekleniyor...", font=("Arial", 14))
sonuc_etiketi.pack(pady=10)

yorum_etiketi = tk.Label(pencere, text="", font=("Arial", 12, "italic"))
yorum_etiketi.pack(pady=10)

pencere.mainloop()
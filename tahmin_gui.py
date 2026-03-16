#tahmin_gui.py.
import tkinter as tk
from tkinter import messagebox
import random

# Bilgisayarın tuttuğu sayı
hedef = random.randint(1, 100)
deneme = 0

def kontrol_et():
    global deneme
    try:
        tahmin = int(giriş_kutusu.get())
        deneme += 1
        
        if tahmin < hedef:
            sonuç_etiketi.config(text="Daha YÜKSEK bir sayı gir!", fg="blue")
        elif tahmin > hedef:
            sonuç_etiketi.config(text="Daha DÜŞÜK bir sayı gir!", fg="red")
        else:
            messagebox.showinfo("Tebrikler!", f"{deneme}. denemede bildin!")
            pencere.destroy() # Oyunu kapatır
    except ValueError:
        messagebox.showerror("Hata", "Lütfen sadece sayı girin!")

pencere = tk.Tk()
pencere.title("Sayı Tahmin Oyunu - GUI")
pencere.geometry("350x250")

tk.Label(pencere, text="1-100 arası bir sayı tuttum:", font=("Arial", 12)).pack(pady=10)

giriş_kutusu = tk.Entry(pencere, font=("Arial", 14))
giriş_kutusu.pack(pady=5)

buton = tk.Button(pencere, text="Tahmin Et", command=kontrol_et, bg="green", fg="white", font=("Arial", 10, "bold"))
buton.pack(pady=10)

sonuç_etiketi = tk.Label(pencere, text="", font=("Arial", 11))
sonuç_etiketi.pack(pady=10)

pencere.mainloop()
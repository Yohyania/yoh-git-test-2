import tkinter as tk

root = tk.Tk()

# bikin Label dengan font Comic Sans MS ukuran 50 italic
Font1 = tk.Label(root, text="Halo dari Mars", font=("Comic Sans MS",50,"italic")) #label untuk teks/gambar
Font1.pack() # agar label muncul di jendela

Button1 = tk.Button(root, text="Tombol Muncul", font=("Arial",20,"bold")) #button untuk tombol
Button1.pack()

root.mainloop() # biar jendela tetap terbuka
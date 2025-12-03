# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# prog03.py

from PIL import Image, ImageTk
import tkinter as tk
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
root = tk.Tk()
root.title("Faculdade SENAI - PDI - 2025-2")
photo = ImageTk.PhotoImage(im)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
btn_ok = tk.Button(root, text="OK", command=root.destroy)
btn_ok.pack()
root.mainloop()

# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog01.py

'''
We can use the routine split() to split an image into its constituent
channels. We can also merge various images into a single image with the
routine merge(). Listing 4-1 shows a demonstration of this.
'''

from PIL import Image, ImageTk
import tkinter as tk
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
root = tk.Tk()
root.title("RED Channel Demo")
r, g, b = im.split()
photo1 = ImageTk.PhotoImage(r)
l1 = tk.Label(root, image=photo1)
l1.pack()
l1.photo = photo1

photo1 = ImageTk.PhotoImage(g)
l1 = tk.Label(root, image=photo1)
l1.pack()
l1.photo = photo1

photo3 = ImageTk.PhotoImage(Image.merge("RGB", (r, g, b)))
l3 = tk.Label(root, image=photo3)
l3.pack()
l3.photo = photo3

root.mainloop()


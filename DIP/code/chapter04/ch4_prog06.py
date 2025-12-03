# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog06.py

'''
We can
also transpose the images using the transpose() function.
It takes one of PIL.Image.FLIP_LEFT_RIGHT,
				PIL.Image.FLIP_TOP_BOTTOM,
				PIL.Image.ROTATE_90,
				PIL.Image.ROTATE_180,
				PIL.Image.ROTATE_270, or
				PIL.Image.TRANSPOSE
as an argument. The code below shows a rotation at 180 degrees.

Also, the following line will flip the image vertically:
	out = im.transpose(Image.FLIP_TOP_BOTTOM)
'''

from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()
root.title("Transpose Demo")
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
# out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
photo = ImageTk.PhotoImage(out)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
root.mainloop()

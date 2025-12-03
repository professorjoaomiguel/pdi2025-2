# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog02.py

'''
Colorspace Conversion
You can change the mode of an image using the routine convert(), as
shown below. 
The code below changes the mode of the image to L. The
routine convert() supports all possible conversions between the RGB,
CMYK, and L modes. We can read more about the colorspaces at
https://www.color-management-guide.com/color-spaces.html
'''

from PIL import Image, ImageTk
import tkinter as tk
im1 = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
res1 = im1.convert("L")
root = tk.Tk()
root.title("Colorspace Conversion Demo")
photo = ImageTk.PhotoImage(res1)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
root.mainloop()

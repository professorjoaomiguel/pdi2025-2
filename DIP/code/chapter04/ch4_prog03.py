# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog03.py

'''
Image Blending
We can blend two images using the blend() method. It takes three
arguments—two images to be blended and the value of alpha. The
mathematical formula it uses for blending is as follows:

	output = image1 * (1.0 - alpha) + image2 * alpha

Now, we will write a program that can change the value of alpha so
that we can experience the blending effect ourselves. 
We will use the scale widget in Tkinter.
'''

from PIL import Image, ImageTk
import tkinter as tk

def show_value_1(alpha):
	print('Alpha: ', alpha)
	img = Image.blend(im1, im2, float(alpha))
	photo = ImageTk.PhotoImage(img)
	l['image'] = photo
	l.photo = photo
	
root = tk.Tk()
root.title('Blending Demo')
im1 = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
im2 = Image.open("/home/pi/DIP/dataset/4.1.08.tiff")
photo = ImageTk.PhotoImage(im1)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
w1 = (tk.Scale(root, label="Alpha", from_=0, to=1,resolution=0.01, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()
root.mainloop()

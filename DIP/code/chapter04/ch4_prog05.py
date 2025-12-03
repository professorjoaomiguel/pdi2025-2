# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog05.py

'''
Rotating an Image
We can use the routine rotate(), which takes the angle of
rotation as an argument. The code below demonstrates this idea.
Run this code to experience the rotation effect on an image.
'''

from PIL import Image, ImageTk
import tkinter as tk
def show_value_1(angle):
	print('Angle: ', angle)
	img = im.rotate(float(angle))
	photo = ImageTk.PhotoImage(img)
	l['image'] = photo
	l.photo = photo

root = tk.Tk()
root.title("Rotation Demo")
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
photo = ImageTk.PhotoImage(im)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
w1 = (tk.Scale(root, label="Angle", from_=0, to=180,
      resolution=1, command=show_value_1, orient=tk.
      HORIZONTAL))
w1.pack()
root.mainloop()

# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog04.py

'''
Resizing an Image
You can resize an imageusing the routine resize(), as shown in
This example varies the image size from (128, 128) to (512, 512).
The routine resize() takes the new size tuple as an argument.
The code also invokes the Tkinter window in full-screen mode
with the root.attributes() function call. To close this 
window, you have to press Alt+F4 from the keyboard.
Run the code and have a look at the output.
'''

from PIL import Image, ImageTk
import tkinter as tk
def show_value_1(size):
	print('Resize: ', size, ' : ', size)
	img = im.resize((int(size), int(size)))
	photo = ImageTk.PhotoImage(img)
	l['image'] = photo
	l.photo = photo

root = tk.Tk()
root.attributes('-fullscreen', True)
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
photo = ImageTk.PhotoImage(im)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo
w1 = (tk.Scale(root, label="Resize", from_=128,to=512, resolution=1, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()
root.mainloop()

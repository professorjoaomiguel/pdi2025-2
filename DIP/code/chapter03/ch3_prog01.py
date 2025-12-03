# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch3_prog01.py

'''
It will show the image in an xli window. This is the simplest Pillow
program; it loads an image in a Python variable with the function call
open() and displays it with the function call show(). In the first line, we are
importing the Image module of Pillow. We will learn more about this module
in the next chapter. The standard version of show() is not very efficient,
because it saves the image to a temporary file and calls the xv utility to
display the image. However, it is handy for the purposes of debugging.
'''

from PIL import Image
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
im.show()

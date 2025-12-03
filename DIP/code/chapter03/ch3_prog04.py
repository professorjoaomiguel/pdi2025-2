# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# prog04.py
# We can also check the properties of an image as follows:

from PIL import Image
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
print("mode:", im.mode)
print("format:", im.format)
print("size:", im.size)
print("info:", im.info)
print("bands:", im.getbands())

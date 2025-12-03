# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# prog03_comment.py

# Importa as classes Image e ImageTk da biblioteca Pillow (PIL)
from PIL import Image, ImageTk

# Importa a biblioteca Tkinter para criar a interface gráfica (GUI)
import tkinter as tk

# Abre o arquivo de imagem especificado e o carrega em um objeto 'im'
im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")

# Cria a janela principal da aplicação e a atribui à variável 'root'
root = tk.Tk()

# Define o texto que aparecerá na barra de título da janela
root.title("Faculdade SENAI - PDI - 2025-2")

# Converte a imagem do Pillow ('im') para um formato que o Tkinter entende
photo = ImageTk.PhotoImage(im)

# Cria um widget 'Label' (etiqueta) para exibir a imagem 'photo' dentro da janela 'root'
l = tk.Label(root, image=photo)

# Adiciona o Label à janela, ajustando o tamanho da janela ao da imagem
l.pack()

# Mantém uma referência à imagem para evitar que ela seja 'coletada como lixo' (desapareça)
l.photo = photo

# Cria um widget 'Button' (botão) dentro da janela 'root'
btn_ok = tk.Button(root, text="OK", command=root.destroy)

# Adiciona o botão à janela, posicionando-o abaixo do widget anterior (a imagem)
btn_ok.pack()

# Inicia o loop principal da aplicação, que aguarda por eventos (cliques, teclado, etc.)
root.mainloop()

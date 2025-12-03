# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog04.py


from PIL import Image, ImageTk       # Importa classes do Pillow para manipulação de imagem (Image) e Tkinter (ImageTk)
import tkinter as tk                 # Importa a biblioteca Tkinter para interface gráfica (GUI)

# --- VARIÁVEIS GLOBAIS ---
# Variáveis que serão usadas dentro e fora da função de callback
im_original = None  # Variável para armazenar a imagem original carregada
l_resized = None    # Label para a imagem redimensionada
l_original = None   # Label para a imagem original (para comparação)


# --- FUNÇÃO DE CALLBACK PARA O WIDGET SCALE ---

def show_value_1(size_str):
    """
    Função chamada sempre que o valor do Scale (Tamanho) é alterado.
    Redimensiona a imagem e atualiza o display.
    """
    try:
        # Converte o valor string do scale para inteiro
        size = int(size_str)
        print(f'Redimensionamento: {size} x {size} pixels')
        
        # 1. Redimensionamento da Imagem
        # A rotina resize() usa a nova tupla (largura, altura) como argumento.
        # Ela aplica um filtro de resampling (amostragem) padrão (geralmente LANCZOS para qualidade).
        img_resized = im_original.resize((size, size))

        # 2. Atualiza o Label da Imagem Redimensionada
        photo = ImageTk.PhotoImage(img_resized)
        
        # Usa .config() para atualizar a imagem no Label
        l_resized.config(image=photo) 
        l_resized.photo = photo        # Mantém a referência
        
    except ValueError:
        print("Erro: O valor de redimensionamento não é válido.")


# ---------------------------------------------------------------
# --- CRIAÇÃO DA INTERFACE GRÁFICA (LAYOUT) ---
# ---------------------------------------------------------------

# 1. Configuração da Janela Tkinter
root = tk.Tk()
root.title("Processamento de Imagens 2025-2 | Demonstração de Redimensionamento")

# Remove a linha de tela cheia ('-fullscreen', True) para melhor usabilidade em demonstrações,
# e adiciona um botão de fechamento. 
# Se a tela cheia for essencial, adicione: root.attributes('-fullscreen', True)

# 2. Carregamento da Imagem Original
try:
    im_original = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
except FileNotFoundError:
    print("Erro: Imagem não encontrada. Usando substituta.")
    im_original = Image.new('RGB', (512, 512), color='gray')


# --- LAYOUT DE COMPARAÇÃO (ORIGINAL vs. REDIMENSIONADA) ---

# Frame principal para conter as duas imagens lado a lado
frame_display = tk.Frame(root)
frame_display.pack(side="top", pady=10)

# Frame para o controle (Scale)
frame_control = tk.Frame(root)
frame_control.pack(side="top", pady=10)

# --- Lado Esquerdo: Imagem Original (Referência) ---
photo_original = ImageTk.PhotoImage(im_original)
l_original = tk.Label(frame_display, image=photo_original)
l_original.pack(side="left", padx=10)
l_original.photo = photo_original
tk.Label(frame_display, text="Original",
         font=('Helvetica', 10, 'bold')).pack(side="left")

# --- Lado Direito: Imagem Redimensionada (Será Atualizada) ---
# Inicializa com o tamanho original ou com o valor inicial do Scale (ex: 128x128)
initial_size = 128
initial_img = im_original.resize((initial_size, initial_size))
photo_resized = ImageTk.PhotoImage(initial_img)

l_resized = tk.Label(frame_display, image=photo_resized)
l_resized.pack(side="right", padx=10)
l_resized.photo = photo_resized
tk.Label(frame_display, text="Redimensionada",
         font=('Helvetica', 10, 'bold')).pack(side="right")


# --- CONTROLE (SCALE) ---

# Cria o Widget Scale para variar o tamanho
w1 = tk.Scale(frame_control, label="Tamanho (Largura e Altura)", 
              from_=128, to=512, resolution=1, 
              command=show_value_1, orient=tk.HORIZONTAL, length=500)
w1.set(initial_size) # Define o valor inicial
w1.pack(side="left", padx=10)


# --- BOTÃO DE FECHAMENTO ---
btn_close = tk.Button(root, text="Fechar Aplicação",
                      command=root.destroy)
btn_close.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()

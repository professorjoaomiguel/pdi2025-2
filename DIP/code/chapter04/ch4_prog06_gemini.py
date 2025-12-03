# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog06.py

from PIL import Image, ImageTk, Image as Img # Importa classes do Pillow. Img é usado para referenciar constantes.
import tkinter as tk                         # Importa a biblioteca Tkinter para interface gráfica (GUI)
from tkinter import ttk                      # Importa ttk para widgets mais modernos (opcional)

# --- VARIÁVEIS GLOBAIS E CONSTANTES ---
im_original = None                           # Armazena a imagem original carregada
l_output = None                              # Label para a imagem transformada (Resultado)
opcoes_transposicao = {
    "Espelhar Horizontalmente": Img.FLIP_LEFT_RIGHT,
    "Espelhar Verticalmente": Img.FLIP_TOP_BOTTOM,
    "Girar 90°": Img.ROTATE_90,
    "Girar 180°": Img.ROTATE_180,
    "Girar 270°": Img.ROTATE_270,
    "Transpor (Espelhar e Rotacionar)": Img.TRANSPOSE
}
# Variável de controle para o OptionMenu, inicializada com uma opção padrão
variavel_transposicao = None 


# --- FUNÇÃO DE CALLBACK PARA O MENU DE SELEÇÃO ---

def aplicar_transposicao(opcao_selecionada):
    """
    Função chamada quando uma nova opção é selecionada no menu.
    Aplica a transformação geométrica e atualiza a imagem de saída.
    """
    # 1. Obtém o método (constante PIL) correspondente à opção de texto
    metodo_pil = opcoes_transposicao[opcao_selecionada]
    
    # 2. Executa a Transposição (Transformação Geométrica)
    # A função transpose() realiza o espelhamento ou rotação em múltiplos de 90°.
    img_transformada = im_original.transpose(metodo_pil)
    
    # 3. Atualiza o Label da Imagem de Saída (l_output)
    photo = ImageTk.PhotoImage(img_transformada)
    
    # Atualiza a imagem no Label
    l_output.config(image=photo) 
    l_output.photo = photo        # Mantém a referência

    print(f"Transformação aplicada: {opcao_selecionada}")


# ---------------------------------------------------------------
# --- CRIAÇÃO DA INTERFACE GRÁFICA (LAYOUT) ---
# ---------------------------------------------------------------

# 1. Configuração da Janela Tkinter
root = tk.Tk()
root.title("Processamento de Imagens 2025-2 | Demonstração de Transposição (Geométrica)")

# 2. Carregamento da Imagem Original
try:
    im_original = Img.open("/home/pi/DIP/dataset/4.1.07.tiff")
except FileNotFoundError:
    print("Erro: Imagem não encontrada. Usando substituta.")
    im_original = Img.new('RGB', (256, 256), color='gray')


# --- LAYOUT DE COMPARAÇÃO (ORIGINAL vs. TRANSFORMADA) ---

# Frame principal para conter os displays lado a lado
frame_display = tk.Frame(root)
frame_display.pack(side="top", pady=15)

# --- Lado Esquerdo: Imagem Original (Referência) ---
tk.Label(frame_display, text="Original", font=('Helvetica', 10, 'bold')).pack(side="left", padx=10, anchor="s")

photo_original = ImageTk.PhotoImage(im_original)
l_original = tk.Label(frame_display, image=photo_original)
l_original.pack(side="left", padx=10)
l_original.photo = photo_original


# --- Lado Direito: Imagem Transformada (Resultado) ---
# Inicializa a imagem de saída com a imagem original
photo_output_init = ImageTk.PhotoImage(im_original)

l_output = tk.Label(frame_display, image=photo_output_init)
l_output.pack(side="right", padx=10)
l_output.photo = photo_output_init

tk.Label(frame_display, text="Transformada", font=('Helvetica', 10, 'bold')).pack(side="right", padx=10, anchor="s")


# --- CONTROLE DE SELEÇÃO ---

# Frame para agrupar o controle e o botão
frame_control = tk.Frame(root)
frame_control.pack(side="top", pady=10)

# Variável de controle Tkinter inicializada
variavel_transposicao = tk.StringVar(root)
# Define o valor inicial como a primeira chave do dicionário
variavel_transposicao.set(list(opcoes_transposicao.keys())[0])

# Cria o OptionMenu (Menu de Seleção)
menu_opcoes = tk.OptionMenu(frame_control, variavel_transposicao, 
                             *opcoes_transposicao.keys(), 
                             command=aplicar_transposicao)
menu_opcoes.config(width=30)
tk.Label(frame_control, text="Selecione a Transformação:").pack(side="left", padx=5)
menu_opcoes.pack(side="left", padx=10)

# --- BOTÃO DE FECHAMENTO ---
btn_close = tk.Button(root, text="Fechar Aplicação", command=root.destroy)
btn_close.pack(pady=10)

# Garante que a primeira transformação seja aplicada na inicialização
aplicar_transposicao(variavel_transposicao.get())

# Inicia o loop principal do Tkinter
root.mainloop()

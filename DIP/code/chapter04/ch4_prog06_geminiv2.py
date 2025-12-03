# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog06.py

from PIL import Image, ImageTk, Image as Img # Importa classes do Pillow. Img é usado para referenciar constantes.
import tkinter as tk                         # Importa a biblioteca Tkinter para interface gráfica (GUI)

# --- VARIÁVEIS GLOBAIS E CONSTANTES ---
im_original = None                           # Armazena a imagem original carregada
l_output = None                              # Label para a imagem transformada (Resultado)

# Dicionário de transformações: Nome amigável -> Constante PIL.Image
opcoes_transposicao = {
    "Espelhar Horizontalmente": Img.FLIP_LEFT_RIGHT,
    "Espelhar Verticalmente": Img.FLIP_TOP_BOTTOM,
    "Girar 90°": Img.ROTATE_90,
    "Girar 180°": Img.ROTATE_180,
    "Girar 270°": Img.ROTATE_270,
    "Transpor (Girar + Espelhar)": Img.TRANSPOSE
}

# --- FUNÇÃO DE APLICAÇÃO ---

def aplicar_transposicao(metodo_pil, nome_transformacao):
    """
    Função chamada pelo clique do botão.
    Aplica a transformação geométrica e atualiza a imagem de saída.
    """
    # 1. Executa a Transposição (Transformação Geométrica)
    # Usa a constante PIL.Image passada pelo botão.
    img_transformada = im_original.transpose(metodo_pil)
    
    # 2. Atualiza o Label da Imagem de Saída (l_output)
    photo = ImageTk.PhotoImage(img_transformada)
    
    # Atualiza a imagem no Label
    l_output.config(image=photo) 
    l_output.photo = photo        # Mantém a referência

    # Feedback no console
    print(f"Transformação aplicada: {nome_transformacao} ({metodo_pil})")


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
photo_original = ImageTk.PhotoImage(im_original)
l_original = tk.Label(frame_display, image=photo_original)
l_original.pack(side="left", padx=10)
l_original.photo = photo_original

tk.Label(frame_display, text="Original",
         font=('Helvetica', 10, 'bold')).pack(side="left", padx=10, anchor="s")


# --- Lado Direito: Imagem Transformada (Resultado) ---
# Inicializa a imagem de saída com a imagem original
photo_output_init = ImageTk.PhotoImage(im_original)

l_output = tk.Label(frame_display, image=photo_output_init)
l_output.pack(side="right", padx=10)
l_output.photo = photo_output_init

tk.Label(frame_display, text="Transformada",
         font=('Helvetica', 10, 'bold')).pack(side="right", padx=10, anchor="s")


# -------------------------------------------------------
# --- CONTROLE: BOTÕES ESPECÍFICOS ---
# -------------------------------------------------------

# Frame para agrupar os botões (pode ser necessário mais de uma linha, dependendo da tela)
frame_botoes = tk.Frame(root)
frame_botoes.pack(side="top", pady=15)

# Loop que cria um botão para cada tipo de transposição
for nome, metodo in opcoes_transposicao.items():
    # Cria um botão, usando lambda para chamar a função com os argumentos corretos
    btn = tk.Button(frame_botoes, text=nome,
                    # Lambda garante que a função aplicar_transposicao seja chamada
                    # apenas no clique, passando a constante (metodo) e o nome.
                    command=lambda m=metodo, n=nome: aplicar_transposicao(m, n))
    btn.pack(side="left", padx=5, pady=5)


# --- BOTÃO DE FECHAMENTO ---
btn_close = tk.Button(root, text="Fechar Aplicação", command=root.destroy)
btn_close.pack(pady=10)

# Aplica uma transformação inicial (Ex: Espelhar Horizontalmente) para mostrar um resultado
# imediatamente na inicialização.
aplicar_transposicao(Img.FLIP_LEFT_RIGHT, "Espelhar Horizontalmente")

# Inicia o loop principal do Tkinter
root.mainloop()

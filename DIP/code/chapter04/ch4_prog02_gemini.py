# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog02.py

from PIL import Image, ImageTk       # Importa classes do Pillow para manipulação de imagem
import tkinter as tk                 # Importa a biblioteca Tkinter para interface gráfica
import locale                        # Para formatação de números (separador de milhar)

# Define o locale para garantir que o separador de milhar (,) funcione corretamente
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
except locale.Error:
    # Fallback para sistemas que não possuem o locale pt_BR.utf8
    locale.setlocale(locale.LC_ALL, '') 

# --- FUNÇÃO AUXILIAR PARA CRIAR UM PAINEL (IMAGEM + DADOS COMPLETOS) ---
def criar_painel(parent_frame, imagem_pil, texto_legenda, tamanho_bytes, linhas, colunas, total_pixels):
    # Cria um Frame para agrupar a imagem e o texto
    frame = tk.Frame(parent_frame)
    frame.pack(side="left", padx=15, pady=10) # Alinha os painéis lado a lado

    # Converte o objeto Image (Pillow) para PhotoImage (Tkinter)
    photo = ImageTk.PhotoImage(imagem_pil)
    
    # Cria o Label para a Imagem
    l_img = tk.Label(frame, image=photo)
    l_img.photo = photo  # Mantém a referência
    l_img.grid(row=0, column=0) 

    # Calcula o tamanho em Megabytes para exibição
    tamanho_mb = tamanho_bytes / (1024 * 1024)
    
    # Formata números grandes com separadores de milhar
    info_bytes_formatado = locale.format_string("%d", tamanho_bytes, grouping=True)
    info_pixels_formatado = locale.format_string("%d", total_pixels, grouping=True)

    # Cria a string completa da legenda com todos os dados
    info_texto = (
        f"**{texto_legenda}**\n"
        f"Dimensões: **{linhas} Linhas x {colunas} Colunas**\n"
        f"Total de Pixels: **{info_pixels_formatado}**\n"
        f"Modo: {imagem_pil.mode} ({imagem_pil.getbands().__len__()} Canais)\n"
        f"Tamanho Total: {info_bytes_formatado} Bytes ({tamanho_mb:.2f} MB)"
    )

    # Cria o Label para a Legenda (usando justify para centralizar o texto multilinha)
    l_legenda = tk.Label(frame, text=info_texto, justify=tk.LEFT, font=("Helvetica", 10))
    l_legenda.grid(row=1, column=0, pady=5)
    
    return frame

# ---------------------------------------------------------------
# --- PRINCIPAL ---
# ---------------------------------------------------------------

# 1. Carrega a imagem e trata a exceção
try:
    im1 = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
except FileNotFoundError:
    print("Erro: Arquivo de imagem não encontrado. Usando imagem substituta.")
    im1 = Image.new('RGB', (200, 200), color=(100, 100, 100))

# 2. Realiza a Conversão de Colorspace
# 'L' (Luminance) usa 1 byte por pixel (8 bits)
res1 = im1.convert("L")

# 3. Cálculo das Dimensões e Tamanhos em Bytes
colunas, linhas = im1.size # Nota: PIL armazena (width, height)
total_pixels = colunas * linhas

# Tamanho RGB (3 bytes por pixel: R, G, B)
tamanho_rgb_bytes = total_pixels * 3

# Tamanho Luminância L (1 byte por pixel)
tamanho_l_bytes = total_pixels * 1

# 4. Configuração da Janela Tkinter
root = tk.Tk()
root.title("Colorspace Conversion Demo - Análise de Dados e Tamanho")

# 5. Criação do Frame principal para conter os painéis lado a lado
frame_display = tk.Frame(root)
frame_display.pack(side="top", pady=10)

# 6. Exibe a Imagem Original (Lado Esquerdo)
criar_painel(frame_display, im1, 
             "1. Imagem Original", 
             tamanho_rgb_bytes, linhas, colunas, total_pixels)

# 7. Exibe a Imagem Convertida (Lado Direito)
criar_painel(frame_display, res1, 
             "2. Imagem Convertida", 
             tamanho_l_bytes, linhas, colunas, total_pixels)

# 8. Adiciona um botão para fechar a aplicação
btn_close = tk.Button(root, text="Fechar Aplicação", command=root.destroy)
btn_close.pack(pady=10)

# 9. Inicia o loop principal do Tkinter
root.mainloop()

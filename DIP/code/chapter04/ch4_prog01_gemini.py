# Processamento de Imagens 2025-2
# Prof. João Miguel
# ch4_prog01.py - Com 3 Canais na 1ª Linha e Imagem Colorida na 2ª Linha

from PIL import Image, ImageTk
import tkinter as tk

# Carrega a imagem
try:
    im = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
except FileNotFoundError:
    print("Erro: Arquivo de imagem não encontrado. Usando imagem substituta.")
    im = Image.new('RGB', (100, 100), color='gray') 

root = tk.Tk()
root.title("Canais RGB (1ª Linha) e Imagem Composta (2ª Linha)")

# Divide a imagem nos canais R, G, B
r, g, b = im.split()

# --- 1. CONFIGURAÇÃO DOS DADOS ---
canais = [
    (r, "Canal Vermelho (R)"),
    (g, "Canal Verde (G)"),
    (b, "Canal Azul (B)"),
]

img_composta = Image.merge("RGB", (r, g, b))

# --- Função Auxiliar para Criar Painel de Imagem + Legenda ---
def criar_painel_imagem(parent, imagem_pil, texto_legenda):
    frame = tk.Frame(parent)
    
    # Converte a imagem para o formato Tkinter
    photo = ImageTk.PhotoImage(imagem_pil)
    
    # Cria o Label da Imagem
    l_img = tk.Label(frame, image=photo)
    l_img.photo = photo 
    l_img.grid(row=0, column=0) 

    # Cria o Label da Legenda
    l_legenda = tk.Label(frame, text=texto_legenda)
    l_legenda.grid(row=1, column=0, pady=5)
    
    return frame

# ==========================================================
## 🖼️ Primeira Linha: Canais R, G, B
# ==========================================================

# Cria um Frame que conterá apenas as três imagens de canais
frame_canais = tk.Frame(root)
# Empacota no topo da janela (será a primeira linha)
frame_canais.pack(side="top", pady=10) 

# Loop para criar e posicionar os painéis R, G, B lado a lado
for imagem_pil, legenda in canais:
    painel = criar_painel_imagem(frame_canais, imagem_pil, legenda)
    # Todos os painéis dentro do frame_canais são empacotados à esquerda
    painel.pack(side="left", padx=10)


# ==========================================================
## 📸 Segunda Linha: Imagem Colorida (Merged)
# ==========================================================

# Cria um Frame que conterá apenas a imagem colorida
frame_composta = tk.Frame(root)
# Empacota no topo (abaixo da frame_canais) e centraliza
frame_composta.pack(side="top", pady=15) 

# Cria o painel para a imagem colorida
painel_composto = criar_painel_imagem(frame_composta, img_composta, "Imagem Colorida (RGB)")

# Posiciona o painel colorido dentro de seu Frame (frame_composta)
# O .pack() aqui não precisa de side="left" pois só há um widget, ele centralizará
painel_composto.pack()


# ==========================================================
## 🚪 Botão Sair
# ==========================================================

# Cria um Frame para o botão Sair e o alinha abaixo do conteúdo
frame_sair = tk.Frame(root)
# Empacota no topo (abaixo do frame_composta)
frame_sair.pack(side="top", fill="x", pady=10)

btn = tk.Button(frame_sair, text="Sair", command=root.destroy)
# Centraliza o botão Sair no seu Frame
btn.pack(pady=5)

root.mainloop()

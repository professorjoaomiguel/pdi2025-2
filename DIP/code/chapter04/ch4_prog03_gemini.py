# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog03.py

from PIL import Image, ImageTk       # Importa classes do Pillow para manipulação de imagem (Image) e Tkinter (ImageTk)
import tkinter as tk                 # Importa a biblioteca Tkinter para interface gráfica (GUI)

# --- CONFIGURAÇÃO INICIAL E CARREGAMENTO DE IMAGENS ---

# Dimensões padrão para a imagem de fallback
FALLBACK_SIZE = (200, 200)

try:
    # Carrega as duas imagens de origem. Notas:
    # 1. Image.blend requer que as imagens tenham o mesmo tamanho e modo (ex: RGB).
    im_input_1 = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
    im_input_2 = Image.open("/home/pi/DIP/dataset/4.1.08.tiff")
    
    # Converte explicitamente ambas para 'RGB' para garantir que o modo seja idêntico, 
    # evitando erros de blend caso uma fosse 'P' ou 'L'.
    im_input_1 = im_input_1.convert("RGB")
    im_input_2 = im_input_2.convert("RGB")

except FileNotFoundError:
    print("Erro: Arquivos de imagem não encontrados. Usando imagens substitutas.")
    # Cria imagens de fallback
    im_input_1 = Image.new('RGB', FALLBACK_SIZE, color='red')
    im_input_2 = Image.new('RGB', FALLBACK_SIZE, color='blue')
except ValueError:
    # Captura erro caso as imagens não possam ser mescladas (tamanhos diferentes)
    print("Erro: Imagens têm tamanhos ou modos incompatíveis para blend.")
    im_input_1 = Image.new('RGB', FALLBACK_SIZE, color='gray')
    im_input_2 = Image.new('RGB', FALLBACK_SIZE, color='gray')


# --- FUNÇÃO DE CALLBACK PARA O WIDGET SCALE ---

def show_value_1(alpha_str):
    """
    Função chamada sempre que o valor do Scale (Alpha) é alterado.
    Realiza a mesclagem e atualiza a imagem de saída.
    """
    # Converte o valor string do scale para float
    alpha = float(alpha_str)
    
    # Imprime o valor de alpha
    print('Alpha: ', alpha)
    
    # 1. Executa a mesclagem (Blending)
    # Fórmula: output = im_input_1 * (1.0 - alpha) + im_input_2 * alpha
    img_blended = Image.blend(im_input_1, im_input_2, alpha)
    
    # 2. Atualiza o Label da Imagem Mesclada (l_output)
    photo = ImageTk.PhotoImage(img_blended)
    l_output.config(image=photo) # Atualiza a imagem no Label
    l_output.photo = photo        # Mantém a referência
    
    # Atualiza o Label de informação de Alpha
    label_alpha_info.config(text=f"Alpha (Mesclagem): {alpha:.2f}")


# ---------------------------------------------------------------
# --- CRIAÇÃO DA INTERFACE GRÁFICA (LAYOUT) ---
# ---------------------------------------------------------------

root = tk.Tk()
# Define o título da janela
root.title("Processamento de Imagens 2025-2 | Demonstração de Blending")

# --- FRAME PRINCIPAL PARA AS ENTRADAS (Topo) ---
frame_inputs = tk.Frame(root)
frame_inputs.pack(side="top", pady=10)

# 1. Imagem de Entrada 1
photo_in1 = ImageTk.PhotoImage(im_input_1)
l_in1 = tk.Label(frame_inputs, image=photo_in1)
l_in1.pack(side="left", padx=10)
l_in1.photo = photo_in1

# Legenda para Entrada 1
tk.Label(frame_inputs, text="INPUT 1 (Alpha = 0.0)", font=('Helvetica', 9)).pack(side="left")

# 2. Imagem de Entrada 2
photo_in2 = ImageTk.PhotoImage(im_input_2)
l_in2 = tk.Label(frame_inputs, image=photo_in2)
l_in2.pack(side="right", padx=10)
l_in2.photo = photo_in2

# Legenda para Entrada 2
tk.Label(frame_inputs, text="INPUT 2 (Alpha = 1.0)", font=('Helvetica', 9)).pack(side="right")

# --- FRAME DE SAÍDA E CONTROLE (Centro) ---
frame_output = tk.Frame(root)
frame_output.pack(side="top", pady=15)

# 3. Imagem de Saída (Inicialmente igual à Imagem 1, Alpha=0)
photo_out = ImageTk.PhotoImage(im_input_1)
l_output = tk.Label(frame_output, image=photo_out, text="OUTPUT")
l_output.pack()
l_output.photo = photo_out

# Label para exibir o valor de Alpha atual
label_alpha_info = tk.Label(root, text="Alpha (Mesclagem): 0.00", font=('Helvetica', 11, 'bold'))
label_alpha_info.pack(pady=5)

# 4. Widget Scale (Controle Deslizante)
# from_=0, to=1 -> Define o intervalo
# resolution=0.01 -> Permite incrementos de 1% (0.01)
# command=show_value_1 -> Liga o movimento à função que faz a mesclagem
w1 = tk.Scale(root, label="Controle de Mesclagem (Alpha)", 
              from_=0.0, to=1.0, resolution=0.01, 
              command=show_value_1, orient=tk.HORIZONTAL, length=500)
w1.set(0.0) # Define o valor inicial como 0.0
w1.pack(pady=10)

# 5. Botão de Fechar
btn_close = tk.Button(root, text="Fechar Aplicação", command=root.destroy)
btn_close.pack(pady=5)

# Inicia o loop principal do Tkinter
root.mainloop()

# Processamento de Imagens 2025-2
# Prof. João Miguel
# Imagens: https://sipi.usc.edu/database/database.php?volume=misc
# Livro: Raspberry Pi Image Processing Programming
#
# ch4_prog05.py

from PIL import Image, ImageTk       # Importa classes do Pillow para manipulação de imagem (Image) e Tkinter (ImageTk)
import tkinter as tk                 # Importa a biblioteca Tkinter para interface gráfica (GUI)

# --- VARIÁVEIS GLOBAIS ---
im_original = None    # Armazena a imagem original carregada
l_rotated = None      # Label para a imagem que será rotacionada (Resultado)
l_angle_info = None   # Label para exibir o ângulo atual
ANGLE_RANGE = 360     # Define o range máximo de rotação

# --- FUNÇÃO DE CALLBACK PARA O WIDGET SCALE ---

def show_value_1(angle_str):
    """
    Função chamada sempre que o valor do Scale (Ângulo) é alterado.
    Executa a rotação e atualiza a imagem de saída.
    """
    try:
        # Converte o valor string do scale para float
        angle = float(angle_str)
        
        # Imprime o angulo
        print('Angle: ', angle)
        
        # 1. Rotação da Imagem
        # A rotina rotate(angle) gira a imagem no sentido anti-horário (padrão).
        # expand=True faz com que a imagem de saída se expanda para caber toda a imagem rotacionada,
        # sem cortar os cantos. Isso é essencial para demonstração.
        img_rotated = im_original.rotate(angle, expand=False)
        
        # 2. Atualiza o Label da Imagem Rotacionada
        photo = ImageTk.PhotoImage(img_rotated)
        
        # Usa .config() para atualizar a imagem no Label
        l_rotated.config(image=photo) 
        l_rotated.photo = photo        # Mantém a referência
        
        # 3. Atualiza o Label de informação do Ângulo
        l_angle_info.config(text=f"Ângulo Atual: {angle:.2f} Graus")
        
    except ValueError:
        print("Erro: O valor do ângulo não é válido.")


# ---------------------------------------------------------------
# --- CRIAÇÃO DA INTERFACE GRÁFICA (LAYOUT) ---
# ---------------------------------------------------------------

# 1. Configuração da Janela Tkinter
root = tk.Tk()
root.title(f"Processamento de Imagens 2025-2 | Demonstração de Rotação ({ANGLE_RANGE}°)")

# 2. Carregamento da Imagem Original
try:
    im_original = Image.open("/home/pi/DIP/dataset/4.1.07.tiff")
except FileNotFoundError:
    print("Erro: Imagem não encontrada. Usando substituta.")
    im_original = Image.new('RGB', (256, 256), color='gray')


# --- LAYOUT DE COMPARAÇÃO (ORIGINAL vs. ROTACIONADA) ---

# Frame principal para conter os displays (lado a lado)
frame_display = tk.Frame(root)
frame_display.pack(side="top", pady=10)

# Frame para controles e feedback
frame_control = tk.Frame(root)
frame_control.pack(side="top", pady=5)


# --- Lado Esquerdo: Imagem Original (Referência) ---
photo_original = ImageTk.PhotoImage(im_original)
l_original = tk.Label(frame_display, image=photo_original)
l_original.pack(side="left", padx=20)
l_original.photo = photo_original

# Legenda da Original
tk.Label(frame_display, text="Original", font=('Helvetica', 10, 'bold')).pack(side="left", anchor="n")


# --- Lado Direito: Imagem Rotacionada (Resultado) ---
# Inicializa a imagem rotacionada com 0 graus
initial_img_rotated = im_original.rotate(0, expand=False) 
photo_rotated = ImageTk.PhotoImage(initial_img_rotated)

l_rotated = tk.Label(frame_display, image=photo_rotated)
l_rotated.pack(side="right", padx=20)
l_rotated.photo = photo_rotated

# Legenda da Rotacionada
tk.Label(frame_display, text="Rotacionada", font=('Helvetica', 10, 'bold')).pack(side="right", anchor="n")


# --- FEEDBACK E CONTROLE ---

# Label para exibir o valor de Alpha atual
l_angle_info = tk.Label(frame_control, text="Ângulo Atual: 0.00 Graus", font=('Helvetica', 11, 'bold'))
l_angle_info.pack(pady=5)

# Cria o Widget Scale para variar o ângulo
w1 = tk.Scale(frame_control, label=f"Controle de Rotação (0° a {ANGLE_RANGE}°)", 
              from_=0, to=ANGLE_RANGE, resolution=1, 
              command=show_value_1, orient=tk.HORIZONTAL, length=500)
w1.set(0) # Define o valor inicial como 0
w1.pack(pady=10)


# --- BOTÃO DE FECHAMENTO ---
btn_close = tk.Button(root, text="Fechar Aplicação", command=root.destroy)
btn_close.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()

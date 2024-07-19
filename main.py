import tkinter as tk
from PIL import Image, ImageTk

def load_images():
    """Carrega e processa as imagens."""
    # Carrega e redimensiona a primeira imagem
    image1 = Image.open("mario.jpg")  # Atualize o caminho para a sua imagem
    image1 = image1.resize((120, 120))
    photo1 = ImageTk.PhotoImage(image1)
    
    # Carrega e redimensiona a segunda imagem
    image2 = Image.open("kingdomrush.jpg")  # Atualize o caminho para a sua imagem
    image2 = image2.resize((120, 120))
    photo2 = ImageTk.PhotoImage(image2)
    
    # Carrega e redimensiona a terceira imagem
    image3 = Image.open("exemplo.png")  # Atualize o caminho para a sua imagem
    image3 = image3.resize((120, 120))
    photo3 = ImageTk.PhotoImage(image3)

    return photo1, photo2, photo3

# Cria a janela principal
root = tk.Tk()
root.title("Aplicativo de Jogos")
root.geometry("300x300")  # Ajuste o tamanho da janela se necessário
root.resizable(False,False)
# Carrega as imagens
image1, image2, image3 = load_images()

# Cria o Frame principal
frame = tk.Frame(root, background="lightgrey")
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Cria o Canvas
canvas = tk.Canvas(frame, background="lightgrey")
canvas.grid(row=0, column=0, sticky="nsew")

# Adiciona a scrollbar horizontal
scroll_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

# Cria um Frame interno para os widgets e adiciona ao Canvas
frame_internal = tk.Frame(canvas, background="lightgrey")
frame_internal.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Adiciona o Frame interno ao Canvas
canvas.create_window((0, 0), window=frame_internal, anchor="nw")
canvas.configure(xscrollcommand=scroll_x.set)

# Adiciona widgets ao Frame interno
label_titulo = tk.Label(frame_internal, text="Jogos em Destaque", compound="top", background="#fff0b8", font=("Arial", 10))
label_titulo.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky="nw")

# Jogo 1
label1 = tk.Label(frame_internal, text="Super Mario Bros.", image=image1, compound="top", font=("Arial", 10))
label1.grid(row=1, column=0, padx=5, pady=5)

button_favoritos1 = tk.Button(frame_internal, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos1.grid(row=2, column=0, padx=5, pady=5)

button_download = tk.Button(frame_internal, text="Download", font=("Arial", 7))
button_download.grid(row=4, column=0, padx=5, pady=5)

# Jogo 2
label2 = tk.Label(frame_internal, text="Kingdom Rush", image=image2, compound="top", font=("Arial", 10))
label2.grid(row=1, column=1, padx=5, pady=5)

button_favoritos2 = tk.Button(frame_internal, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos2.grid(row=2, column=1, padx=5, pady=5)

button_download2 = tk.Button(frame_internal, text="Download", font=("Arial", 7))
button_download2.grid(row=4, column=0, padx=5, pady=5)
# Jogo 3
label3 = tk.Label(frame_internal, text="Jogo 3", image=image3, compound="top", font=("Arial", 10))
label3.grid(row=1, column=2, padx=5, pady=5)

button_favoritos3 = tk.Button(frame_internal, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos3.grid(row=2, column=2, padx=5, pady=5)

button_download3 = tk.Button(frame_internal, text="Download", font=("Arial", 7))
button_download3.grid(row=4, column=0, padx=5, pady=5)

# Configura o layout do grid interno
frame_internal.grid_rowconfigure(1, weight=1)
frame_internal.grid_rowconfigure(2, weight=0)
frame_internal.grid_columnconfigure(0, weight=1)
frame_internal.grid_columnconfigure(1, weight=1)
frame_internal.grid_columnconfigure(2, weight=1)

# Configura o layout do Frame principal
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=0)
frame.grid_columnconfigure(0, weight=1)

# Executa o loop principal do tkinter
root.mainloop()

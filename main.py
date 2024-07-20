import tkinter as tk
from PIL import Image, ImageTk

def load_images():
    image1 = Image.open("mario.jpg")
    image1 = image1.resize((120, 120))
    photo1 = ImageTk.PhotoImage(image1)
    
    image2 = Image.open("kingdomrush.jpg")
    image2 = image2.resize((120, 120))
    photo2 = ImageTk.PhotoImage(image2)
    
    image3 = Image.open("csgo.webp")
    image3 = image3.resize((120, 120))
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("bloons.jpg")
    image4 = image4.resize((120, 120))
    photo4 = ImageTk.PhotoImage(image4)
    
    image5 = Image.open("pacman.jpg")
    image5 = image5.resize((120, 120))
    photo5 = ImageTk.PhotoImage(image5)
    
    image6 = Image.open("donkeykong.webp")
    image6 = image6.resize((120, 120))
    photo6 = ImageTk.PhotoImage(image6)
    
    image7 = Image.open("tetris.jpg")
    image7 = image7.resize((120, 120))
    photo7 = ImageTk.PhotoImage(image7)

    image8 = Image.open("contra.webp")
    image8 = image8.resize((120, 120))
    photo8 = ImageTk.PhotoImage(image8)

    return photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8

# Cria a janela principal
root = tk.Tk()
root.title("Aplicativo de Jogos")
root.geometry("700x600")
root.resizable(False, False)

# Carrega as imagens
image1, image2, image3, image4, image5, image6, image7, image8 = load_images()

# Cria o Frame principal
frame = tk.Frame(root, background="lightgrey")
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Cria o Canvas
canvas = tk.Canvas(frame, background="#333e50")
canvas.grid(row=0, column=0, sticky="nsew")


scroll_x = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")


scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")


frame_principal = tk.Frame(canvas, background="#333e50")
frame_principal.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame_principal, anchor="nw")
canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)



# Título de Jogos em Destaque
label_titulo_destaques = tk.Label(frame_principal, text="Jogos em Destaque", compound="top", background="#fff0b8", font=("Arial", 10))
label_titulo_destaques.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="nw")

# Frame para os jogos em destaque
frame_destaques = tk.Frame(frame_principal, background="#5c6e6e")
frame_destaques.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Jogo 1
label1 = tk.Label(frame_destaques, text="Super Mario Bros.", image=image1, compound="top", font=("Arial", 10))
label1.grid(row=0, column=0, padx=5, pady=5)

button_favoritos1 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos1.grid(row=1, column=0, padx=5, pady=5)

button_download1 = tk.Button(frame_destaques, text="Download", font=("Arial", 7))
button_download1.grid(row=2, column=0, padx=5, pady=5)

# Jogo 2
label2 = tk.Label(frame_destaques, text="Kingdom Rush", image=image2, compound="top", font=("Arial", 10))
label2.grid(row=0, column=1, padx=5, pady=5)

button_favoritos2 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos2.grid(row=1, column=1, padx=5, pady=5)

button_download2 = tk.Button(frame_destaques, text="Download", font=("Arial", 7))
button_download2.grid(row=2, column=1, padx=5, pady=5)

# Jogo 3
label3 = tk.Label(frame_destaques, text="CS:GO", image=image3, compound="top", font=("Arial", 10))
label3.grid(row=0, column=2, padx=5, pady=5)

button_favoritos3 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos3.grid(row=1, column=2, padx=5, pady=5)

button_download3 = tk.Button(frame_destaques, text="Download", font=("Arial", 7))
button_download3.grid(row=2, column=2, padx=5, pady=5)

# Bloons TD 6
label4 = tk.Label(frame_destaques, text="Bloons TD 6", image=image4, compound="top", font=("Arial", 10))
label4.grid(row=0, column=3, padx=5, pady=5)

button_favoritos4 = tk.Button(frame_destaques, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos4.grid(row=1, column=3, padx=5, pady=5)

button_download4 = tk.Button(frame_destaques, text="Download", font=("Arial", 7))
button_download4.grid(row=2, column=3, padx=5, pady=5)

# Adiciona o título para a nova seção de Jogos de Plataforma
label_titulo_plataforma = tk.Label(frame_principal, text="Jogos de Plataforma", compound="top", background="#fff0b8", font=("Arial", 10))
label_titulo_plataforma.grid(row=2, column=0, padx=5, pady=5, columnspan=4, sticky="nw")

# Frame para os jogos de plataforma
frame_plataforma = tk.Frame(frame_principal, background="#5c6e6e")
frame_plataforma.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Pacman
label5 = tk.Label(frame_plataforma, text="Pacman", image=image5, compound="top", font=("Arial", 10))
label5.grid(row=0, column=0, padx=5, pady=5)

button_favoritos5 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos5.grid(row=1, column=0, padx=5, pady=5)

button_download5 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7))
button_download5.grid(row=2, column=0, padx=5, pady=5)

# Donkey Kong
label6 = tk.Label(frame_plataforma, text="Donkey Kong", image=image6, compound="top", font=("Arial", 10))
label6.grid(row=0, column=1, padx=5, pady=5)

button_favoritos6 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos6.grid(row=1, column=1, padx=5, pady=5)

button_download6 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7))
button_download6.grid(row=2, column=1, padx=5, pady=5)

# Tetris
label7 = tk.Label(frame_plataforma, text="Tetris", image=image7, compound="top", font=("Arial", 10))
label7.grid(row=0, column=2, padx=5, pady=5)

button_favoritos7 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos7.grid(row=1, column=2, padx=5, pady=5)

button_download7 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7))
button_download7.grid(row=2, column=2, padx=5, pady=5)

# Contra
label8 = tk.Label(frame_plataforma, text="Contra", image=image8, compound="top", font=("Arial", 10))
label8.grid(row=0, column=3, padx=5, pady=5)

button_favoritos8 = tk.Button(frame_plataforma, text="Adicionar aos Favoritos", font=("Arial", 7))
button_favoritos8.grid(row=1, column=3, padx=5, pady=5)

button_download8 = tk.Button(frame_plataforma, text="Download", font=("Arial", 7))
button_download8.grid(row=2, column=3, padx=5, pady=5)

# Configura o layout do grid interno
frame_destaques.grid_rowconfigure(0, weight=1)
frame_destaques.grid_rowconfigure(1, weight=0)
frame_destaques.grid_rowconfigure(2, weight=0)
frame_destaques.grid_columnconfigure(0, weight=1)
frame_destaques.grid_columnconfigure(1, weight=1)
frame_destaques.grid_columnconfigure(2, weight=1)
frame_destaques.grid_columnconfigure(3, weight=1)

frame_plataforma.grid_rowconfigure(0, weight=1)
frame_plataforma.grid_rowconfigure(1, weight=0)
frame_plataforma.grid_rowconfigure(2, weight=0)
frame_plataforma.grid_columnconfigure(0, weight=1)
frame_plataforma.grid_columnconfigure(1, weight=1)
frame_plataforma.grid_columnconfigure(2, weight=1)
frame_plataforma.grid_columnconfigure(3, weight=1)

# Configura o layout do Frame principal
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=0)
frame_principal.grid_rowconfigure(2, weight=0)
frame_principal.grid_rowconfigure(3, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2, weight=1)
frame_principal.grid_columnconfigure(3, weight=1)

# Ajusta as proporções do Canvas e do Frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Executa o loop principal do tkinter
root.mainloop()

import chess
import chess.engine
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import threading
import time
from tkinter import ttk
from detect_os import detect_operating_system

def stockfish_engine():
    os = detect_operating_system
    if os == "Windows":
        stockfish_path = ".\\bin\\stockfish.exe"
    else:
        stockfish_path = "./bin/stockfish"

    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    return engine

def chess_images():
    os = detect_operating_system
    if os == "Windows":
        chess_images_path = ".\\assets\\pieces\\"
    else:
        chess_images_path = "./assets/pieces/"

    return chess_images_path

# Tamanho inicial do tabuleiro
board_size = 450

# Tamanho original da janela
original_window_size = (board_size, board_size)

# Tempo limite de pensamento inicial da máquina
time_limit = 1

# Variável para controlar o modo de jogo (jogador vs. máquina ou automático)
auto_mode = False

# Variável global para o tabuleiro
board = chess.Board()

# Posição inicial do tabuleiro
initial_fen = board.fen()

# Histórico de movimentos
move_history = []

engine = stockfish_engine()

# Função para obter a melhor jogada do Stockfish
def get_best_move(board, time_limit):
    result = engine.play(board, chess.engine.Limit(time=float(time_limit)))
    return result.move

# Função para criar uma imagem do tabuleiro de xadrez com peças
def create_chessboard_image(board, size):
    square_size = size // 8  # Tamanho de cada quadrado do tabuleiro
    image = Image.new("RGB", (size, size))
    images_path = chess_images()

    for rank in range(8):
        for file in range(8):
            square_color = "black" if (rank + file) % 2 == 0 else "white"
            draw = ImageDraw.Draw(image)
            draw.rectangle(
                [(file * square_size, rank * square_size),
                 ((file + 1) * square_size, (rank + 1) * square_size)],
                fill=square_color)

            piece = board.piece_at(chess.square(file, 7 - rank))
            if piece is not None:
                piece_image = Image.open(f"{images_path}{piece.symbol()}_{'white' if piece.color == chess.WHITE else 'black'}.png")
                piece_image = piece_image.resize((square_size, square_size))
                image.paste(piece_image, (file * square_size, rank * square_size))

    return image

# Função para atualizar a exibição do tabuleiro
def update_board(size):
    global chessboard_image
    chessboard_image = create_chessboard_image(board, size)
    photo = ImageTk.PhotoImage(chessboard_image)

    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

# Função para definir o tamanho da tela
def set_board_size(size):
    global board_size, original_window_size
    board_size = size
    canvas.config(width=board_size, height=board_size)
    original_window_size = (board_size, board_size)  # Atualiza o tamanho original da janela
    update_board(board_size)

# Função para restaurar o tabuleiro para a posição inicial
def restore_board():
    global board
    board = chess.Board(initial_fen)
    update_board(board_size)

# Função para sair do jogo
def quit_game():
    engine.quit()
    root.destroy()

# Função para adicionar um movimento ao histórico
def add_to_move_history(move):
    move_history.append(move)

# Função para mostrar o histórico de movimentos em uma caixa de texto
def show_move_history():
    history_window = tk.Toplevel(root)
    history_window.title("Histórico de Movimentos")

    text = tk.Text(history_window)
    text.pack()

    for i, move in enumerate(move_history, start=1):
        text.insert(tk.END, f"{i}. {move}\n")

# Função para enviar a jogada do jogador
def submit_player_move():
    move = player_move_entry.get()
    if move.lower() == "quit":
        quit_game()  # Adicione uma opção para sair do jogo
    try:
        board.push_san(move)
        add_to_move_history(move)  # Adicione o movimento ao histórico
    except ValueError:
        print("Movimento inválido. Tente novamente.")
    update_board(board_size)
    if not board.is_game_over():
        make_computer_move()

# Função para fazer a jogada da máquina
def make_computer_move():
    best_move = get_best_move(board, time_limit)  # Define o limite de tempo para a análise
    print("Melhor jogada do Stockfish:", best_move.uci())
    board.push(best_move)
    add_to_move_history(best_move.uci())  # Adicione a jogada da máquina ao histórico
    update_board(board_size)

# Função para aumentar o tempo limite
def increase_time_limit():
    global time_limit
    time_limit += 1  # Aumente o tempo em 1 segundo
    update_time_label()

# Função para diminuir o tempo limite
def decrease_time_limit():
    global time_limit
    if time_limit > 1:  # Certifique-se de que o tempo não seja menor que 1 segundo
        time_limit -= 1  # Diminua o tempo em 1 segundo
        update_time_label()

# Função para atualizar o rótulo de tempo com o valor atual
def update_time_label():
    time_label.config(text=f"Tempo Limite da Máquina: {time_limit} segundos")

# Função para alternar entre os modos de jogo (Jogador vs. Máquina e Automático)
def toggle_auto_mode():
    global auto_mode
    auto_mode = not auto_mode
    if auto_mode:
        auto_mode_button.config(text="Parar Modo Automático")
        play_auto_game_thread = threading.Thread(target=play_auto_game)
        play_auto_game_thread.start()
    else:
        auto_mode_button.config(text="Jogar Sozinho")

# Função para jogar automaticamente (usando Stockfish)
def play_auto_game():
    while not board.is_game_over() and auto_mode:
        make_computer_move()
        root.update_idletasks()  # Atualize a interface gráfica para que a janela seja responsiva
        time.sleep(1)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Xadrez com Stockfish")

canvas = tk.Canvas(root, width=board_size, height=board_size)
canvas.pack()

update_board(board_size)

# Caixa de entrada para a jogada do jogador
player_move_entry = tk.Entry(root)
player_move_entry.pack()

# Botão para enviar a jogada do jogador
submit_button = ttk.Button(root, text="Enviar Jogada", command=submit_player_move)
submit_button.pack()

# Criação do menu de opções
menu = tk.Menu(root)
root.config(menu=menu)

# Menu Tamanho da Tela
size_menu = tk.Menu(menu)
menu.add_cascade(label="Tamanho da Tela", menu=size_menu)
size_menu.add_command(label="Pequeno", command=lambda: set_board_size(400))
size_menu.add_command(label="Médio", command=lambda: set_board_size(600))
size_menu.add_command(label="Grande", command=lambda: set_board_size(800))
size_menu.add_separator()

# Opção para restaurar o tabuleiro
menu.add_command(label="Reiniciar partida", command=restore_board)

# Menu Histórico de Movimentos
menu.add_command(label="Histórico de Movimentos", command=show_move_history)

# Menu Sair do Jogo
menu.add_command(label="Sair do Jogo", command=quit_game)

# Botões para aumentar e diminuir o tempo limite
increase_time_button = ttk.Button(root, text="Aumentar Tempo", command=increase_time_limit)
increase_time_button.pack()
decrease_time_button = ttk.Button(root, text="Diminuir Tempo", command=decrease_time_limit)
decrease_time_button.pack()

# Rótulo para exibir o tempo atual
time_label = ttk.Label(root, text=f"Tempo Limite da Máquina: {time_limit} segundos")
time_label.pack()

# Botão para alternar entre os modos de jogo (Jogador vs. Máquina e Automático)
auto_mode_button = ttk.Button(root, text="Jogar Sozinho", command=toggle_auto_mode)
auto_mode_button.pack()

print("Tempo limite da máquina:", time_limit)

root.mainloop()

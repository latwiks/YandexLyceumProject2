import pygame
import sys
import random
from moviepy.editor import *

clip = VideoFileClip("./videos/2.mp4")
# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 300, 300
CELL_SIZE = WIDTH // 3

# Цвета
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Игровое поле
board = [[''] * 3 for _ in range(3)]


# Отрисовка сетки
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)


# Отрисовка крестика или нолика
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text_surface = font.render(symbol, True, LINE_COLOR)
    screen.blit(text_surface, (col * CELL_SIZE + 20, row * CELL_SIZE + 20))


# Проверка на победу
def check_winner(symbol):
    for row in range(3):
        if all(board[row][col] == symbol for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def check_draw():
    return all(all(cell != '' for cell in row) for row in board)


# Главный цикл игры
player_turn = True
player_symbol = 'X'
computer_symbol = 'O'
player_score = 0
computer_score = 0
a = True
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] == '':
                board[row][col] = player_symbol
                if check_winner(player_symbol):
                    player_score += 1
                    print(f"Игрок выиграл! Счёт: Игрок {player_score} - Компьютер {computer_score}")
                    board = [[''] * 3 for _ in range(3)]
                player_turn = False

    if player_score == 3 and computer_score < 3:
        a = False
        clip.preview()
        import rock_paper_scissors as f
        f()

    if not player_turn:
        # Computer's turn (random move)
        empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            board[row][col] = computer_symbol
            if check_winner(computer_symbol):
                computer_score += 1
                print(f"Компьютер выиграл! Счёт: Игрок {player_score} - Компьютер {computer_score}")
                board = [[''] * 3 for _ in range(3)]
            elif check_draw():
                print("Ничья!")
                board = [[''] * 3 for _ in range(3)]
            player_turn = True

    screen.fill(WHITE)
    draw_grid()

    # Отрисовка символов на доске
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                draw_symbol(row, col, board[row][col])

    pygame.display.flip()

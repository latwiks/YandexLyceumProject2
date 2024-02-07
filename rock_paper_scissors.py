import pygame
import sys
import random
from moviepy.editor import *

clip = VideoFileClip("./videos/3.mp4")
# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 300

# Цвета
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень-ножницы-бумага")

# Счет
player_score = 0
computer_score = 0


# Отрисовка текста
def draw_text(text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, LINE_COLOR)
    screen.blit(text_surface, (x, y))


a = True
# Главный цикл игры
while a:
    if player_score == 3 and computer_score < 3:
        clip.preview()
        a = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Игрок выбирает камень (1)
                player_choice = "камень"
            elif event.key == pygame.K_2:
                # Игрок выбирает ножницы (2)
                player_choice = "ножницы"
            elif event.key == pygame.K_3:
                # Игрок выбирает бумагу (3)
                player_choice = "бумага"

                # Выбор компьютера
            computer_choice = random.choice(["камень", "ножницы", "бумага"])

            # Определение победителя
            if player_choice == computer_choice:
                result = "Ничья"
            elif (player_choice == "камень" and computer_choice == "ножницы") or \
                    (player_choice == "ножницы" and computer_choice == "бумага") or \
                    (player_choice == "бумага" and computer_choice == "камень"):
                result = "Вы победили!"
                player_score += 1
            else:
                result = "Компьютер победил!"
                computer_score += 1

            print(
                f"Игрок: {player_choice}, Компьютер: {computer_choice} - {result} (Счет: Игрок {player_score} - Компьютер {computer_score})")

    screen.fill(WHITE)
    draw_text("Выберите: камень (1), ножницы (2), бумага (3)", 20, 20, 20)

    pygame.display.flip()

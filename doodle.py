# импортируем модули
import random
import subprocess
import sys
from sprite_functions.Enemy import Enemy
from sprites import *
from sprite_functions.Player import Player
from sprite_functions.Block import Block
from sprite_groups import *
import pygame
from moviepy.editor import *

clip = VideoFileClip('videos/1.mp4')
# инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# создаем объект игрока
player = Player(400, 300)
all_sprites.add(player)
players.add(player)

# создаем первый блок в центре экрана
first_block = Block(400, 500, 'normal')
all_sprites.add(first_block)
blocks.add(first_block)

# ставим игрока на первый блок
player.rect.bottom = first_block.rect.top

# создаем остальные блоки
last_y = first_block.rect.y
for i in range(10):
    # выбираем случайную координату по x
    x = random.randint(0, 700)
    # выбираем высоту блока так, чтобы он был на расстоянии прыжка от предыдущего
    y = random.randint(0, 600)
    # выбираем тип блока с заданными вероятностями
    p = random.random()
    if p < 0.3:
        type = 'go'
    elif p < 0.5:
        type = 'fallen'
    else:
        type = 'normal'
    block = Block(x, y, type)
    all_sprites.add(block)
    blocks.add(block)
    # обновляем высоту последнего блока
    last_y = y

# создаем переменные для игрового цикла
running = True  # флаг работы игры
clock = pygame.time.Clock()  # таймер
font = pygame.font.SysFont('Arial', 32)  # шрифт для текста
# создаем список для хранения нажатых клавиш
keys = []
# создаем читкод
cheat = [pygame.K_b, pygame.K_o, pygame.K_s, pygame.K_s]
# запускаем игровой цикл
while running:
    # обрабатываем события
    for event in pygame.event.get():
        # если нажата кнопка закрытия окна, то выходим из игры
        if event.type == pygame.QUIT:
            running = False
        # если нажата клавиша, то меняем скорость игрока по горизонтали
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vx = -10
            if event.key == pygame.K_RIGHT:
                player.vx = 10
            # если нажата клавиша пробела, то устанавливаем флаг стрельбы
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                player.shoot = True
                pygame.mixer.music.load("sounds/shoot.mp3")
                pygame.mixer.music.play(0)
            keys.append(event.key)
            # если список содержит четыре клавиши, то проверяем, совпадает ли он с читкодом
            if len(keys) == 4:
                if keys == cheat:
                    # если да, то увеличиваем счет на 1000000
                    player.score += 1000000
                # удаляем первый элемент списка
                keys.pop(0)
        # если отпущена клавиша, то обнуляем скорость игрока по горизонтали
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.vx = 0

    # обновляем спрайты
    all_sprites.update()

    # проверяем столкновения игрока с врагами
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        # если игрок коснулся врага, то игра заканчивается
        running = False

    # проверяем высоту игрока
    if player.rect.top < 200:
        # если игрок поднялся выше 200 пикселей, то опускаем все спрайты вниз
        player.rect.y += abs(player.vy)
        for block in blocks:
            block.rect.y += abs(player.vy)
        for enemy in enemies:
            enemy.rect.y += abs(player.vy)
        # создаем новые блоки сверху
        while len(blocks) < 100:
            # выбираем случайную координату по x
            x = random.randint(0, 700)
            # выбираем высоту блока так, чтобы он был на расстоянии прыжка от предыдущего
            y = last_y - random.randint(0, 100) if blocks.sprites()[
                                                       -1].get_type() != "fallen" else last_y - random.randint(0, 10)
            # выбираем тип блока с заданными вероятностями
            p = random.random()
            if p < 0.1:
                type = 'go'
            elif p < 0.2:
                type = 'fallen'
            else:
                type = 'normal'
            block = Block(x, y, type)
            all_sprites.add(block)
            blocks.add(block)
            # обновляем высоту последнего блока
            last_y = y
        # создаем новых врагов сверху с некоторой вероятностью
        if random.random() < 0.01:
            x = random.randint(0, 800)
            y = random.randint(-50, 0)
            enemy = Enemy(x, y)
            all_sprites.add(enemy)
            enemies.add(enemy)

    # рисуем фон
    screen.blit(bg, (0, 0))

    # рисуем спрайты
    all_sprites.draw(screen)

    # рисуем счет
    score_text = font.render('Score: ' + str(player.score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # обновляем экран
    pygame.display.flip()

    # задаем частоту кадров
    clock.tick(60)
    if player.rect.bottom > 600:
        # если игрок вышел за нижнюю границу экрана, то игра заканчивается
        running = False
    if player.score >= 100:
        running = False
        clip.preview()
        import tic_tac_toe as f
        f()

with open("high_score.txt", "r") as f:
    high_score = f.read()
    high_score_int = int(high_score)
with open("high_score.txt", "w") as f:
    if high_score_int < player.score:
        f.write(str(player.score))
    else:
        f.write(high_score)

# выходим из pygame
pygame.quit()
sys.exit()

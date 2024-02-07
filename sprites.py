import pygame

# загружаем спрайты
bg = pygame.image.load('images/bg.jpg')
enemy_image = pygame.image.load('images/enemy.png')
# создаем переменные для спрайтов дудлика
right_doodle = pygame.image.load('images/doodle1.png')
# отзеркаливаем правый спрайт дудлика, чтобы получить левый
left_doodle = pygame.transform.flip(right_doodle, True, False)
jump_doodle = pygame.image.load('images/doodle2.png')
normal_block = pygame.image.load('images/normal_block.png')
fallen_block = pygame.image.load('images/fallen_block.png')
go_block = pygame.image.load('images/go_block.png')
# создаем переменные для спрайтов патрона и стреляющего дудлика
bullet_image = pygame.image.load('images/bullet.png')
punch_doodle = pygame.image.load('images/punch_doodle.png')

# изменяем размеры спрайтов
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
# учитываем разные размеры спрайтов дудлика
right_doodle = pygame.transform.scale(right_doodle, (50, 50))
bg = pygame.transform.scale(bg, (800, 600))
left_doodle = pygame.transform.scale(left_doodle, (50, 50))
jump_doodle = pygame.transform.scale(jump_doodle, (50, 50))
normal_block = pygame.transform.scale(normal_block, (100, 20))
fallen_block = pygame.transform.scale(fallen_block, (100, 20))
go_block = pygame.transform.scale(go_block, (100, 20))
# изменяем размеры спрайтов патрона и стреляющего дудлика
bullet_image = pygame.transform.scale(bullet_image, (20, 20))
punch_doodle = pygame.transform.scale(punch_doodle, (50, 60))

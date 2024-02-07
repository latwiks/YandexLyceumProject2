from sprite_functions.Bullet import Bullet
from sprite_groups import all_sprites, bullets, blocks
from sprites import *

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # выбираем начальный спрайт дудлика
        self.image = right_doodle
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = 0  # скорость по горизонтали
        self.vy = 0  # скорость по вертикали
        self.jump = False  # флаг прыжка
        self.score = 0  # счет игрока
        self.shoot = False  # флаг стрельбы
        self.timer = 0  # таймер для возврата к исходному спрайту

    def update(self):
        # обновляем позицию игрока
        self.rect.x += self.vx
        self.rect.y += self.vy
        # проверяем границы экрана
        if self.rect.left < 0:
            self.rect.right = 800
        if self.rect.right > 800:
            self.rect.left = 0
        # проверяем столкновения с блоками
        hits = pygame.sprite.spritecollide(self, blocks, False)
        if hits:
            # если игрок стоит на блоке, то он может прыгать
            if self.rect.bottom <= hits[0].rect.bottom:
                self.jump = True
                pygame.mixer.music.load("sounds/jump.mp3")
                pygame.mixer.music.play(0)
                self.vy = -15  # задаем начальную скорость прыжка
                # увеличиваем счет в зависимости от типа блока
                if hits[0].type == 'normal':
                    self.score += 1
                elif hits[0].type == 'fallen':
                    self.score += 2
                elif hits[0].type == 'go':
                    self.score += 3
            # если игрок ударяется о блок снизу, то он теряет скорость
            elif self.rect.top >= hits[0].rect.top:
                self.vy += 0.5
        else:
            # если игрок не касается блоков, то он падает под действием гравитации
            self.jump = False
            self.vy += 0.5
        # проверяем, не упал ли игрок за нижнюю границу экрана
        if self.rect.top > 600:
            # если да, то игра заканчивается
            global running
            running = False
        # меняем спрайт дудлика в зависимости от направления движения, прыжка и стрельбы
        if self.shoot:
            self.image = punch_doodle
            # создаем патрон
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            # запускаем таймер для возврата к исходному спрайту
            self.timer = pygame.time.get_ticks()
            # сбрасываем флаг стрельбы
            self.shoot = False
        elif self.jump:
            self.image = jump_doodle
        elif self.vx < 0:
            self.image = left_doodle
        elif self.vx > 0:
            self.image = right_doodle
        # если прошло 200 мс с момента стрельбы, то возвращаемся к исходному спрайту
        if pygame.time.get_ticks() - self.timer > 200:
            self.timer = 0
            if self.jump:
                self.image = jump_doodle
            elif self.vx < 0:
                self.image = left_doodle
            elif self.vx > 0:
                self.image = right_doodle
        # обновляем прямоугольник дудлика
        self.rect = self.image.get_rect(center=self.rect.center)

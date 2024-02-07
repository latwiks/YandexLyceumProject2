import pygame
from sprite_groups import enemies
from sprites import bullet_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vy = -10  # скорость по вертикали

    def update(self):
        # обновляем позицию патрона
        self.rect.y += self.vy
        # если патрон вышел за границы экрана, то удаляем его
        if self.rect.bottom < -100:
            self.kill()
        # проверяем столкновения патрона с врагами
        hits = pygame.sprite.spritecollide(self, enemies, True)
        if hits:
            # если патрон попал в врага, то удаляем его
            self.kill()

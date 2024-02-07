import pygame

from sprites import enemy_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = 0  # скорость по горизонтали
        self.vy = 0  # скорость по вертикали

    def update(self):
        # обновляем позицию врага
        self.rect.x += self.vx
        self.rect.y += self.vy
        # если враг вышел за границы экрана, то удаляем его
        if self.rect.top > 600:
            self.kill()

import math
import pygame
from sprite_groups import players
from sprites import normal_block, fallen_block, go_block


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type  # тип блока: normal, fallen или go
        # загружаем соответствующий спрайт
        if self.type == 'normal':
            self.image = normal_block
        elif self.type == 'fallen':
            self.image = fallen_block
        elif self.type == 'go':
            self.image = go_block
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vx = 0  # скорость по горизонтали
        self.vy = 0  # скорость по вертикали

    def update(self):
        # обновляем позицию блока
        self.rect.x += self.vx
        self.rect.y += self.vy
        # если блок вышел за границы экрана, то удаляем его
        if self.rect.top > 600:
            self.kill()
        # если блок сваливающийся, то он падает после касания игроком
        if self.type == 'fallen':
            hits = pygame.sprite.spritecollide(self, players, False)
            if hits:
                self.vy = 5
        # если блок подвижный, то он движется по горизонтали
        if self.type == 'go':
            self.vx = math.sin(pygame.time.get_ticks() / 1000) * 5

    def get_type(self):
        return self.type

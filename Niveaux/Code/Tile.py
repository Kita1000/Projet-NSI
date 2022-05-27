import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
        super().__init__(size,x,y)
        self.image = surface

class Obstacles(StaticTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,surface)


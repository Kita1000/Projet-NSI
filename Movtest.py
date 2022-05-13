import pygame

pygame.init()

# Creation de la classe joueur (permet de faciliter son implantation pour les differents niveau)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Pour ne pas avoir d'erreur
        super.__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('grey')
        # On affiche "l'image" sur le rectangle
        self.rect = self.image.get_rect(topleft = pos)
        self.pressed_r = False
        self.pressed_l = False
        self.forw_maxspeed = 10
        self.back_maxspeed = -self.forw_maxspeed
        self.accel_x = 0.5
        self.x_speed = 0
        self.x = 0
        self.y = 0

    # Getting da input
    def movement(self):
        keys_pre = pygame.key.get_pressed()

        if keys_pre[pygame.K_RIGHT]:
            # vitesse instantanée
            self.x_speed += 0.5
            if self.x_speed >= self.forw_maxspeed:
                self.x_speed = self.forw_maxspeed
                self.x += self.x_speed
            else:
                self.x_speed += self.accel_x

        if keys_pre[pygame.K_LEFT]:
            # vitesse instantanée
            # vitesse instantanée
            self.x_speed += 0.5
            if self.x_speed >= self.back_maxspeed:
                self.x_speed = self.back_maxspeed
                self.x += self.x_speed
            else:
                self.x_speed = - self.accel_x

        if not keys_pre[pygame.K_RIGHT]:
            # decelerate
            while self.x_speed > 0:
                self.x_speed = self.x_speed * 0.98
            self.x_speed = 0

        if not keys_pre[pygame.K_RIGHT]:
            # decelerate
            if self.x_speed > 0:
                self.x_speed = self.x_speed * 0.98
            else:
                self.x_speed = 0

    def update(self):
        self.movement()
        self.rect.x += self.x_speed






import pygame, os
from Niveaux.Code.level_settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_player_images()
        self.frame_index = 0
        self.animation_speed = 0.55
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 15
        self.gravity = 0.8
        self.jump_speed = -15

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_player_images(self):
        idle = []
        files_in_idle = next(os.walk("Player_images/idle"))[2]
        for i in range(1, len(files_in_idle)):
            idle.append(
                pygame.transform.scale(pygame.image.load(os.path.join('Player_images/idle', '' + str(i) + '.png')),
                                       (player_w_lvl, player_h_lvl)))

        run = []
        files_in_run = next(os.walk("Player_images/run"))[2]
        for i in range(1, len(files_in_run)):
            run.append(
                pygame.transform.scale(pygame.image.load(os.path.join('Player_images/run', '' + str(i) + '.png')),
                                       (player_w_lvl, player_h_lvl)))

        jump = []
        files_in_jump = next(os.walk("Player_images/jump"))[2]
        for i in range(1, len(files_in_jump)):
            jump.append(
                pygame.transform.scale(pygame.image.load(os.path.join('Player_images/jump', '' + str(i) + '.png')),
                                       (player_w_lvl, player_h_lvl)))

        fall = []
        files_in_fall = next(os.walk("Player_images/fall"))[2]
        for i in range(0, len(files_in_fall)):
            fall.append(
                pygame.transform.scale(pygame.image.load(os.path.join('Player_images/fall', 'fall.png')),
                                       (player_w_lvl, player_h_lvl)))

        self.animations = dict({"idle": idle, "jump": jump, "run": run, "fall": fall})

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y


    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()

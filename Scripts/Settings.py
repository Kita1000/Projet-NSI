import pygame.image
import os

pygame.init()

screen_width = 1600
screen_height = 800
White = (255, 255, 255)
Black = (0, 0, 0)
GRAY = pygame.Color('gray12')
Game_Title = "A Perilous Journey"
FPS = 18

# Importation des Fonds d'ecran
options_background = pygame.image.load(os.path.join('Images/Transparent.png'))
Main_background = pygame.image.load(os.path.join('Images/Main_BG.jpg'))

# On definit des polices d'écritures
Main_font = pygame.font.Font("Fonts/Font.ttf", 85)
Button_font = pygame.font.Font("Fonts/Nicefont.ttf", 55)
other_Font = pygame.font.Font("Fonts/Main_Font.otf", 95)

# Importations d'images
idle = [pygame.image.load(os.path.join('Player_images', 'player_idle1.png')),
pygame.image.load(os.path.join('Player_images', 'player_idle2.png')),
pygame.image.load(os.path.join('Player_images', 'player_idle3.png')),
pygame.image.load(os.path.join('Player_images', 'player_idle4.png'))]


walk_right = [pygame.image.load(os.path.join('Player_images', 'player_run_r1.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_r2.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_r3.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_r4.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_r5.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_r6.png'))]


walk_left = [pygame.image.load(os.path.join('Player_images', 'player_run_l1.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_l2.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_l3.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_l4.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_l5.png')),
pygame.image.load(os.path.join('Player_images', 'player_run_l6.png'))]
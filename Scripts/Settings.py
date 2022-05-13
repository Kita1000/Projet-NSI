import pygame.image
import os

pygame.init()

White = (255, 255, 255)
Black = (0, 0, 0)
GRAY = pygame.Color('gray12')
Game_Title = "A Perilous Journey"
FPS = 30

# Importation des images
options_background = pygame.image.load(os.path.join('Images/Transparent.png'))
forest_start = pygame.image.load(os.path.join('Images/Forest_start.png'))
forest_start_overlay = pygame.image.load(os.path.join('Images/Forest_start_overlay.png'))
Logo = pygame.image.load("Images/Logo_Game.jpg")

# On definit des polices d'écritures
Main_font = pygame.font.Font("Fonts/Font.ttf", 85)
Button_font = pygame.font.Font("Fonts/Nicefont.ttf", 55)
other_Font = pygame.font.Font("Fonts/Main_Font.otf", 95)

# Importation de la musique
main_menu_music = pygame.mixer.Sound("Musique/main_theme.mp3")
forest_music = pygame.mixer.Sound("Musique/Forest_Game_Soundtrack.mp3")
click_sound = pygame.mixer.Sound("Musique/click_sound.mp3")


# Importation des boutons
options_but = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'options_button.png')), (260, 70))
options_but_clicked = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'options_button_clicked.png')), (260, 70))
play_but = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'play_button.png')), (260, 70))
play_but_clicked = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'play_button_clicked.png')), (260, 70))
quit_but = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Quit_button.png')), (260, 70))
quit_but_clicked = pygame.transform.scale(pygame.image.load(os.path.join('Images', 'Quit_button_clicked.png')),  (260, 70))


# Importation image titre
title_name = []
for i in range(1,19):
    title_name.append(pygame.transform.scale(pygame.image.load(os.path.join('Images/title', 'title' + str(i) + '.png')), (1000, 400)))

# Importation feuilles
leaf = []
for i in range(1,185):
    leaf.append(pygame.image.load(os.path.join('Images/leaves', 'leaf1_fall_' + str(i) + '.png')))

# Importation feu de camp
fire_camp = []
for i in range(1,6):
    fire_camp.append(pygame.image.load(os.path.join('Images/Fire_animation', 'fire_' + str(i) + '.png')))


# Importation images du joueur
idle = []
for i in range(1,5):
    idle.append(pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_' + str(i) + '.png')), (120, 165)))


walk_right = []
for i in range(6,14):
    walk_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_' + str(i) + '.png')), (120, 165)))


walk_left = []
for i in range(6,14):
    walk_left.append(pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_' + str(i) + '.png')), (120, 165)))

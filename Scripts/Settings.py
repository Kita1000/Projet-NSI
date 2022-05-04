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

main_menu_music = pygame.mixer.Sound("Musique/main_theme.mp3")
forest_music = pygame.mixer.Sound("Musique/Forest_Game_Soundtrack.mp3")

# Importations d'images du joueur
idle = [pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_01.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_02.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_03.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_04.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_05.png')), (120,165))]


walk_right = [pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_06.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_07.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_08.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_09.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_10.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_11.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_12.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_13.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_14.png')), (120,165))]


walk_left = [pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_06.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_07.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_08.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_09.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_10.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_11.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_12.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_13.png')), (120,165)),
pygame.transform.scale(pygame.image.load(os.path.join('Player_images', 'Player_14.png')), (120,165))]
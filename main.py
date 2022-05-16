import pygame, sys, random

from Scripts.Settings import *
from Scripts.Player_settings import *

from Niveaux.Code.level_1 import Level
from Niveaux.Code.level_data import level_1
from Niveaux.Code.level_settings import *

pygame.init()

# On dÃ©finit plusieurs variables
mainClock = pygame.time.Clock()

# On affiche un titre et un logo au jeu
pygame.display.set_caption('A Perilous Journey')
pygame.display.set_icon(Logo)

x = 65
y = 500
x_speed = 0
accel_x = 0
max_speed = 5
walkcount = 0
frames = 0
idle_wait = 0
fullscreen = True
frames_leaf = 0
rand_x = 0

info = pygame.display.Info()
fullscreen_w, fullscreen_h = screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

Main_background = pygame.transform.scale(pygame.image.load(os.path.join('Images/Main_BG.jpg')), (fullscreen_w,fullscreen_h))



# On dÃ©finit une fonction draw_Text pour pouvoir afficher du texte sur l'Ã©cran qui prend en compte :
# un texte, une police, une couleur, une position et une surface(sur laquelle on affiche le texte).
def draw_text(text, font, color, surface, text_x, text_y):
    textobj = font.render(text, 1, color)

    textrect = textobj.get_rect()
    textrect.topleft = (text_x, text_y)
    surface.blit(textobj, textrect)


def message_blit():
    text_mov = 0
    for character in message:
        draw_text(character, Button_font, (255, 255, 255), screen, screen_width / 3 + text_mov,
                  screen_height / 2)
        pygame.display.flip()
        pygame.time.wait(100)
        text_mov += 20


def characteranimation():
    global walkcount, idle_wait
    # walkcount se remet Ã  0 quand on a affichÃ© le joueur 18 fois (on affiche le joueur 3 fois pour chaque image)
    if walkcount + 1 >= 27:
        walkcount = 0

    # idle_wait est une liste de 4 images...
    # Donc quand idle_wait est supÃ©rieur ou egal a 5 on revient au debut de la liste d'image.
    if idle_wait + 1 >= 6:
        idle_wait = 0
    # Si le joueur va vers la gauche(accel_x nÃ©gatif) on blit les images walk_left.
    if x_speed < 0:
        # On blit une image de la liste walk_right pendant 3 tours de boucle.
        # Donc si on augmente la valeur de FPS le joueur aura des animations plus rapides.
        screen.blit(walk_left[walkcount // 3], (x, y))
        walkcount += 1
    # Si le joueur va vers la droite(accel_x positif) on blit les images walk_right.
    if x_speed > 0:
        # On blit une image de la liste walk_right pendant 3 tours de boucle.
        screen.blit(walk_right[walkcount // 3], (x, y))
        walkcount += 1
    # Si le joueur n'avance ni vers la droite ni vers la gauche on blit les images idle.
    if x_speed == 0:
        screen.blit(idle[idle_wait // 2], (x, y))
        idle_wait += 1

def title_animation():
    global frames
    if frames + 1 >= 55:
        frames = 0
    screen.blit(title_name[frames // 3], (screen_width/4.6, screen_height/4.6))
    frames +=1

def leaf_falling(leafs):
    global frames_leaf, rand_x
    if frames_leaf + 1 >= 366:
        frames_leaf = 0
        rand_x = random.randrange(20, screen_width)
    screen.blit(leaf[frames_leaf // 2], (rand_x, 0))
    frames_leaf += 1



# On dÃ©finit une classe qui s'occupe de tout dans le Menu Principal
class Main_Menu:
    def __init__(self):
        pygame.mixer.music.load("Musique/main_theme.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        Main_Menu.start(self)

    def start(self):
        global but_color, screen_width, screen_height, Main_background
        click = False
        while True:
            screen.blit(Main_background, (0, 0))
            # On affiche le Nom du jeu sur le fond d'Ã©cran

            title_animation()

            # On veut trouver la position de la souris et on l'attribut Ã  mx et my
            mx, my = pygame.mouse.get_pos()

            # On définit trois boutons pour le menu.
            Play_Game_but = pygame.Rect(screen_width / 2.45, screen_height / 1.8, 260, 70)
            Options_but = pygame.Rect(screen_width / 2.45, screen_height / 1.59, 260, 70)
            Quit_Game_but = pygame.Rect(screen_width / 2.45, screen_height / 1.4, 260, 70)

            screen.blit(play_but, (screen_width / 2.45, screen_height / 1.8))
            screen.blit(options_but, (screen_width / 2.45, screen_height / 1.59))
            screen.blit(quit_but, (screen_width / 2.45, screen_height / 1.43))

            # Si le curseur se trouve sur le rectangle et si l'utilisateur click...
            if Play_Game_but.collidepoint((mx, my)):
                #...on affiche l'image du bouton clicked
                screen.blit(play_but_clicked, (screen_width / 2.45, screen_height / 1.8))
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    # On envoie le joueur vers le jeu.
                    start_animation()

            if Options_but.collidepoint((mx, my)):
                screen.blit(options_but_clicked, (screen_width / 2.45, screen_height / 1.59))
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    # On envoie le joueur vers les options
                    options()

            if Quit_Game_but.collidepoint((mx, my)):
                screen.blit(quit_but_clicked, (screen_width / 2.45, screen_height / 1.43))
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    # On quitte le jeu
                    pygame.time.wait(270)
                    pygame.quit()
                    sys.exit()

            leaf_falling(10)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On dÃ©finit ce qu'est qu'un click.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            # On update l'Ã©cran Ã  chaque tour de boucle
            pygame.display.flip()
            # On tourne le jeu a la valeur de FPS
            mainClock.tick(FPS)


class options:
    def __init__(self):
        global click, fullscreen, screen_width, screen_height, Main_background, forest_start
        click = False

        running = True
        while running:
            if fullscreen == False:
                screen_width, screen_height = 1600, 800
                screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
                Main_background = pygame.transform.scale(pygame.image.load(os.path.join('Images/Main_BG.jpg')),
                                                         (screen_width, screen_height))
                forest_start = pygame.transform.scale(pygame.image.load(os.path.join('Images/Forest_start.png')),
                                                         (screen_width, screen_height))
            else:
                screen_width, screen_height = fullscreen_w, fullscreen_h
                screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
                Main_background = pygame.transform.scale(pygame.image.load(os.path.join('Images/Main_BG.jpg')),
                                                         (fullscreen_w, fullscreen_h))
                forest_start = pygame.transform.scale(pygame.image.load(os.path.join('Images/Forest_start.png')),
                                                      (fullscreen_w, fullscreen_h))

            screen.blit(Main_background, (0, 0))
            screen.blit(options_background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        Main_Menu.start(self)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            draw_text('Options', Button_font, (0, 0, 25), screen, screen_width / 2 - 50, 100)
            draw_text('Player Movement :', Button_font, (0, 0, 25), screen, screen_width / 2 - 100, 200)
            draw_text('Run Right :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 300)
            draw_text('D or ->', Button_font, (0, 0, 25), screen, screen_width / 2, 300)
            draw_text('Run Left :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 400)
            draw_text('Q or <-', Button_font, (0, 0, 25), screen, screen_width / 2, 400)
            draw_text('Sprint :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 500)
            draw_text('Ctrl + left or right', Button_font, (0, 0, 25), screen, screen_width / 2, 500)

            mx, my = pygame.mouse.get_pos()

            Exit_but = pygame.Rect(screen_width - 200, 240, 100, 50)

            if Exit_but.collidepoint((mx, my)):
                but1_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    Main_Menu.start(self)
            else:
                but1_color = (100, 69, 50)

            pygame.draw.rect(screen, but1_color, Exit_but)
            draw_text('Exit', Button_font, (0, 0, 25), screen, screen_width - 200, 250)

            fullscreen_but = pygame.Rect(screen_width / 2 - 50, screen_height / 1.3, 100, 50)

            if fullscreen_but.collidepoint((mx, my)):
                but1_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    fullscreen = True

            else:
                but1_color = (100, 69, 50)

            pygame.draw.rect(screen, but1_color, fullscreen_but)
            draw_text('Fullscreen', Button_font, (0, 0, 25), screen, screen_width / 2 - 50, screen_height / 1.3)

            small_window_but = pygame.Rect(screen_width / 2 - 200, screen_height / 1.3, 100, 50)

            if small_window_but.collidepoint((mx, my)):
                but1_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.set_volume(click_sound, 0.2)
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    fullscreen = False
            else:
                but1_color = (100, 69, 50)

            pygame.draw.rect(screen, but1_color, small_window_but)
            draw_text('1800x1600', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, screen_height / 1.3)

            pygame.display.flip()
            mainClock.tick(FPS)


class game_selection:
    def __init__(self):
        global screen
        click = False
        game_selection_run = True
        while game_selection_run:

            screen.blit(Main_background, (0, 0))
            screen.blit(options_background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    game_selection_run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_selection_run = False
                        Main_Menu.start(self)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            mx, my = pygame.mouse.get_pos()

            profile_1_but = pygame.Rect(screen_width / 2.4, screen_height / 2.8, 250, 50)
            profile_2_but = pygame.Rect(screen_width / 2.4, screen_height / 2.8 + 120, 250, 50)
            profile_3_but = pygame.Rect(screen_width / 2.4, screen_height / 2.8 + 240, 250, 50)

            if profile_1_but.collidepoint((mx, my)):
                but1_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    # On envoie le joueur vers le jeu.
                    start_animation()
            else:
                but1_color = (100, 69, 50)
            if profile_2_but.collidepoint((mx, my)):
                but2_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    # On envoie le joueur vers les options
                    start_animation()
            else:
                but2_color = (100, 69, 50)
            if profile_3_but.collidepoint((mx, my)):
                but3_color = (100, 100, 100)
                if click:
                    pygame.mixer.Sound.play(click_sound)
                    pygame.time.wait(100)
                    # On quitte le jeu
                    start_animation()
            else:
                but3_color = (100, 69, 50)

            pygame.draw.rect(screen, but1_color, profile_1_but)
            draw_text("Profile 1", Button_font, (255, 255, 255), screen, screen_width / 2.2,
                      screen_height / 2.8 + 5)

            pygame.draw.rect(screen, but2_color, profile_2_but)
            draw_text("Profile 2", Button_font, (255, 255, 255), screen, screen_width / 2.2,
                      screen_height / 2.8 + 125)

            pygame.draw.rect(screen, but3_color, profile_3_but)
            draw_text("Profile 3", Button_font, (255, 255, 255), screen, screen_width / 2.2,
                      screen_height / 2.8 + 245)

            draw_text("Profile Selector", Button_font, (255, 255, 255), screen, screen_width / 2.35,
                      screen_height / 2.8 - 100)

            pygame.display.flip()


class start_animation:
    def __init__(self):
        global message, click, left_pressed, right_pressed, up_pressed, down_pressed, left_shift, accel_x, wait, x_speed, accel_x, y, x, max_speed

        intro_not_start = True
        click = False
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.load("Musique/Forest_Game_Soundtrack.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        waiting = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Main_Menu()
                    if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        wait = 0
                        left_pressed = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        wait = 0
                        right_pressed = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        left_pressed = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        right_pressed = False


            screen.fill(GRAY)
            message = "Deep in the Woods"
            if intro_not_start:
                message_blit()
                draw_text("Click to continue . . .", Button_font, (0, 0, 0), screen, screen_width - 400,
                          screen_height - 100)
                pygame.display.flip()
                while click == False:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                click = False
                    intro_not_start = False

            play_level_1()


class play_level_1:
    def __init__(self):

        screen = pygame.display.set_mode((lvl_screen_width, lvl_screen_height))
        level = Level(level_1, screen)
        game_clock = pygame.time.Clock()
        while True:
            mainClock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_menu()

            screen.fill((0, 0, 0))
            level.run()
            game_clock.tick(60)
            pygame.display.flip()


class pause_menu:
    # add a pause screen
    pass


# On renvoie le programme Ã la classe Main_Menu pour commencer le jeu.
Main_Menu()
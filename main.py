import sys,pygame
import main
from Scripts.Player_settings import *
from Scripts.Settings import *

pygame.init()

# On définit plusieurs variables
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
# On affiche un titre et un logo au jeu
pygame.display.set_caption('A Perilous Journey')
Logo = pygame.image.load("Images/Logo_Game.jpg")
pygame.display.set_icon(Logo)


# On définit une fonction draw_Text pour pouvoir afficher du texte sur l'écran qui prend en compte :
# un texte, une police, une couleur, une position et une surface(sur laquelle on affiche le texte).
def draw_text(text, font, color, surface, text_x, text_y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (text_x, text_y)
    surface.blit(textobj, textrect)


# Defintion qui ermet d'afficher l'animation du joueur.
def characteranimation():
    global walkcount, idle_wait
    # walkcount se remet à 0 quand on a affiché le joueur 18 fois (on affiche le joueur 3 fois pour chaque image)
    if walkcount + 1 >= 18:
        walkcount = 0

    # idle_wait est une liste de 4 images...
    # Donc quand idle_wait est supérieur ou egal a 5 on revient au debut de la liste d'image.
    if idle_wait + 1 >= 5:
        idle_wait = 0
    # Si le joueur va vers la gauche(accel_x négatif) on blit les images walk_left.
    if accel_x < 0:
        # On blit une image de la liste walk_right pendant 3 tours de boucle.
        # Donc si on augmente la valeur de FPS le joueur aura des animations plus rapides.
        screen.blit(walk_left[walkcount // 3], (x, y))
        walkcount += 1
    # Si le joueur va vers la droite(accel_x positif) on blit les images walk_right.
    if accel_x > 0:
        # On blit une image de la liste walk_right pendant 3 tours de boucle.
        screen.blit(walk_right[walkcount // 3], (x, y))
        walkcount += 1
    # Si le joueur n'avance ni vers la droite ni vers la gauche on blit les images idle.
    if accel_x == 0:
        screen.blit(idle[idle_wait // 2], (x, y))
        idle_wait += 1

    pygame.display.flip()


# On definit une classe qui s'occupe de tout dans le Menu Principal
class Main_Menu:
    def __init__(self):

        click = False

        while True:
            screen.blit(Main_background, (0, 0))
            # On affiche le Nom du jeu sur le fond d'écran
            draw_text('A Perilous Journey', Main_font, (49, 61, 50), screen, screen_width / 3.25,
                      screen_height / 2.65)

            # On veut trouver la position de la souris et on l'attribut à mx et my
            mx, my = pygame.mouse.get_pos()

            # On définit trois boutons pour le menu.
            Play_Game_but = pygame.Rect(screen_width / 2.4, screen_height / 1.78, 250, 50)
            Options_but = pygame.Rect(screen_width / 2.4, screen_height / 1.75 + 75, 250, 50)
            Quit_Game_but = pygame.Rect(screen_width / 2.4, screen_height / 1.75 + 150, 250, 50)

            # Si le curseur se trouve sur le button et si l'utilisateur click...
            if Play_Game_but.collidepoint((mx, my)):
                if click:
                    # On envoie le joueur vers le jeu.
                    new_game()
            if Options_but.collidepoint((mx, my)):
                if click:
                    # On envoie le joueur vers les options
                    options()
            if Quit_Game_but.collidepoint((mx, my)):
                if click:
                    # On quitte le jeu
                    pygame.quit()
                    sys.exit()
            # On dessine le Button Play_game_but sur l'écran
            pygame.draw.rect(screen, (131, 90, 63), Play_Game_but)
            # On dessine le texte "Play Game" sur le button.
            draw_text("Play Game", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.75)
            # Même chose pour le bouton Options
            pygame.draw.rect(screen, (131, 90, 63), Options_but)
            draw_text("Options", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.5)
            # Même chose pour le bouton quitter le jeu
            pygame.draw.rect(screen, (131, 90, 63), Quit_Game_but)
            draw_text("Quit Game", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On définit ce qu'est qu'un click.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            # On update l'écran à chaque tour de boucle
            pygame.display.flip()
            # On tourne le jeu a la valeur de FPS
            mainClock.tick(FPS)


class new_game:
    def __init__(self):
        # On a besoin des variables et on vas changer leurs valeurs donc on doit les rendre global.
        global click, left_pressed, right_pressed, up_pressed, down_pressed, left_shift, accel_x, wait, x_change, accel_x, y, x, max_speed

        click = False
        # Ajouter une animation avec une boite de texte pour le joueur...
        screen.fill((0, 0, 0))
        draw_text("Where am I ?", Button_font, (255, 255, 255), screen, screen_width / 2.75,
                  screen_height / 2)
        pygame.display.flip()

        # On fait une pause entre chaque texte
        pygame.time.delay(2 * 500)
        screen.fill((0, 0, 0))
        draw_text("What is this place?", Button_font, (255, 255, 255), screen, screen_width / 2.75,
                  screen_height / 2)
        pygame.display.flip()
        pygame.time.delay(2 * 500)

        running = True
        while running:
            mainClock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        main.Main_Menu()
                    # On définit les inputs.
                    if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        wait = 0
                        left_pressed = True
                        accel_x = -10
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        wait = 0
                        right_pressed = True
                        accel_x = 10

                    if event.key == pygame.K_LSHIFT:
                        left_shift = True
                    # On ajoute du sprint pour le joueur can il avance vers la droite en appuyant ctrl
                    if left_shift == True and right_pressed == True:
                        accel_x = 17
                        max_speed = 23
                    # Meme chose pour le côté gauche.
                    if left_shift == True and left_pressed == True:
                        accel_x = -17
                        max_speed = 23
                    # (En cours) Ajouter fonctions pour le saut
                    if event.key == pygame.K_SPACE:
                        up_pressed = True
                    # (Futurs) Ajouter pour descendre plus vite et descendre des plateformes
                    if event.key == pygame.K_DOWN:
                        down_pressed = True

                # On remet toutes les valeurs à 0 et false quand le joueur arrète d'appuyer sur une touche
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        left_pressed = False
                        accel_x = 0
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        right_pressed = False
                        accel_x = 0
                    if event.key == pygame.K_LSHIFT:
                        left_shift = False

                    if left_shift == True and right_pressed == True:
                        accel_x = 0
                        right_pressed = False
                        left_shift = False

                    if left_shift == True and left_pressed == True:
                        accel_x = 0
                        left_pressed = False
                        left_shift = False

                    if event.key == pygame.K_SPACE:
                        up_pressed = False
                    if event.key == pygame.K_DOWN:
                        down_pressed = False

            # On donne a x la valeur de accel_x donc le joueur accélère dans la direction est avec la valeur de accel_x
            x_change += accel_x
            # Si la valeur de x_change dépasse max speed
            if abs(x_change) >= max_speed:
                # On divise x_change par multiplie x_change par la vitesse maximale
                x_change = x_change / abs(x_change) * max_speed

            # On ajoute de la deceleration quand le joueur arrète de bouger.
            if accel_x == 0:
                x_change *= 0.2

            # On bouge le joueur
            x += x_change

            screen.blit(Main_background, (0, 0))
            characteranimation()
            pygame.display.flip()


class options:
    def __init__(self):
        global click
        click = False

        running = True
        while running:
            screen.blit(Main_background, (0, 0))
            screen.blit(options_background, (0, 0))

            draw_text('Options', Button_font, (0, 0, 25), screen, screen_width / 2 - 50, 100)
            draw_text('Player Mouvement :', Button_font, (0, 0, 25), screen, screen_width / 2 - 100, 200)
            draw_text('Run Right :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 300)
            draw_text('D or ->', Button_font, (0, 0, 25), screen, screen_width / 2, 300)
            draw_text('Run Left :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 400)
            draw_text('Q or <-', Button_font, (0, 0, 25), screen, screen_width / 2, 400)
            draw_text('Sprint :', Button_font, (0, 0, 25), screen, screen_width / 2 - 200, 500)
            draw_text('Ctrl + left or right', Button_font, (0, 0, 25), screen, screen_width / 2, 500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        main.Main_Menu()

            pygame.display.flip()
            mainClock.tick(FPS)


# On renvoie le programme à la classe Main_Menu pour commencer le jeu.
Main_Menu()

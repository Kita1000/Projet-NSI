from Scripts.Settings import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
mainclock = pygame.time.Clock()

class player:
    def __init__(self):
        self.x = 65
        self.y = 500
        self.start_x = 65
        self.start_y = 500
        self.x_change = 0
        self.accel_x = 0
        self.max_speed = 15
        self.walkcount = 0
        self.idle_wait = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.left_shift = False

    def player_movement(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # On définit les inputs.
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    wait = 0
                    self.left_pressed = True
                    self.accel_x = -10
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    wait = 0
                    self.right_pressed = True
                    self.accel_x = 10

                if event.key == pygame.K_LSHIFT:
                    self.left_shift = True
                # On ajoute du sprint pour le joueur can il avance vers la droite en appuyant ctrl
                if self.left_shift == True and self.right_pressed == True:
                    self.accel_x = 17
                    self.max_speed = 23
                # Meme chose pour le côté gauche.
                if self.left_shift == True and self.left_pressed == True:
                    self.accel_x = -17
                    self.max_speed = 23
                # (En cours) Ajouter fonctions pour le saut
                if event.key == pygame.K_SPACE:
                    self.up_pressed = True
                # (Futurs) Ajouter pour descendre plus vite et descendre des plateformes
                if event.key == pygame.K_DOWN:
                    self.down_pressed = True

            # On remet toutes les valeurs à 0 et false quand le joueur arrète d'appuyer sur une touche
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.left_pressed = False
                    self.accel_x = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                    self.accel_x = 0
                if event.key == pygame.K_LSHIFT:
                    self.left_shift = False

                if self.left_shift == True and self.right_pressed == True:
                    self.accel_x = 0
                    self.right_pressed = False
                    self.left_shift = False

                if self.left_shift == True and self.left_pressed == True:
                    self.accel_x = 0
                    self.left_pressed = False
                    self.left_shift = False

                if event.key == pygame.K_SPACE:
                    self.up_pressed = False
                if event.key == pygame.K_DOWN:
                    self.down_pressed = False

            # On donne a x la valeur de accel_x donc le joueur accélère dans la direction est avec la valeur de accel_x

            self.x_change += self.accel_x
            # Si la valeur de x_change dépasse max speed
            if abs(self.x_change) >= self.max_speed:
                # On divise x_change par multiplie x_change par la vitesse maximale
                self.x_change = self.x_change / abs(self.x_change) * self.max_speed

            # On ajoute de la deceleration quand le joueur arrète de bouger.
            if self.accel_x == 0:
                self.x_change *= 0.2

            # On bouge le joueur
            self.x += self.x_change

    # Defintion qui ermet d'afficher l'animation du joueur.
    def characteranimation(self):
        global walkcount, idle_wait
        # walkcount se remet à 0 quand on a affiché le joueur 18 fois (on affiche le joueur 3 fois pour chaque image)
        if self.walkcount + 1 >= 18:
            self.walkcount = 0

        # idle_wait est une liste de 4 images...
        # Donc quand idle_wait est supérieur ou egal a 5 on revient au debut de la liste d'image.
        if idle_wait + 1 >= 5:
            idle_wait = 0
        # Si le joueur va vers la gauche(accel_x négatif) on blit les images walk_left.
        if self.accel_x < 0:
            # On blit une image de la liste walk_right pendant 3 tours de boucle.
            # Donc si on augmente la valeur de FPS le joueur aura des animations plus rapides.
            screen.blit(walk_left[walkcount // 3], (self.x, self.y))
            walkcount += 1
        # Si le joueur va vers la droite(accel_x positif) on blit les images walk_right.
        if self.accel_x > 0:
            # On blit une image de la liste walk_right pendant 3 tours de boucle.
            screen.blit(walk_right[walkcount // 3], (self.x, self.y))
            walkcount += 1
        # Si le joueur n'avance ni vers la droite ni vers la gauche on blit les images idle.
        if self.accel_x == 0:
            screen.blit(idle[idle_wait // 2], (self.x, self.y))
            idle_wait += 1

    def level_1(self):
        if self.x > screen_width - 200:
            print('Poopoo')



run = True
while run:
    mainclock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.fill((250,250,10))
    player()
    pygame.display.flip()

import pygame.image

class enemy(object): #importation des images de l'ennemi
    walkRight = [pygame.image.load('Castle_Enemyr9.png'), pygame.image.load('Castle_Enemyr10.png'),#on définit les images du mouvement du personnage pour le mouvement a droite
                 pygame.image.load('Castle_Enemyr11.png'), pygame.image.load('Castle_Enemyr12.png')],
    walkLeft = [pygame.image.load('Castle_Enemyl9.png'), pygame.image.load('Castle_Enemyl10.png'),#on définit les images du mouvement du personnage pour le mouvement a gauche
                pygame.image.load('Castle_Enemyl11.png'), pygame.image.load('Castle_Enemyl12.png')],

    def __init__(self, x, y, width, height, end): #on définit les coordonées et la trajectoire de l'ennemi
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]#on définit la trajectoire
        self.walkCount = 0
        self.vel = 3#on définit la vitesse
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)#on définit la hitbox

    def draw(self,win): #création de la trajectoire des ennemis
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0: #si la vitesse est superieure a 0
            win.blit(self.walkRight(self.walkCount //3), (self.x, self.y)) #avancer vers la droite
            self.walkCount += 1
        else:#si la vitesse est inferieure a 0
            win.blit(self.walkLeft(self.walkCount //3), (self.x, self.y))#avancer vers la gauche
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) #on définit de la hitbox
        pygame.draw.rect(win, (255,0,0), self.hitbox,2) #on déssine la hitbox

    def move(self): #le personnage se déplace sur la trajectoire
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel + -1
                self.walkCount = 0





import pygame.image

# player_Img = pygame.image.load('Playerimg.png')
# self.Scale_img = pygame.transform.scale(player_Img,
#                                               (player_Img.get_width() * scale, player_Img.get_height() * scale))
# self.rect = self.Scale_img.get_rect()
# self.rect.center = (x, y)
screen_width = 1600
screen_height = 800
White = (255, 255, 255)
Black = (0, 0, 0)
Game_Title = "A Perilous Journey"
FPS = 120

player_idle = [pygame.image.load('individualsprites/adventurer-idle-00.png'),
               pygame.image.load('individualsprites/adventurer-idle-01.png'),
               pygame.image.load('individualsprites/adventurer-idle-03.png')]

walk_right = [pygame.image.load('individualsprites/adventurer-run-00.png'),
              pygame.image.load('individualsprites/adventurer-run-01.png'),
              pygame.image.load('individualsprites/adventurer-run-02.png'),
              pygame.image.load('individualsprites/adventurer-run-03.png'),
              pygame.image.load('individualsprites/adventurer-run-04.png'),
              pygame.image.load('individualsprites/adventurer-run-05.png')]

# platform x position, y position, width, height
Platform_List = {(0, screen_height - 180, screen_width, 380),
                 (0, 400, 400, 50), (1200, 400, 400, 50)}

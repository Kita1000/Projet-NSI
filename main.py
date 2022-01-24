import pygame
import sys
from Sprites import*

pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption('A Perilous Journey')
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
Main_background = pygame.image.load("Main_BG.jpg")

Main_font = pygame.font.Font("Main_Font.otf", 95)
Button_font = pygame.font.Font("Nicefont.ttf", 55)


# Setup pygame/window ---------------------------------------- #

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Main_Menu:
    def __init__(self):

        click = False

        while True:
            screen.blit(Main_background, (0, 0))

            draw_text('A Perilous Journey', Main_font, (20, 85, 22), screen, screen_width / 2.87,
                      screen_height / 2.65)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(screen_width / 2.4, screen_height / 1.78, 250, 50)
            button_2 = pygame.Rect(screen_width / 2.4, screen_height / 1.75 + 75, 250, 50)
            button_3 = pygame.Rect(screen_width / 2.4, screen_height / 1.75 + 150, 250, 50)

            if button_1.collidepoint((mx, my)):
                if click:
                    new_game()
            if button_2.collidepoint((mx, my)):
                if click:
                    options()
            if button_3.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(screen, (107, 66, 37), button_1)
            draw_text("Play Game", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.75)
            pygame.draw.rect(screen, (107, 66, 37), button_2)
            draw_text("Options", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.5)
            pygame.draw.rect(screen, (107, 66, 37), button_3)
            draw_text("Quit Game", Button_font, (255, 255, 255), screen, screen_width / 2.25,
                      screen_height / 1.3)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(FPS)


class new_game:
    def __init__(self):

        # Player introduction need to add fade, only pops up at every new game.
        screen.fill((0, 0, 0))
        draw_text("Where am I ?", Main_font, (255, 255, 255), screen, screen_width / 2.75,
                  screen_height / 2)
        pygame.display.flip()
        pygame.time.delay(2 * 500)
        screen.fill((0, 0, 0))
        draw_text("What is this place?", Main_font, (255, 255, 255), screen, screen_width / 2.75,
                  screen_height / 2)
        pygame.display.flip()
        pygame.time.delay(2 * 500)

        player = Player(screen_width / 2, screen_height / 2)

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
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = True
                    if event.key == pygame.K_UP:
                        player.up_pressed = True
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = False
                    if event.key == pygame.K_UP:
                        player.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = False

            screen.blit(Main_background, (0, 0))
            player.draw(screen)
            player.update()
            pygame.display.flip()


class options:
    def __init__(self):
        running = True
        while running:
            screen.fill((0, 0, 0))

            draw_text('Options', Button_font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            mainClock.tick(FPS)




Main_Menu()

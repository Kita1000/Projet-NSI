import pygame

pygame.init()

win = pygame.display.set_mode((1600, 800))

pygame.display.set_caption("A Perilous Journey")

bg = pygame.image.load('Main_BG.jpg')

idleright = [pygame.image.load('individualsprites/adventurer-idle-00.png'),
             pygame.image.load('individualsprites/adventurer-idle-01.png'),
             pygame.image.load('individualsprites/adventurer-idle-02.png')]

walk_right = [pygame.image.load('individualsprites/adventurer-run-00.png'),
              pygame.image.load('individualsprites/adventurer-run-01.png'),
              pygame.image.load('individualsprites/adventurer-run-02.png'),
              pygame.image.load('individualsprites/adventurer-run-03.png'),
              pygame.image.load('individualsprites/adventurer-run-04.png'),
              pygame.image.load('individualsprites/adventurer-run-05.png')]

walk_left = [pygame.image.load('individualsprites/adventurer-run-left1.png'),
             pygame.image.load('individualsprites/adventurer-run-left2.png'),
             pygame.image.load('individualsprites/adventurer-run-left3.png'),
             pygame.image.load('individualsprites/adventurer-run-left4.png'),
             pygame.image.load('individualsprites/adventurer-run-left5.png'),
             pygame.image.load('individualsprites/adventurer-run-left6.png')]

char = pygame.image.load('individualsprites/adventurer-idle-00.png')

player_x = 50
player_y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

walkCount = 0

p_right_pressed = False
p_left_pressed = False
p_right_released = False
p_left_released = False
max_speed = False
acceleration = 1
speed = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 18:
        walkCount = 0

    if p_left_pressed:
        win.blit(walk_left[walkCount // 3], (player_x, player_y))
        walkCount += 1
    elif p_right_released:
        win.blit(walk_right[walkCount // 3], (player_x, player_y))
        walkCount += 1
    else:
        win.blit(idleright[walkCount // 1], (player_x, player_y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(28)

    keys = pygame.key.get_pressed()
    max_speed = False
    acceleration = 1
    x_speed = 0
    deceleration = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or pygame.K_RIGHT:
                p_right_pressed = True
                while p_right_pressed:
                    # Acceleration happens every 100 milliseconds

                    # Accelerate until speed is maxed
                    acceleration += x_speed
                    player_x += x_speed
                    if x_speed == 3:
                        max_speed = True
                        acceleration = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                p_right_released = True
                while p_right_released:
                    pygame.time.wait(1)
                    deceleration += max_speed
                    player_x -= x_speed
                    if max_speed == 0:
                        deceleration = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            player_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()

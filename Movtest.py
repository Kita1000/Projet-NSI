import pygame

pygame.init()
display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

GRAY = pygame.Color('gray12')

display_width, display_height = display.get_size()

x = display_width * 0.45
y = display_height * 0.8

pressed_r = False
pressed_l = False
forw_maxspeed = 10
back_maxspeed = -forw_maxspeed
accel_x = 1
x_speed = 0

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_l = True
            elif event.key == pygame.K_RIGHT:
                pressed_r = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_l = False
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                pressed_r = False
                x_speed = 0

    if pressed_r:
        # vitesse instantanée
        x_speed += 1
        if x_speed >= forw_maxspeed:
            x_speed = forw_maxspeed
            x += x_speed
        else:
            x_speed += accel_x


    if pressed_l:
       #vitesse instantanée
        x_speed += 1
        if x_speed >= forw_maxspeed:
            x_speed = forw_maxspeed
            x = x + x_speed
        else:
            x_speed += accel_x

    x += x_speed



    if x>= 1000:
        x=0

    if x <= 0:
        x = 1000

    display.fill(GRAY)
    pygame.draw.rect(display, (0, 120, 250), (x, y, 20, 40))
    pygame.display.update()
    clock.tick(60)


pygame.quit()

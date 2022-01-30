import pygame
from Settings import*


pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
GRAY = pygame.Color('gray12')
display_width, display_height = display.get_size()
x = display_width * 0.45
y = display_height * 0.8
x_change = 0
accel_x = 0
max_speed = 6
left = False
right = False
walkCount = 0
wait = 0

def redrawGameWindow():
    global walkCount,wait

    if walkCount + 1 >= 18:
        walkCount = 0

    if wait +1 >=3:
        wait=0

    if left:
        display.blit(walk_left[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        display.blit(walk_right[walkCount // 3], (x,y))
        walkCount += 1


    pygame.display.flip()

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                crashed = True
        elif event.type == pygame.KEYDOWN:

            # Set the acceleration value.
            if event.key == pygame.K_LEFT:
                wait = 0
                left = True
                accel_x = -.2
            elif event.key == pygame.K_RIGHT:
                wait = 0
                right = True
                accel_x = .2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                right = False
                left = False
                accel_x = 0

    x_change += accel_x  # Accelerate.
    if abs(x_change) >= max_speed:  # If max_speed is exceeded.
        # Normalize the x_change and multiply it with the max_speed.
        x_change = x_change/abs(x_change) * max_speed

    # Decelerate if no key is pressed.
    if accel_x == 0:
        x_change *= 0.84

    x += x_change  # Move the object.

    display.fill(GRAY)
    redrawGameWindow()
    clock.tick(60)

pygame.quit()
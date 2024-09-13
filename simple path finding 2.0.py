import pygame
import random, math

#player cords
x = random.randint(100, 500)
y = random.randint(100, 300)

#enemy cords
x2 = 0
y2 = 500

#speed
vel = 5 #1.5

# Initializing Pygame
pygame.init()
 
# Initializing surface
width = 500
height = 500
canvas = pygame.display.set_mode((width, height))

# Initializing RGB Color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# main objects

def enemy():
    global x2, y2
    # pythagorus
    diff_x = x - x2
    diff_y = y - y2
    hype = math.sqrt((diff_x**2) + (diff_y**2))
    diff_x_per = (diff_x * 0.1)
    diff_y_per = (diff_y * 0.1)
    #print(diff_x, diff_y)
    #print(hype)
    if 1==1:
        x2 += diff_x_per
        y2 += diff_y_per
    

    pygame.draw.circle(canvas, black, (x2, y2), 10) #enemy



def player():
    pygame.draw.circle(canvas, red, (x, y), 10) #player



def game():
    global x, y, white, black, x2, y2, vel, width, height
    running = True

    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # left
            if x > 12:
                x -= vel

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # right
            if x < width-12:
                x += vel

        if keys[pygame.K_UP] or keys[pygame.K_w]:  # up
            if y > 12:
                y -= vel

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # down
            if y < height-12:
                y += vel

        canvas.fill(white)    
        pygame.draw.line(canvas, red, (x, y), (x2, y2), 2)
        enemy()
        player()

        pygame.display.update()

        pygame.time.Clock().tick(60)




game()
pygame.quit()


# now to get the object to move toward to player


# getting the movement towards to player - worked out now just getting coords of player to move it towards - pretty easy
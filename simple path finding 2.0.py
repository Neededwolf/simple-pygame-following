import pygame
import random, math, time


go = True
#needed vars
clock = 0
running = True
#player cords
x = random.randint(100, 500)
y = random.randint(100, 300)
var = 0
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
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)



# main objects

def enemy():
    global x2, y2, diff_x
    # pythagorus
    diff_x = x - x2
    diff_y = y - y2
    hype = math.sqrt((diff_x**2) + (diff_y**2))
    diff_x_per = (diff_x * 0.01)
    diff_y_per = (diff_y * 0.01)
    #print(diff_x, diff_y)
    #print(hype)
    if 1==1:
        x2 += diff_x_per
        y2 += diff_y_per
    

    enemy = pygame.draw.circle(canvas, black, (x2, y2), 10) #enemy




def player():
    player = pygame.draw.circle(canvas, red, (x, y), 10) #player


def end_game():
    global running, go
    go = False
    


def collision():
    difference_x = x2 - x
    difference_y = y2 - y
    is_safe = 18
    if difference_x > is_safe or difference_x < -is_safe:
        pass
        
    
    elif difference_y > is_safe or difference_y < -is_safe:
        pass
    
    else:
        end_game()
            

def timer():
    global clock, timing
    if go:
        clock += 1
        timing = clock / 60
    else:
        pass


def timer_display():
    global clock, timing, running
    if go:
        timing = str(round(timing, 2))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(timing + "s", True, green, white)
        textRect = text.get_rect()
        textRect.center = (width/2, height/2)
        canvas.blit(text, textRect)
    
    else:
        print("1")
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font2.render(timing + " seconds alive", True, red, white)
        textRect2 = text2.get_rect()
        textRect2.center = (width/2, 100)
        canvas.blit(text2, textRect2)
        running = False
        pygame.display.update()
        pygame.time.wait(2000)

        
    


def game():
    global x, y, white, black, x2, y2, vel, width, height, running
    

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
        timer()
        timer_display()
        player()
        enemy()
        collision()



        pygame.display.update()
        
        pygame.time.Clock().tick(60)




game()
pygame.quit()


# now to get the object to move toward to player


# getting the movement towards to player - worked out now just getting coords of player to move it towards - pretty easy
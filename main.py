import random
import pygame
import sys

pygame.init()

# deifne glovals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (149, 188, 226)
RED = (255, 0, 0)
size = (800, 600)
framerate = 60
col1_x = 400
col2_x = 700
col3_x = 1000
col1_y = -100
col2_y = random.randint(-200, 0)
col3_y = random.randint(-200, 0)
dead = False
score = 0
score_collision = []
collision = []
wait=150


#importing images
bg = pygame.image.load("flappybird_tlo.png")
podloga = pygame.image.load("D:\podłoga.png")
column_bot = pygame.image.load("D:\column_bot.png")
column_top = pygame.image.load("D:\column_top.png")
ptak = pygame.image.load("D:\ptak.png")


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy bird")

# The loop will carry on until the user exits the game (e.g. clicks the close button).

clock = pygame.time.Clock()

bird_y = 200
bird_velocity_y = 1
font1 = pygame.freetype.Font("C:/Users/eryko/PycharmProjects/FlappyBird/8-bit Arcade Out.ttf", 72)

def you_lost():
    global bird_y, bird_velocity_y, col1_x, col2_x, col3_x, collision, dead
    if bird_y >= 700 or any(collision):
        collision = []
        # columns stop moving
        col1_x -= 0
        col2_x -= 0
        col3_x -= 0
        bird_velocity_y += 2  # bird falls
        dead = True


def add_points():
    global score, score_collision
    if any(score_collision):
        score += 1


carryOn = True
# -------- Main Program Loop -----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we can exit the while loop

        # Game logic
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dead:
                bird_velocity_y = -7.5
            #if event.key == pygame.K_SPACE and dead:
                # main()
                #dead = False

        # --- Drawing code should go here
        # First, clear the screen to white.
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))


    # drawin the columns and making them move
    col1_top = screen.blit(column_top, (col1_x,col1_y)) #pygame.draw.rect(screen, BLACK, [col1_x, col1_y, 90, 300], 0)
    col1_bot = screen.blit(column_bot, (col1_x,col1_y+500))
    col2_top = screen.blit(column_top, (col2_x,col2_y))
    col2_bot = screen.blit(column_bot, (col2_x,col2_y+500))
    col3_top = screen.blit(column_top, (col3_x,col3_y))
    col3_bot = screen.blit(column_bot, (col3_x,col3_y+500))
    screen.blit(podloga, (0, 548))

    # score counters gates
    score_gate_1 = pygame.draw.rect(screen, BLUE, [col1_x, col1_y + 300, 1, 200], 0)
    score_gate_2 = pygame.draw.rect(screen, BLUE, [col2_x, col2_y + 300, 1, 200], 0)
    score_gate_3 = pygame.draw.rect(screen, BLUE, [col3_x, col3_y + 300, 1, 200], 0)

    # score counter text
    font = pygame.font.Font("C:/Users/eryko/PycharmProjects/FlappyBird/8-bit Arcade Out.ttf", 72)
    font2 = pygame.font.Font("C:/Users/eryko/PycharmProjects/FlappyBird/8-bit Arcade In.ttf", 72)
    score_display = font.render(f"{score}", True, BLACK)
    score_display2 = font2.render(f"{score}", True, WHITE)
    screen.blit(score_display, (size[0]/2-10, 20))
    screen.blit(score_display2, (size[0] / 2 - 10, 20))

    # drawing the bird and making him fall with gravity
    bird = screen.blit(ptak, (150,bird_y)) #pygame.draw.rect(screen, RED, [150, bird_y, 50, 50], 0)

    score_counter_bird = pygame.draw.rect(screen, BLUE, [150, bird_y, 3, 1], 0)
    bird_y += bird_velocity_y
    bird_velocity_y += 14 / framerate


    if dead == False:
        col1_x -= 4
        col2_x -= 4
        col3_x -= 4

    #restart column position when it gets out of bounds
    if col1_x <= -90:
        col1_x = col3_x + 300
        col1_y = random.randint(-200, 0)
    if col2_x <= -90:
        col2_x = col1_x + 300
        col2_y = random.randint(-200, 0)
    if col3_x <= -90:
        col3_x = col2_x + 300
        col3_y = random.randint(-200, 0)

    # collision detection
    collision = [bird.colliderect(col1_bot), bird.colliderect(col1_top),
                 bird.colliderect(col2_bot), bird.colliderect(col2_top),
                 bird.colliderect(col3_bot), bird.colliderect(col3_top)]

    score_collision = [score_counter_bird.colliderect(score_gate_1),
                       score_counter_bird.colliderect(score_gate_2),
                       score_counter_bird.colliderect(score_gate_3)]

    # die on collision with cols, floor
    add_points()
    you_lost()

    if dead:
        game_over = font.render(f"GAME OVER", True, BLACK)
        game_over1 = font2.render(f"GAME OVER", True, WHITE)
        text_rect = game_over.get_rect(center=(size[0] / 2, size[1] / 2))
        screen.blit(game_over, text_rect)
        screen.blit(game_over1, text_rect)
        wait-=1

        # setup()

    # update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()
    # limit to 60 frames per second
    clock.tick(framerate)
    if wait == 0:
        pygame.display.quit()
        pygame.quit()
        sys.exit()
pygame.quit()

import pygame
import time
import random
import os


# Get the current script's directory
script_dir = os.path.dirname(__file__)

# Constants
SNAKE_SPEED = 15
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

# Initialize pygame
pygame.init()

# Set up the game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# FPS controller
fps = pygame.time.Clock()

# Snake initial position and body
snake_pos = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Load fruit image
# Construct the path to the image using os.path.join
image_path_apple = os.path.join(script_dir, "images", "apple.png")

# Load the image
fruit_image = pygame.image.load(image_path_apple)

fruit_image = pygame.transform.scale(fruit_image, (10, 10))

# Load snake head image

image_path_head = os.path.join(script_dir, "images", "head.png")
snake_head_image = pygame.image.load(image_path_head)

snake_head_image = pygame.transform.scale(snake_head_image, (10, 10))

# Load snake body image
image_path_body = os.path.join(script_dir, "images", "body.png")
snake_body_image = pygame.image.load(image_path_body)
snake_body_image = pygame.transform.scale(snake_body_image, (10, 10))

# Fruit position and spawn flag
fruit_pos = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
             random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
fruit_spawn = True

# Snake direction and change direction
direction = 'RIGHT'
change_to = direction

# Player's score
score = 0

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Function to handle game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is: ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH/2, WINDOW_HEIGHT/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update snake direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    snake_pos[0] += 10 if direction == 'RIGHT' else (
        -10 if direction == 'LEFT' else 0)
    snake_pos[1] += 10 if direction == 'DOWN' else (
        -10 if direction == 'UP' else 0)

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Respawn the fruit
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                     random.randrange(1, (WINDOW_HEIGHT//10)) * 10]

    fruit_spawn = True
    game_window.fill(BLACK)

    # Draw snake
    for i, pos in enumerate(snake_body):
        # Draw snake head using image
        if i == 0:
            game_window.blit(snake_head_image, (pos[0], pos[1]))
        else:
            # Draw snake body using image
            game_window.blit(snake_body_image, (pos[0], pos[1]))
    
    # Draw fruit
    game_window.blit(fruit_image, (fruit_pos[0], fruit_pos[1]))

    # Game over conditions


    # Game over conditions


    # Game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_HEIGHT-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Display score
    show_score(1, WHITE, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second / Refresh Rate
    fps.tick(SNAKE_SPEED)

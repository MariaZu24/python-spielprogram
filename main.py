import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simple Game")

# Set up the player
player_width = 100
player_height = 100
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 5
# Jumping
player_is_jumping = False
player_jump_height = 100
player_jump_speed = 1

def jump():
    global player_y, player_is_jumping
    if not player_is_jumping:
        player_is_jumping = True

def update_player():
    global player_y, player_is_jumping, player_jump_height, player_jump_speed 
    if player_is_jumping:
        player_y -= player_jump_speed
        player_jump_height -= player_jump_speed
        
        if player_jump_height <= 0:
            player_is_jumping = False



# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 0
enemy_speed = 1

huhn_png = pygame.image.load("huhn.png").convert_alpha()

huhn_png = pygame.transform.scale(huhn_png, (player_width, player_height))
huhn_png = pygame.transform.flip(huhn_png, True, False)


# Game loop
running = True
x=50
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # jump
    update_player()
     
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP]:
        jump()

    # Move the enemy
    enemy_y += enemy_speed

    # Check for collision
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        running = False

    # Draw the game
    window.fill((0, 0, 0))

    window.blit(huhn_png, (player_x, player_y))

    #pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, (0, 255, 0), (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.flip()


# Quit the game

pygame.quit()
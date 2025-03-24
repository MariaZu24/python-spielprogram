import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Huhn spiel")

#GROUND_Level = window_height - player_height - 100

background_shift = 0

gravity = 0.5
scroll_speed = 0.5
jump_power = -14

# background music
pygame.mixer.music.load ("game_music.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(1.0)

# egg 
egg_01 = pygame.image.load("egg.png")
egg_01 = pygame.transform.scale(egg_01, (50, 50))

egg_02 = pygame.image.load("egg.png")
egg_02 = pygame.transform.scale(egg_02, (50, 50))


# Sound wenn Huhn getroffen
getroffen = pygame.mixer.Sound('chicken_noise.mp3')


# Set up the player
player_width = 100
player_height = 100

GROUND_Level = window_height - player_height - 100

player_x = window_width // 2 - player_width // 2
player_y = GROUND_Level
player_jump_speed = 5
player_speed = 5



#player_jump_speed = 0
#player_is_jumping = False
#on_ground = False  

#starting-enemy_height = 300

def auf_platform():
    for rect in [(rect1_x, rect1_y, rect1_width, rect1_height),
                 (rect2_x, rect2_y, rect2_width, rect2_height),
                 (rect3_x, rect3_y, rect3_width, rect3_height)]:
        if (player_x + player_width > rect[0] and 
            player_x < rect[0] + rect[2] and
            player_y + player_height >= rect[1] and 
            player_y + player_height <= rect[1] + rect[3]):
            return True
    return False




# Define the rectangles
rect1_x, rect1_y, rect1_width, rect1_height = random.randint(0, window_width - 20), 250, 200, 20
rect2_x, rect2_y, rect2_width, rect2_height = random.randint(0, window_width - 20), 100, 200, 20
rect3_x, rect3_y, rect3_width, rect3_height = random.randint(0, window_width - 20), 380, 200, 20

# Jumping
player_is_jumping = False
player_jump_speed = 0

# Set up the clock
clock = pygame.time.Clock() 

# level of difficulty
font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, (255, 0, 255))
    window.blit(text_surface, (x, y))

def menu():
    global difficulty
    global scroll_speed
    # This is a menu loop
    while True:
        window.fill((0, 0, 0))
        draw_text("select Difficulty", window_width // 2 - 100, window_height // 2 - 100)

        draw_text("Press 1 for easy", window_width // 2 - 100, window_height // 2)
        draw_text("Press 2 for medium", window_width // 2 - 100, window_height // 2 + 50)
        draw_text("Press 3 for hard", window_width // 2 - 100, window_height // 2 + 100)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 1
                    scroll_speed = 0.5
                    enemy_speed = 1
                    return
                if event.key == pygame.K_2:
                    difficulty = 2
                    scroll_speed = 1
                    enemy_speed = 2
                    return
                if event.key == pygame.K_3:
                    difficulty = 3
                    scroll_speed = 3
                    enemy_speed = 3
                    return


def jump():
    global player_y, player_is_jumping , player_jump_speed
    if not player_is_jumping and (player_y >= GROUND_Level or auf_platform()):
        player_is_jumping = True
        player_jump_speed = jump_power

#def update_player():
    #global player_x, player_y, player_is_jumping, player_current_jump_height, player_jump_speed 
    #if player_is_jumping:
     #   player_y -= player_jump_speed
      #  player_current_jump_height += player_jump_speed
       # oben_ist_zu = player_y <= 310 and (player_x > 300 and player_x < 500)
        #if player_current_jump_height <= 0:
         #   player_jump_speed = -player_jump_speed
          #  player_is_jumping = False
        #if (player_current_jump_height >= 200 or oben_ist_zu):
         #   player_jump_speed = -player_jump_speed


def update_player():
    global player_y, player_is_jumping, player_jump_speed

    # Schwerkraft anwenden
    if player_is_jumping:
        player_jump_speed += gravity
    player_y += player_jump_speed

    # Kollision mit Plattformen prüfen
    on_platform = False
    for rect in [(rect1_x, rect1_y, rect1_width, rect1_height),
                 (rect2_x, rect2_y, rect2_width, rect2_height),
                 (rect3_x, rect3_y, rect3_width, rect3_height)]:
        if (player_x < rect[0] + rect[2] and 
            player_x + player_width > rect[0] and
            player_y + player_height >= rect[1] and 
            player_y + player_height <= rect[1] + rect[3] + 5):
            
            player_y = rect[1] - player_height  # Auf Plattform setzen
            player_is_jumping = False
            player_jump_speed = 0  # Fall stoppen
            on_platform = True
            break  # Keine weitere Bewegung mehr prüfen

    # Wenn der Spieler nicht auf einer Plattform ist, Schwerkraft anwenden
    if not on_platform:
        player_is_jumping = True

    # Kollision mit dem Boden
    if player_y >= GROUND_Level:
        player_y = GROUND_Level
        player_is_jumping = False
        player_jump_speed = 0


#sed up egg
egg_width = 50
egg_height = 50
egg_x = random.randint(0, window_width - egg_width)
egg_y = 0
egg_speed = 1

egg02_width = 50
egg02_height = 50
egg02_x = random.randint(0, window_width - egg_width)
egg02_y = 0
egg02_speed = 1

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 0
enemy_speed = 1

enemy02_width = 50
enemy02_height = 50
enemy02_x = random.randint(0, window_width - enemy_width)
enemy02_y = 0
enemy02_speed = 1


huhn_png = pygame.image.load("huhn.png").convert_alpha()
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (window_width, window_height))

huhn_png = pygame.transform.scale(huhn_png, (player_width, player_height))
huhn_png = pygame.transform.flip(huhn_png, True, False)

# Show menu splash screen
menu()

def game_over():
    window.fill((0, 0, 0))
    # Draw "Game Over" text with larger font and cool effects
    large_font = pygame.font.Font(None, 72)
    game_over_surface = large_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect(center=(window_width // 2, window_height // 2 - 50))
    
    # Add shadow effect
    shadow_surface = large_font.render("Game Over", True, (0, 0, 0))
    shadow_rect = shadow_surface.get_rect(center=(window_width // 2 + 5, window_height // 2 - 45))
    
    window.blit(shadow_surface, shadow_rect)
    window.blit(game_over_surface, game_over_rect)
    draw_text("Press any key to exit", window_width // 2 - 150, window_height // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Main Game loop
running = True
egg_counter = 0

while running:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        
    
     # Rechtecke nach links bewegen
    rect1_x -= scroll_speed
    rect2_x -= scroll_speed
    rect3_x -= scroll_speed

    # Rechtecke zurücksetzen, wenn sie den Bildschirm verlassen
    if rect1_x + rect1_width < 0:
        rect1_x = window_width
        rect1_y = random.randint(0, window_height - 20)
    if rect2_x + rect2_width < 0:
        rect2_x = window_width
        rect2_y = random.randint(0, window_height - 20)
    if rect3_x + rect3_width < 0:
        rect3_x = window_width
        rect3_y = random.randint(0, window_height - 20)
       

    # jump
    update_player()
     
    # Spieler bewegen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP]:
        jump()



    # Move the enemy
    enemy_y += enemy_speed
    if (enemy_y > (window_height-20)):
        enemy_y = 0
        enemy_x = random.randint(0, window_width - enemy_width)
    enemy02_y += enemy02_speed
    if (enemy_y > (window_height - 20)):
        enemy_y = 0
        enemy_x = random.randint(0, window_width - enemy_width)
    egg_y += egg_speed
    if (egg_y > (window_height - 20)):
        egg_y = 0
        egg_x = random.randint(0, window_width - egg_width)
    egg02_y += egg02_speed
    if (egg02_y > (window_height - 20)):    
        egg02_y = 0
        egg02_x = random.randint(0, window_width - egg02_width)

    # Check for collision
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        running = False
        game_over()

    if player_x < enemy02_x + enemy02_width and player_x + player_width > enemy02_x and player_y < enemy02_y + enemy02_height and player_y + player_height > enemy02_y:
        running = False
        game_over()

    # Check for collision with egg
    if player_x < egg_x + egg_width and player_x + player_width > egg_x and player_y < egg_y + egg_height and player_y + player_height > egg_y:
        egg_y = 0
        egg_x = random.randint(0, window_width - egg_width)
        egg_speed += 0.5
        egg_counter+=1

    if player_x < egg02_x + egg02_width and player_x + player_width > egg02_x and player_y < egg02_y + egg02_height and player_y + player_height > egg02_y:
        egg02_y = 0
        egg02_x = random.randint(0, window_width - egg02_width)
        egg02_speed += 0.5
        egg_counter+=1
        # Perform any additional actions when the egg is collected
        # For example, increase the player's score or play a sound effect


    # Draw the game
    window.blit(background, (0 - background_shift, 0))
    window.blit(background, (window_width - background_shift, 0))
    background_shift += scroll_speed
    if background_shift >= window_width:  # Corrected condition
        background_shift = 0

    # Rectangle01
    pygame.draw.rect(window, (102, 51, 0), (rect1_x, rect1_y, rect1_width, rect1_height))
    window.blit(huhn_png, (player_x, player_y))
    
    
     # Rectangle02
    pygame.draw.rect(window, (102, 51, 0), (rect2_x, rect2_y, rect2_width, rect2_height))
    window.blit(huhn_png, (player_x, player_y))

     # Rectangle03
    pygame.draw.rect(window, (102, 51, 0), (rect3_x, rect3_y, rect3_width, rect3_height))
    window.blit(huhn_png, (player_x, player_y))

    # Draw the eggs
    window.blit(egg_01, (egg_x, egg_y))
    window.blit(egg_02, (egg02_x, egg02_y))

    # Draw a counter of the eggs on the screen
    draw_text(f"Eggs: {egg_counter}", 10, 10)

    #pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.circle(window, (204, 0, 0), (enemy_x + enemy_width // 2, enemy_y + enemy_height // 2), 30)
    pygame.draw.circle(window, (204, 0, 0), (enemy02_x + enemy02_width // 2, enemy02_y + enemy02_height // 2), 30)
    pygame.display.flip()


# Quit the game

pygame.quit()
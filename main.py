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
                    return
                if event.key == pygame.K_2:
                    difficulty = 2
                    scroll_speed = 1
                    return
                if event.key == pygame.K_3:
                    difficulty = 3
                    scroll_speed = 3
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
            return  # Keine weitere Bewegung mehr prüfen

    # Kollision mit dem Boden
    if player_y >= GROUND_Level:
        player_y = GROUND_Level
        player_is_jumping = False
        player_jump_speed = 0






# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 0
enemy_speed = 1

huhn_png = pygame.image.load("huhn.png").convert_alpha()
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (window_width, window_height))

huhn_png = pygame.transform.scale(huhn_png, (player_width, player_height))
huhn_png = pygame.transform.flip(huhn_png, True, False)

# Show menu splash screen
menu()

# Main Game loop
running = True

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
     
    # Move the player
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT] and player_x > 0:
     #   player_x > 0:
      #  background_shift -= 0.8
    #if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
    #    player_x += player_speed
    #if keys[pygame.K_UP]:
    #    jump()

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

               # if kollisionskontrolle(kugelX-30,kugelY-25,gegnerX[durchgang], gegnerY[durchgang]) == True:
                # Kugel hat getroffen
                # print("Kugel hat getroffen")
               # pygame.mixer.Sound.play(getroffen)



    # Check for collision
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        running = False

    # Draw the game
    window.blit(background, (0-background_shift, 0))
    window.blit(background, (window_width-background_shift, 0))
    background_shift -= scroll_speed
    if background_shift <= window_width:
        background_shift = 0
    # Rectangle01
    pygame.draw.rect(window, (102, 51, 0), (rect1_x, rect1_y, rect1_width, rect1_height))
    window.blit(huhn_png, (player_x, player_y))
    draw_text(f"Jumping {player_is_jumping} x:{player_x} y:{player_y}", 0,0)
    draw_text(f"Jump Height", 0,50)
    
     # Rectangle02
    pygame.draw.rect(window, (102, 51, 0), (rect2_x, rect2_y, rect2_width, rect2_height))
    window.blit(huhn_png, (player_x, player_y))

     # Rectangle03
    pygame.draw.rect(window, (102, 51, 0), (rect3_x, rect3_y, rect3_width, rect3_height))
    window.blit(huhn_png, (player_x, player_y))

    #pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, (0, 255, 0), (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.flip()


# Quit the game

pygame.quit()
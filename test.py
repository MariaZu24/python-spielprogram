import pygame

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Spielerparameter
player_width = 50
player_height = 50
player_x = window_width // 2
player_y = window_height - player_height - 100
player_velocity_y = 0
gravity = 0.5

# Bodenhöhe
ground_level = window_height - player_height - 100

# Hauptspiel-Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Sprunglogik
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_y >= ground_level:
            player_velocity_y = -10  # Negativer Wert für den Sprung nach oben

    # Schwerkraft anwenden
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Kollisionslogik mit dem Boden
    if player_y >= ground_level:
        player_y = ground_level
        player_velocity_y = 0

    # Zeichnen des Spiels
    window.fill((0, 0, 0))  # Hintergrund schwarz
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))  # Spieler zeichnen
    pygame.display.flip()

pygame.quit()
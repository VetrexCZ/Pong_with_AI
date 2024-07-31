# Python Pong Game !

import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení herního okna
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game") # Název Okna

# Nahrani zvukoveho souboru
collision_sound = pygame.mixer.Sound("Internet_projects\\Pong_with_AI\\event.mp3")
collision_sound2 = pygame.mixer.Sound("Internet_projects\\Pong_with_AI\\event2.mp3")

# Barvy
white = (255, 255, 255)
black = (0, 0, 0)

# Velikost a pozice hráčů a mičku
player_width, player_height = 15, 100
ball_size = 20

# X levý hráč
# Y pravý hráč
player1_x, player1_y = 50, height // 2 - player_height // 2 
player2_x, player2_y = width - 50 - player_width, height // 2 - player_height // 2

ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 5, 5 # Rychlost ve směru osy x a y

# Funkce pro umelou inteligenci
def artificial_intelligence(ball_y, player1_y):
    if ball_y < player1_y + player_height // 2:
        return -5   # Pohyb nahoru
    elif ball_y > player1_y + player_height // 2:
        return 5    # Pohyb dolu
    else:
        return 0    # Zustane na miste

# Herní smyčka
clock = pygame.time.Clock()

# Tlačítko pro zavření okna
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ovládání pomoci klávesnice
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5 # Velikost posunu
    if keys[pygame.K_DOWN] and player2_y < height - player_height:
        player2_y += 5

    # Umela inteligence pro prvniho hrace (levy hrac)
    ai_movement = artificial_intelligence(ball_y, player1_y)
    player1_y += ai_movement
    
    # Pohyb míčku
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Obbití míčku od hráču
    if (
        (player1_x < ball_x < player1_x + player_width)
        and (player1_y < ball_y < player1_y + player_height)
    ):
        ball_speed_x = abs(ball_speed_x)
        collision_sound.play() # Prehraje zvuk pri detekci kolize
    
    if (
        (player2_x < ball_x < player2_x + player_width)
        and (player2_y < ball_y < player2_y + player_height)
    ):
        ball_speed_x = -abs(ball_speed_x)
        collision_sound.play() # Prehraje zvuk pri detekci kolize

    # Odbití míčku od stěn
    if ball_y < 0 or ball_y > height - ball_size:
        ball_speed_y *= -1
        collision_sound2.play() # Prehraje zvuk pri detekci horni a dolni steny

    # Kontrola vítězství
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
    
    # Vykreslení herního pole
    win.fill(black)
    pygame.draw.rect(win, white, (player1_x, player1_y, player_width, player_height ))
    pygame.draw.rect(win, white, (player2_x, player2_y, player_width, player_height ))
    pygame.draw.ellipse(win, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.update() # Aktualizace změn
    clock.tick(75) # FPS
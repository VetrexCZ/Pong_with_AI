# Python Pong Game !

import pygame
import sys

# Initializing Pygame
pygame.init()

# Setting game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game") # Displayet window name

# Upload saved sounds
collision_sound = pygame.mixer.Sound("Internet_projects\\Pong_with_AI\\event.mp3")
collision_sound2 = pygame.mixer.Sound("Internet_projects\\Pong_with_AI\\event2.mp3")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Size and placement of players and ball
player_width, player_height = 15, 100
ball_size = 20

# X stands for left player (AI)
# Y stands for right player (human)
player1_x, player1_y = 50, height // 2 - player_height // 2 
player2_x, player2_y = width - 50 - player_width, height // 2 - player_height // 2

ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 5, 5 # Ball speed on axis x and y

# Simple function for AI
def artificial_intelligence(ball_y, player1_y):
    if ball_y < player1_y + player_height // 2:
        return -5   # Up direction
    elif ball_y > player1_y + player_height // 2:
        return 5    # Down direction
    else:
        return 0    # Stays in place

# Game loop
clock = pygame.time.Clock()

# Button for close a window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player keyboard control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5 # Shift size
    if keys[pygame.K_DOWN] and player2_y < height - player_height:
        player2_y += 5

    # AI stands for first player (left player)
    ai_movement = artificial_intelligence(ball_y, player1_y)
    player1_y += ai_movement
    
    # Ball move
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball bounce from players
    if (
        (player1_x < ball_x < player1_x + player_width)
        and (player1_y < ball_y < player1_y + player_height)
    ):
        ball_speed_x = abs(ball_speed_x)
        collision_sound.play() # Play sound if detects impact with player
    
    if (
        (player2_x < ball_x < player2_x + player_width)
        and (player2_y < ball_y < player2_y + player_height)
    ):
        ball_speed_x = -abs(ball_speed_x)
        collision_sound.play() # Play sound if detects impact with player

    # Ball bounce from upper and bottom wall
    if ball_y < 0 or ball_y > height - ball_size:
        ball_speed_y *= -1
        collision_sound2.play() # Play sound if detects impact with upper and bottom wall

    # Win control
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
    
    # Game zone rendering
    win.fill(black)
    pygame.draw.rect(win, white, (player1_x, player1_y, player_width, player_height ))
    pygame.draw.rect(win, white, (player2_x, player2_y, player_width, player_height ))
    pygame.draw.ellipse(win, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.update() # Update change
    clock.tick(75) # Frames per seconds
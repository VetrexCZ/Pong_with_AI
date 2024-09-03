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

# Ball position
ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 7, 7
max_ball_speed = 10 # Ball speed

# Simple function for AI
def artificial_intelligence(ball_y, player1_y):
    if ball_y < player1_y + player_height // 2 and player1_y > 0:
        return -6   # Up direction
    elif ball_y > player1_y + player_height // 2 and player1_y < height - player_height:
        return 6    # Down direction
    return 0    # No movement

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
        player2_y -= 7 # Shift size
    if keys[pygame.K_DOWN] and player2_y < height - player_height:
        player2_y += 7

    # AI stands for first player (left player)
    ai_movement = artificial_intelligence(ball_y, player1_y)
    player1_y += ai_movement
    
    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball and paddle collision
    player1_rect = pygame.Rect(player1_x, player1_y, player_width, player_height)
    player2_rect = pygame.Rect(player2_x, player2_y, player_width, player_height)
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

    if player1_rect.colliderect(ball_rect):
        ball_speed_x = abs(ball_speed_x)
        collision_sound.play() # Play sound if detects impact with player
    
    if player2_rect.colliderect(ball_rect):
        ball_speed_x = -abs(ball_speed_x)
        collision_sound.play() # Play sound if detects impact with player

    # Ball and wall collision
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1
        collision_sound2.play() # Play sound if detects impact with upper and bottom wall

    # Scoring system: reset ball
    if ball_x <= 0 or ball_x >= width:
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x *= -1 # Change direction
    
    # Game zone rendering
    win.fill(black)
    pygame.draw.rect(win, white, player1_rect)
    pygame.draw.rect(win, white, player2_rect)
    pygame.draw.ellipse(win, white, ball_rect)

    pygame.display.flip() # Update display
    clock.tick(75) # Frames per seconds
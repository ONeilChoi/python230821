import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLS = 10
BLOCK_GAP = 5
BALL_SPEED = 5
PADDLE_SPEED = 8

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")

# Initialize paddle and ball
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = BALL_SPEED
ball_speed_y = -BALL_SPEED

# Create blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * (BLOCK_WIDTH + BLOCK_GAP), row * (BLOCK_HEIGHT + BLOCK_GAP), BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # Collision with blocks
    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.circle(screen, RED, ball.center, BALL_RADIUS)

    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

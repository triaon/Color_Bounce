import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (12, 18, 4)
GRAY = (200, 200, 200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Bounce")
grid = [[GRAY for _ in range(WIDTH // GRID_SIZE)] for _ in range(HEIGHT // GRID_SIZE)]
for y in range(len(grid)):
    for x in range(len(grid[0]) // 2):
        grid[y][x] = WHITE
    for x in range(len(grid[0]) // 2, len(grid[0])):
        grid[y][x] = BLACK
ball_radius = 12
ball_white = pygame.Rect(WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_black = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_white_speed = [random.choice([-10, 10]), random.choice([-10, 10])]
ball_black_speed = [random.choice([-10, 10]), random.choice([-10, 10])]
def handle_collision(ball, ball_speed, color):
    grid_x = min(max(ball.centerx // GRID_SIZE, 0), len(grid[0]) - 1)
    grid_y = min(max(ball.centery // GRID_SIZE, 0), len(grid) - 1)
    if grid[grid_y][grid_x] != color:
        dx = ball.centerx - grid_x * GRID_SIZE - GRID_SIZE / 2
        dy = ball.centery - grid_y * GRID_SIZE - GRID_SIZE / 2
        angle = math.atan2(dy, dx) + random.choice((-0.1,0.1))
        speed = math.sqrt(ball_speed[0] ** 2 + ball_speed[1] ** 2)
        ball_speed[0] = speed * math.cos(2 * angle) * -1
        ball_speed[1] = speed * math.sin(2 * angle) * -1
        grid[grid_y][grid_x] = color
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_white = ball_white.move(ball_white_speed)
    ball_black = ball_black.move(ball_black_speed)
    handle_collision(ball_white, ball_white_speed, WHITE)
    handle_collision(ball_black, ball_black_speed, BLACK)
    if ball_white.left < 0 or ball_white.right > WIDTH:
        ball_white_speed[0] *= -1
    if ball_white.top < 0 or ball_white.bottom > HEIGHT:
        ball_white_speed[1] *= -1
    if ball_black.left < 0 or ball_black.right > WIDTH:
        ball_black_speed[0] *= -1
    if ball_black.top < 0 or ball_black.bottom > HEIGHT:
        ball_black_speed[1] *= -1
    screen.fill(GRAY)
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.circle(screen, BLACK, ball_white.center, ball_radius)
    pygame.draw.circle(screen, WHITE, ball_black.center, ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(100)
pygame.quit()

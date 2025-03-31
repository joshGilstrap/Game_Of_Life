import pygame
import random
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def create_grid():
    grid = [[random.randint(0, 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    return grid

def draw_grid(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, random.choice(COLORS), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            else:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid():
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = grid[y][x]
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_x = x + i
            neighbor_y = y + j
            if 0 <= neighbor_x < GRID_WIDTH and 0 <= neighbor_y < GRID_HEIGHT:
                count += grid[neighbor_y][neighbor_x]
    return count

grid = create_grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    screen.fill(BLACK)
    draw_grid(grid)
    grid = update_grid()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
import pygame
import random
from statistics import mean, median, mode

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 300
screen_height = 300
tile_size = 100

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sliding Tiles Puzzle")

# Font
font = pygame.font.Font(None, 36)

# Initialize tiles
tiles = [random.randint(1, 9) for _ in range(3)]
positions = [(i * tile_size, 0) for i in range(3)]


def draw_tiles():
    screen.fill(white)
    for i, tile in enumerate(tiles):
        pygame.draw.rect(screen, blue, (positions[i][0], positions[i][1], tile_size, tile_size))
        text = font.render(str(tile), True, white)
        screen.blit(text, (positions[i][0] + tile_size // 2 - 10, positions[i][1] + tile_size // 2 - 10))

    pygame.display.flip()


def calculate_stats():
    try:
        tile_me

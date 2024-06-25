import pygame

# Bildschirmgröße und Kachelgröße
TILE_SIZE = 32
WIDTH, HEIGHT = 20 * TILE_SIZE, 15 * TILE_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farmspiel")

# Schriftart
pygame.font.init()
FONT = pygame.font.SysFont(None, 24)

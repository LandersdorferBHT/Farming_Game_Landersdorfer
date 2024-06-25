import pygame
from config import TILE_SIZE, SCREEN

def draw_player(player_pos):
    PLAYER_SPRITE = pygame.image.load("textures/player.png").convert_alpha()
    PLAYER_SPRITE = pygame.transform.scale(PLAYER_SPRITE, (TILE_SIZE, TILE_SIZE))
    SCREEN.blit(PLAYER_SPRITE, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))


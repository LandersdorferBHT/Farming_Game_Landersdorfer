import pygame
from config import TILE_SIZE, SCREEN


# Creates Player Texture and Scales it to the Tile Size
def draw_player(player_pos):
    player_sprite = pygame.image.load("textures/player.png").convert_alpha()
    player_sprite = pygame.transform.scale(player_sprite, (TILE_SIZE, TILE_SIZE))
    SCREEN.blit(player_sprite, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

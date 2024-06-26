import pygame

sprite_sheet = pygame.image.load("textures/village_assets.png").convert_alpha()


def get_asset(x, y, width, height):
    asset = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    asset.blit(sprite_sheet, (0, 0), (x, y, width, height))
    return asset

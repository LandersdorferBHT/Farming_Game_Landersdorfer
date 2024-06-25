import pygame
from config import SCREEN, TILE_SIZE


def initialize_map():
    map_layout = [['' for _ in range(20)] for _ in range(15)]
    field_status = {}

    # Farmhaus platzieren
    farmhouse_pos = (9, 6)
    map_layout[farmhouse_pos[1]][farmhouse_pos[0]] = 'F'

    # Weg um das Farmhaus
    for i in range(4):
        map_layout[4][7 + i] = 'V'
        map_layout[8][7 + i] = 'V'
    for i in range(5):
        map_layout[4 + i][7] = 'V'
        map_layout[4 + i][11] = 'V'

    # Felder um das Farmhaus in einem Grid anordnen
    field_one = [(13, 1), (12, 1), (11, 1), (13, 2), (12, 2), (11, 2), (13, 3), (12, 3), (11, 3)]
    for pos in field_one:
        map_layout[pos[0]][pos[1]] = 'T'
        field_status[pos[1], pos[0]] = 'plowed'

    field_two = [(13, 5), (12, 5), (11, 5), (13, 6), (12, 6), (11, 6), (13, 7), (12, 7), (11, 7)]
    for pos in field_two:
        map_layout[pos[0]][pos[1]] = 'T'
        field_status[pos[1], pos[0]] = 'plowed'

    field_three = [(13, 9), (12, 9), (11, 9), (13, 10), (12, 10), (11, 10), (13, 11), (12, 11), (11, 11)]
    for pos in field_three:
        map_layout[pos[0]][pos[1]] = 'T'
        field_status[pos[1], pos[0]] = 'plowed'

    # Large Field
    # fieldGridFiveStart = (14, 1)
    for x in range(5):
        for y in range(9):
            map_layout[1 + y][14 + x] = 'T'
            field_status[(14 + x, 1 + y)] = 'plowed'

    # Marktstand platzieren und Pfad erzeugen
    market_pos = (1, 1)
    map_layout[market_pos[1]][market_pos[0]] = 'M'

    path_to_market = [(3, 1), (3, 2), (3, 3), (4, 3), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (7, 6)] # (7, 6)
    for pos in path_to_market:
        map_layout[pos[1]][pos[0]] = 'P'

    # Bäume am Rand und als nicht betretbar markieren
    for x in range(20):
        map_layout[0][x] = 'B'
        map_layout[14][x] = 'B'
    for y in range(15):
        map_layout[y][0] = 'B'
        map_layout[y][19] = 'B'

    return map_layout, field_status

# Trying with Textures

FARMHOUSE = pygame.image.load("textures/farmhouse.png").convert_alpha()
FARMHOUSE = pygame.transform.scale(FARMHOUSE, (TILE_SIZE, TILE_SIZE))

PATH = pygame.image.load("textures/path.png").convert_alpha()
PATH = pygame.transform.scale(PATH, (TILE_SIZE, TILE_SIZE))

FIELD_PLOWED = pygame.image.load("textures/dirt.png").convert_alpha()
FIELD_PLOWED = pygame.transform.scale(FIELD_PLOWED, (TILE_SIZE, TILE_SIZE))

TREE = pygame.image.load("textures/tree.png").convert_alpha()
TREE = pygame.transform.scale(TREE, (TILE_SIZE, TILE_SIZE))

GRASS = pygame.image.load("textures/grass.png").convert_alpha()
GRASS = pygame.transform.scale(GRASS, (TILE_SIZE, TILE_SIZE))

MARKET = pygame.image.load("textures/market.png").convert_alpha()
MARKET = pygame.transform.scale(MARKET, (TILE_SIZE, TILE_SIZE))

BUSH = pygame.image.load("textures/bush.png").convert_alpha()
BUSH = pygame.transform.scale(BUSH, (TILE_SIZE, TILE_SIZE))

def draw_map(map_layout, field_status):

    for y in range(15):
        for x in range(20):
            SCREEN.blit(GRASS, (x * TILE_SIZE, y * TILE_SIZE))


            if map_layout[y][x] == 'F':
                SCREEN.blit(FARMHOUSE, (x * TILE_SIZE, y * TILE_SIZE))

            elif map_layout[y][x] == 'P':
                SCREEN.blit(PATH, (x * TILE_SIZE, y * TILE_SIZE))

            elif map_layout[y][x] == 'T':
                field_state = field_status.get((x, y), 'plowed')

                if isinstance(field_state, tuple):
                    crop_type = field_state[1]
                    field_state = field_state[0]
                else:
                    crop_type = None

                if field_state == 'plowed':
                    SCREEN.blit(FIELD_PLOWED, (x * TILE_SIZE, y * TILE_SIZE))

                elif field_state == 'planted' and crop_type:
                    SCREEN.blit(FIELD_PLOWED, (x * TILE_SIZE, y * TILE_SIZE))

                    sprout_x = x * TILE_SIZE + (TILE_SIZE - crop_type.sprout_texture.get_width()) // 2
                    sprout_y = y * TILE_SIZE + (TILE_SIZE - crop_type.sprout_texture.get_height()) // 2
                    SCREEN.blit(crop_type.sprout_texture, (sprout_x, sprout_y))

                elif field_state == 'harvestable' and crop_type:
                    SCREEN.blit(FIELD_PLOWED, (x * TILE_SIZE, y * TILE_SIZE))

                    harvestable_x = x * TILE_SIZE + (TILE_SIZE - crop_type.harvestable_texture.get_width()) // 2
                    harvestable_y = y * TILE_SIZE + (TILE_SIZE - crop_type.harvestable_texture.get_height()) // 2

                    SCREEN.blit(crop_type.harvestable_texture, (harvestable_x, harvestable_y))

                elif field_state == 'harvested':
                    SCREEN.blit(crop_type.harvested_texture, (x * TILE_SIZE, y * TILE_SIZE))

            elif map_layout[y][x] == 'M':
                SCREEN.blit(MARKET, (x * TILE_SIZE, y * TILE_SIZE))

            elif map_layout[y][x] == 'B':
                SCREEN.blit(TREE, (x * TILE_SIZE, y * TILE_SIZE))

            elif map_layout[y][x] == 'V':
                SCREEN.blit(BUSH, (x * TILE_SIZE, y * TILE_SIZE))

            else:
                SCREEN.blit(GRASS, (x * TILE_SIZE, y * TILE_SIZE))
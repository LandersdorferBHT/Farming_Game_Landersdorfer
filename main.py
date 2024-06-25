import pygame
import sys
import time
from config import SCREEN
from map import initialize_map, draw_map
from player import draw_player
from hud import draw_hud, draw_field_info
from field import update_field_growth
from fruits import fruits

# Initializes Pygame
pygame.init()

# Initializes Map and Player
map_layout, field_status = initialize_map()
field_timers = {}
player_pos = [10, 7]

# Initializes Player Inventory and Account Balance
inventory = {'seeds': 10, 'harvested_produce': 0}
account_balance = 0.0

# Selected Crop Type
selected_fruit = fruits[0]

# Main Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Movement with Arrow Keys
        # Also makes sure that the Player can't run through Trees
        elif event.type == pygame.KEYDOWN:

            # Behaviour for Arrow Key Left
            if event.key == pygame.K_LEFT and player_pos[0] > 0 and map_layout[player_pos[1]][player_pos[0] - 1] != 'B':
                player_pos[0] -= 1

            # Behaviour Arrow Key Right
            elif event.key == pygame.K_RIGHT and player_pos[0] < 19 and map_layout[player_pos[1]][player_pos[0] + 1] != 'B':
                player_pos[0] += 1

            # Behaviour Arrow Key Up
            elif event.key == pygame.K_UP and player_pos[1] > 0 and map_layout[player_pos[1] - 1][player_pos[0]] != 'B':
                player_pos[1] -= 1

            # Behaviour Arrow Key Down
            elif event.key == pygame.K_DOWN and player_pos[1] < 14 and map_layout[player_pos[1] + 1][player_pos[0]] != 'B':
                player_pos[1] += 1

            # All Field Work is done with the Spacebar
            elif event.key == pygame.K_SPACE:

                # Get Players Position
                player_tile = (player_pos[0], player_pos[1])

                if map_layout[player_tile[1]][player_tile[0]] == 'T':
                    current_status = field_status.get(player_tile)

                    # Plants Selected Crop when Field is 'plowed' and there's at least 1 Seed in the Inventory
                    if current_status == 'plowed' and inventory['seeds'] > 0:
                        field_status[player_tile] = ('planted', selected_fruit)

                        # Starts Growth Timer for Crop
                        field_timers[player_tile] = time.time()

                        inventory['seeds'] -= 1

                    # Harvests Field and will add Crop to Inventory
                    elif current_status and current_status[0] == 'harvestable':
                        field_status[player_tile] = ('harvested', current_status[1])
                        inventory['harvested_produce'] += 1

                    # Plows the Harvested Field
                    elif current_status and current_status[0] == 'harvested':
                        field_status[player_tile] = 'plowed'

                    # Default Status is 'plowed'
                    elif not current_status:
                        field_status[player_tile] = 'plowed'

            # Behaviour for Key V
            elif event.key == pygame.K_v:

                # Sells Harvested Crops on the Market
                if map_layout[player_pos[1]][player_pos[0]] == 'M' and inventory['harvested_produce'] > 0:
                    account_balance += inventory['harvested_produce'] * 0.2
                    inventory['harvested_produce'] = 0

            # Behaviour for Key B
            elif event.key == pygame.K_b:

                # Buys Seeds on the Market
                if map_layout[player_pos[1]][player_pos[0]] == 'M' and account_balance >= 0.2:
                    inventory['seeds'] += 1
                    account_balance -= 0.15

            # Behaviour for Key F
            elif event.key == pygame.K_f:

                # Selects next Crop from List, First is Barley
                selected_fruit = fruits[(fruits.index(selected_fruit) + 1) % len(fruits)]

    # Update Plant Growth
    update_field_growth(field_timers, field_status)

    SCREEN.fill((0, 0, 0))
    draw_map(map_layout, field_status)
    draw_player(player_pos)

    # Shows HUD for Player Stats and Field Info
    draw_hud(inventory, account_balance, selected_fruit)
    draw_field_info(field_status, tuple(player_pos))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

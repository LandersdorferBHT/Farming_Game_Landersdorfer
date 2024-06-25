import pygame
import sys
import time
from config import SCREEN
from map import initialize_map, draw_map
from player import draw_player
from hud import draw_hud, draw_field_info
from field import update_field_growth
from fruits import fruits

# Initialisiere Pygame
pygame.init()

# Initialisiere die Karte und den Spieler
map_layout, field_status = initialize_map()
field_timers = {}
player_pos = [10, 7]

# Spielerinventar und Kontostand
inventory = {'seeds': 10, 'harvested_produce': 0}
account_balance = 0.0

# Aktuell ausgewählte Frucht
selected_fruit = fruits[0]

# Hauptspiel-Schleife
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_pos[0] > 0 and map_layout[player_pos[1]][player_pos[0] - 1] != 'B':
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and player_pos[0] < 19 and map_layout[player_pos[1]][player_pos[0] + 1] != 'B':
                player_pos[0] += 1
            elif event.key == pygame.K_UP and player_pos[1] > 0 and map_layout[player_pos[1] - 1][player_pos[0]] != 'B':
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and player_pos[1] < 14 and map_layout[player_pos[1] + 1][player_pos[0]] != 'B':
                player_pos[1] += 1
            elif event.key == pygame.K_SPACE:
                # Feldbearbeitung
                player_tile = (player_pos[0], player_pos[1])
                if map_layout[player_tile[1]][player_tile[0]] == 'T':
                    current_status = field_status.get(player_tile)
                    if current_status == 'plowed' and inventory['seeds'] > 0:
                        field_status[player_tile] = ('planted', selected_fruit)
                        field_timers[player_tile] = time.time()
                        inventory['seeds'] -= 1
                    elif current_status and current_status[0] == 'harvestable':
                        field_status[player_tile] = ('harvested', current_status[1])
                        inventory['harvested_produce'] += 1
                    elif current_status and current_status[0] == 'harvested':
                        field_status[player_tile] = 'plowed'
                    elif not current_status:
                        field_status[player_tile] = 'plowed'
            elif event.key == pygame.K_v:
                # Verkauf von Erzeugnissen
                if map_layout[player_pos[1]][player_pos[0]] == 'M' and inventory['harvested_produce'] > 0:
                    account_balance += inventory['harvested_produce'] * 0.2  # Jeder Ertrag bringt 10 Cent
                    inventory['harvested_produce'] = 0
            elif event.key == pygame.K_b:
                # Kauf von Samen
                if map_layout[player_pos[1]][player_pos[0]] == 'M' and account_balance >= 0.2:
                    inventory['seeds'] += 1
                    account_balance -= 0.15  # Jeder Samen kostet 20 Cent
            elif event.key == pygame.K_f:
                # Fruchtart auswählen
                selected_fruit = fruits[(fruits.index(selected_fruit) + 1) % len(fruits)]
                print(f"Ausgewählte Frucht: {selected_fruit.name}")

    # Aktualisiere das Pflanzenwachstum
    update_field_growth(field_timers, field_status)

    SCREEN.fill((0, 0, 0))
    draw_map(map_layout, field_status)
    draw_player(player_pos)

    draw_hud(inventory, account_balance, selected_fruit)
    draw_field_info(field_status, tuple(player_pos))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

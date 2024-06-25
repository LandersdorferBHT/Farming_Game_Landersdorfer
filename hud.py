from config import FONT, SCREEN, WIDTH


# Function to Draw Player HUD (Inventory, Account Balance, Selected Crop)
def draw_hud(inventory, account_balance, selected_fruit):
    seeds_text = FONT.render(f'Samen: {inventory["seeds"]}', True, (255, 255, 255))
    produce_text = FONT.render(f'Erzeugnisse: {inventory["harvested_produce"]}', True, (255, 255, 255))
    balance_text = FONT.render(f'Kontostand: {account_balance:.2f}€', True, (255, 255, 255))
    fruit_text = FONT.render(f'Frucht: {selected_fruit.name}', True, (255, 255, 255))

    SCREEN.blit(seeds_text, (30, 250))
    SCREEN.blit(produce_text, (30, 275))
    SCREEN.blit(balance_text, (30, 300))
    SCREEN.blit(fruit_text, (30, 325))


# Function to Draw Field Info HUD (Field Status, Planted Crop)
def draw_field_info(field_status, player_pos):
    field_info_text = "Feldstatus: "
    crop_info_text = "Angebaute Fruchtart: "

    if player_pos in field_status:
        field_state = field_status[player_pos]
        if isinstance(field_state, tuple):
            field_info_text += field_state[0]
            crop_info_text += field_state[1].name
        else:
            field_info_text += field_state
            crop_info_text += "Keine"
    else:
        field_info_text += "Nicht verfügbar"
        crop_info_text += "Keine"

    field_info_render = FONT.render(field_info_text, True, (255, 255, 255))
    crop_info_render = FONT.render(crop_info_text, True, (255, 255, 255))

    SCREEN.blit(field_info_render, (WIDTH - 250, 400))
    SCREEN.blit(crop_info_render, (WIDTH - 250, 425))



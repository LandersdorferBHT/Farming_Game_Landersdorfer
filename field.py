import time

def update_field_growth(field_timers, field_status):
    growth_time = 10  # Zeit bis zur Ernte in Sekunden
    current_time = time.time()
    for tile, start_time in list(field_timers.items()):
        elapsed_time = current_time - start_time
        if elapsed_time > growth_time:
            field_state = field_status.get(tile)
            if isinstance(field_state, tuple) and field_state[0] == 'planted':
                field_status[tile] = ('harvestable', field_state[1])
                del field_timers[tile]

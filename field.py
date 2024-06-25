import time


# Function to Update the Growth Status per Field
def update_field_growth(field_timers, field_status):

    # Growth Time of 10 Seconds per Crop
    growth_time = 10
    current_time = time.time()

    # Set Field Status to 'harvestable' after 10 Seconds
    for tile, start_time in list(field_timers.items()):
        elapsed_time = current_time - start_time
        if elapsed_time > growth_time:
            field_state = field_status.get(tile)
            if isinstance(field_state, tuple) and field_state[0] == 'planted':
                field_status[tile] = ('harvestable', field_state[1])
                del field_timers[tile]

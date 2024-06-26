import pygame
from config import TILE_SIZE


# Fruit Class, to Create Crops with Name and Textures
class Fruit:
    def __init__(self, name, sprout_texture, harvestable_texture, harvested_texture):
        self.name = name
        self.sprout_texture = sprout_texture
        self.harvestable_texture = harvestable_texture
        self.harvested_texture = harvested_texture

        # Load and Scale Textures
        self.sprout_texture = pygame.image.load(self.sprout_texture).convert_alpha()
        self.sprout_texture = pygame.transform.scale(self.sprout_texture, (TILE_SIZE / 2, TILE_SIZE / 2))

        self.harvestable_texture = pygame.image.load(self.harvestable_texture).convert_alpha()
        self.harvestable_texture = pygame.transform.scale(self.harvestable_texture, (TILE_SIZE / 2, TILE_SIZE / 2))

        self.harvested_texture = pygame.image.load(self.harvested_texture).convert_alpha()
        self.harvested_texture = pygame.transform.scale(self.harvested_texture, (TILE_SIZE, TILE_SIZE))


# Create Single Crops
barley = Fruit("Barley", "textures/dirt_sprout.png", "textures/barley.png", "textures/grain_harvested.png")
wheat = Fruit("Wheat", "textures/dirt_sprout.png", "textures/wheat.png", "textures/grain_harvested.png")
potato = Fruit("Potato", "textures/dirt_sprout.png", "textures/potatoes.png", "textures/root_harvested.png")
carrot = Fruit("Carrot", "textures/dirt_sprout.png", "textures/carrot.png", "textures/root_harvested.png")
turnip = Fruit("Turnip", "textures/dirt_sprout.png", "textures/turnip.png", "textures/root_harvested.png")

# Crop List
fruits = [barley, wheat, potato, carrot, turnip]

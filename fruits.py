import pygame
from config import TILE_SIZE
class Fruit:
    def __init__(self, name, sprout_texture, harvestable_texture, harvested_texture):
        self.name = name
        self.sprout_texture = sprout_texture
        self.harvestable_texture = harvestable_texture
        self.harvested_texture = harvested_texture

        # Lade und skaliere die Texturen
        self.sprout_texture = pygame.image.load(self.sprout_texture).convert_alpha()
        self.sprout_texture = pygame.transform.scale(self.sprout_texture, (TILE_SIZE / 2, TILE_SIZE / 2))

        self.harvestable_texture = pygame.image.load(self.harvestable_texture).convert_alpha()
        self.harvestable_texture = pygame.transform.scale(self.harvestable_texture, (TILE_SIZE / 2, TILE_SIZE / 2))

        self.harvested_texture = pygame.image.load(self.harvested_texture).convert_alpha()
        self.harvested_texture = pygame.transform.scale(self.harvested_texture, (TILE_SIZE, TILE_SIZE))

# Definition der Fruchtarten
barley = Fruit("Gerste", "textures/dirt_sprout.png", "textures/barley.png", "textures/grain_harvested.png")
wheat = Fruit("Weizen", "textures/dirt_sprout.png", "textures/wheat.png", "textures/grain_harvested.png")
potato = Fruit("Kartoffeln", "textures/dirt_sprout.png", "textures/potatoes.png", "textures/root_harvested.png")
carrot = Fruit("Karotten", "textures/dirt_sprout.png", "textures/carrot.png", "textures/root_harvested.png")
turnip = Fruit("Steckrüben", "textures/dirt_sprout.png", "textures/turnip.png", "textures/root_harvested.png")

# Fruchtarten Liste
fruits = [barley, wheat, potato, carrot, turnip]

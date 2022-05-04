import pygame.sprite

from Niveaux.Code.import_tools import import_csv_layout, import_cut_graphics
from Niveaux.Code.level_settings import tile_size
from Niveaux.Code.Tile import *


class Level:
    def __init__(self, level_data, surface):
        # general Setup
        self.display_surface = surface
        self.world_shift = -2

        # Terrain Setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # Decorations setup
        decorations_layout = import_csv_layout(level_data['decorations'])
        self.decoration_sprites = self.create_tile_group(decorations_layout, 'decorations')



    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('Niveaux/Tilesets/forest_tileset.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'decorations':
                        # On coupe les tiles et on les mets dans une liste
                        decoration_tile_list = import_cut_graphics('Niveaux/Tilesets/forest_tileset.png')
                        # On atrribut chaque tile a une surface
                        tile_surface = decoration_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        # Run the entire level

        # Draw terrain sprites
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # draw decorations
        self.decoration_sprites.update(self.world_shift)
        self.decoration_sprites.draw(self.display_surface)


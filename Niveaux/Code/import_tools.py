from csv import reader
from Niveaux.Code.level_settings import tile_size
import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

def import_cut_graphics(path): #Cette fonction permet de couper les tilesets pour creer des tiles individuellement.
    # On importe l'image des tiles voulu (ceci en fonction de path).
    surface = pygame.image.load(path).convert_alpha()
    #On cherche le nombre de tiles qu'il y a sur la surface.

    #Sur la largeur de l'image.
    tile_num_x = int(surface.get_size()[0] / tile_size)
    #Sur la hauteur de l'image.
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.surface.Surface((tile_size,tile_size))
            new_surface.blit(surface, (0,0), pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_surface)

    return cut_tiles
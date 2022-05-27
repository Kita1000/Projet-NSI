import pygame.sprite

from Niveaux.Code.import_tools import import_csv_layout, import_cut_graphics
from Niveaux.Code.level_settings import *
from Niveaux.Code.Tile import *
from Niveaux.Code.player import Player

class Level:
    def __init__(self, level_data, surface):
        # general Setup
        self.display_surface = surface
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.change_level = False
        self.current_x = None
        self.current_level = 1

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # Terrain Setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # Decorations setup
        decorations_layout = import_csv_layout(level_data['decorations'])
        self.decoration_sprites = self.create_tile_group(decorations_layout, 'decorations')

        # Fence setup
        fence_layout = import_csv_layout(level_data['fence'])
        self.fence_sprites = self.create_tile_group(fence_layout, 'fence')

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

                    if type == 'fence':
                        # On coupe les tiles et on les mets dans une liste
                        fence_tile_list = import_cut_graphics('Niveaux/Tilesets/forest_tileset.png')
                        # On atrribut chaque tile a une surface
                        tile_surface = fence_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface)
                    self.player.add(sprite)
                if val == '3':
                    hat_surface = pygame.image.load('Images/grave.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, hat_surface)
                    self.goal.add(sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collidable_sprites = self.terrain_sprites.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True

                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.terrain_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < lvl_screen_width / 4 and direction_x < 0 and player_x > 500:
            self.world_shift_x = 8
            player.speed = 0
        elif player_x > lvl_screen_width - (lvl_screen_width / 4) and direction_x > 0 :
            self.world_shift_x = -8
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 8

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < lvl_screen_height / 4 and direction_y < 0 and player_y >= 100:
            self.world_shift_y = player.direction.y

        elif player_y > lvl_screen_height - (lvl_screen_height / 4) and direction_y > 0 :
            self.world_shift_y = -player.direction.y

        else:
            self.world_shift_y = 0


    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def check_win(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        if player_x >= lvl_screen_width -1000:
            self.current_level = 2

    def run(self):
        # draw decorations
        self.decoration_sprites.update(self.world_shift_x,self.world_shift_y)
        self.decoration_sprites.draw(self.display_surface)

        # draw decorations
        self.fence_sprites.update(self.world_shift_x,self.world_shift_y)
        self.fence_sprites.draw(self.display_surface)

        # Draw terrain sprites
        self.terrain_sprites.update(self.world_shift_x,self.world_shift_y)
        self.terrain_sprites.draw(self.display_surface)

        # player sprites
        self.player.update()
        self.horizontal_movement_collision()
        self.check_win()

        self.get_player_on_ground()
        self.vertical_movement_collision()

        self.scroll_x()
        self.scroll_y()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift_x,self.world_shift_y)
        self.goal.draw(self.display_surface)

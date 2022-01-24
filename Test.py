from Sprites import *

pyg.init()


class Game:
    def __init__(self):
        # initialise game window, etc.
        self.screen = pyg.display.set_mode((screen_width, screen_height))
        pyg.display.set_caption(Game_Title)
        self.clock = pyg.time.Clock()
        self.running = True

    def main_menu(self):
        self.Menu_font = pyg.font.Font("Main_Font.otf", 80)
        self.Main_background = pyg.image.load("Main_BG.jpg")
        self.Game_Text = self.Menu_font.render("A Perilous Journey", False, "White")

    def new_game(self):
        # Starts new game not program
        self.all_sprites = pyg.sprite.Group()
        self.platforms = pyg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for platform in Platform_List:
            plat = Platform(*platform)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game Loop-Update
        self.all_sprites.update()
        Collision = pyg.sprite.spritecollide(self.player, self.platforms, False)
        if Collision:
            self.player.pos.y = Collision[0].rect.top
            self.player.vel.y = 0

    def events(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE:
                    self.player.jump()


    def draw(self):
        self.screen.fill(White)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.Main_background, (0, 0))
        self.screen.blit(self.Game_Text, (screen_width / 2.72, screen_height / 2.5))

        pyg.display.flip()

    def show_start_screen(self):
        # game start screen
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    # Show main menu first for future game selection and options screen
    g.main_menu()
    g.new_game()

pyg.quit()
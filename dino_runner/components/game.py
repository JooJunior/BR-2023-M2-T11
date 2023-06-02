#classe principal que obtem os objetos do jogo 
import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


FONT_STYLE = "freesansbold.ttf" #alterar


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False ###
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0 ###
        self.death_count = 0 ###

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

        # coment // self.player2 // aula em 54m

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.score = 0
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0: #DDDDDDDDDDD
            self.game_speed +=5

    
    def draw_text(self, texto, size, position):
        font = pygame.font.Font(FONT_STYLE, size) #font, tam
        text = font.render(texto, True, (0, 0, 0)) #antialising True // serrilhado da letra
        text_rect = text.get_rect() #retangulo do texto
        text_rect.center = position
        self.screen.blit(text, text_rect) #

    def draw_power_up_time(self):
        if self.player_has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2) #arredondar casas decimais
            if time_to_show >= 0:
             self.draw_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 22, (500, 40))
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #but we can use #hex //css
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):

        self.draw_text(f"Score: {self.score}", 22, (1000,50))
 #font, tam
 #antialising True // serrilhado da letra
#retangulo do texto
#

    def draw_death_score(self):
        self.draw_text(f"Contagem de morte: {self.death_count}", 22, (550, 400)) #cor
#metodo classe surface


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill ((255, 255, 255)) #
        half_screen_height = SCREEN_HEIGHT // 2 #div composta arredonda p baixo
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.draw_text("Press any key to start", 22, (half_screen_width, half_screen_height))

        else:
            self.draw_score()
            self.draw_death_score()
            self.draw_text("Presse any key to restart", 22, (half_screen_width, half_screen_height))
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))
#text_rect = text.get_rect()
#text_rect.center = (half_screen_width, half_screen_height)
#self.screen.blit(text, text_rect)"""
            

            #1. Mostre a msg "press any key to restart" > #2Mostrar o Score atingido) > #3 Mostrar death_count 
            #4> resetar o score e game speed quando reiniciar > #5> criar m´´etodo p remover repetição de código do texto


        pygame.display.update()
        self.handle_events_on_menu()

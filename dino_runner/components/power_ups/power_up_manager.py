import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.utils.constants import HEART_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

        self.power_ups_possiveis =[
            Hammer(),
            Shield(),
            Heart()
        ]

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(self.power_ups_possiveis[random.randint(0,2)])  #to acess index
            
    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect): #se pegou o powerup..
                if power_up.type == HEART_TYPE:
                    game.player.heart.append(power_up)
                    self.power_ups.remove(power_up)
                    print(len(game.player.heart))
                else:
                    power_up.start_time = pygame.time.get_ticks() #pega o tempo no momento exato
                    game.player.shield = True
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000) #o pygame recebe com mili segundos, entao mmultiplicamos por 1000 (lembra do delay)
                    self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
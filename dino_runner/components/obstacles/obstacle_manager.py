import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import HAMMER_TYPE, MUSIC2
pygame.mixer.init()


class ObstacleManager: #D R
    def __init__(self):
        self.obstacles = [] #

    def update(self, game): 
        obstacle_type = [
            Cactus(), 
            Bird()
        ]
        if len(self.obstacles) == 0:#verifica se tem obstaculo na tela p dps append #é o tamanho da lista 
            self.obstacles.append(obstacle_type[random.randint(0, 1)]) #D

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
              # - ultimo elemento da lista
                if not game.player.has_power_up and len(game.player.heart) == 0 :
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1 ##
                    pygame.mixer.Sound.play(MUSIC2)
                    break
                else:
                    if len(game.player.heart) > 0 and not  game.player.has_power_up:
                        game.player.heart.pop()
                        self.obstacles.remove(obstacle)
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                   
    def draw(self, screen):
        for obstacle in self.obstacles: #p cada obstaculo q ta na lista self.obstacles (inicio), todo obstaculo é adicionado la como imagem
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = [] #quando a gente morre ou tem martelo


        
import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

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
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1 ##
                break
            
    def draw(self, screen):
        for obstacle in self.obstacles: #p cada obstaculo q ta na lista self.obstacles (inicio), todo obstaculo é adicionado la como imagem
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = [] #quando a gente morre ou tem martelo

        
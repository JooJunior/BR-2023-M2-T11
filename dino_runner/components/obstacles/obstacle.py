import pygame
from pygame.sprite import Sprite #Maisculo 1 indica que é uma classe

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite): #Herança, a classe Obstacle instanciando a Sprite eherdando a classe Sprite // atr e funcoes de Sprite q é uma classe da biblioteca pygame
    def __init__(self, image, type): #fortalecer
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #d #método usado proveninete da Sprite
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: #pode ser metodo de sprite
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))


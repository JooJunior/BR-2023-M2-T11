import pygame
from pygame.sprite import Sprite #Maisculo 1 indica que é uma classe

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite): #Herança, a classe Obstacle instanciando a Sprite eherdando a classe Sprite
    def __init__(self, image):
        self.image = image
    
    def update(self):
        pass

    def draw(self, screen):
        pass

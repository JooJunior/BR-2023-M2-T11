import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

#POWERUPS posso usar a logicado BIRD para por a sprite da maça
class PowerUp(Sprite): 
    def __init__(self, image, type):
        self.image = image #recebendo como parametro
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(125, 175) #aparece em alturas variadas
        self.start_time = 0 #conta o tempo em q ele vai estar habilidatdo
        self.duration = random.randint(5, 10)

    def update(self, game_speed, power_ups): #logica parecida c obstacles
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width: #revisar essa logica
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect) #ja tem os atributos acima, entao simplesmente passa o objeto
        

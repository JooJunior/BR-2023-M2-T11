import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = 260
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)   #div composta     
        self.step_index += 1

        if self.step_index >= 9: ## N >9 // pq ele ainda vai ser 1 
            self.step_index = 0
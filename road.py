import pygame
from pygame.surface import Surface
from enemyCar import EnemyCar
from pygame.sprite import Group
import random

class Road:

  def __init__(self, number, spriteGroup:Group, collisionGroup:Group):
    self.number = number * 100

    self.enemyCar = EnemyCar((0, 255, 0), 100, 50)
    self.enemyCar.rect.x = 200 * random.random() + 400
    self.enemyCar.rect.y = 0

    self.speed =  random.random() / 2

    spriteGroup.add(self.enemyCar)
    collisionGroup.add(self.enemyCar)
    return

  def draw(self, screen: Surface, y: float, dt: float):
    pygame.draw.rect(screen, (128, 128, 118), (0, y - self.number, 400, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, y - self.number, 400, 2))
    pygame.draw.rect(screen, (255, 255, 255),
                     (0, 99 + (y - self.number), 400, 2))

    self.enemyCar.moveLeft(dt * self.speed)
    
    self.enemyCar.rect.y = y - self.number + 25

    self.enemyCar.draw(screen)

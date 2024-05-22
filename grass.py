import pygame
from borders import Wall
from pygame.surface import Surface
from pygame.sprite import Group
import random

rock_image = pygame.image.load("rock.png") # 1.) Open Rock
rock_image = pygame.transform.scale(rock_image, (100 * 0.905,100)) # 2.) Scale Rock



class Grass:
  def __init__(self, number, wall_list: Group):
   
    self.number = number * 100
    self.rockPosition = (random.random() * 470)-70
    
    self.wall = Wall(self.rockPosition, 0, 100 * 0.905, 100)
    wall_list.add(self.wall)
   
    return
    
  def draw(self, screen:Surface, y:float, dt:float):
    pygame.draw.rect(screen, (0,200,0), (0, y - self.number, 400, 100 ))
    self.wall.rect.y = y - self.number

    
    screen.blit(rock_image, (self.rockPosition,y - self.number)) # 3.) Draw Rock
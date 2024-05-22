import sys
import pygame
import random

from borders import Wall
from car import Car
from enemyCar import EnemyCar
from grass import Grass
from road import Road

# Hello!!!

gameOver = False

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

clock = pygame.time.Clock()

globalY = 200


playerCar = Car((255, 0, 0), 20, 30)
playerCar.rect.y= 170
playerCar.rect.x = 180

bird = pygame.image.load("download.png")





all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()



wall = Wall(0, 0, 10, 400)
wall_list.add(wall)

wall = Wall(10, 0, 790, 10)
wall_list.add(wall)



wall = Wall(390, 0, 10, 400)
wall_list.add(wall)

wall = Wall(390, 0, 10, 400)
wall_list.add(wall)




playerCar.walls = wall_list

all_sprites.add(playerCar)

section = []
section.append(Grass(0, wall_list))
section.append(Grass(1, wall_list))

frames = 0

for i in range(80):
  randomNum = random.random() # 0 - 1
  if randomNum > 0.5: #More grass = larger number
    section.append(Road(i + 2, enemy_sprites, wall_list))
  else:
    section.append(Grass(i + 2, wall_list))



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  dt = clock.tick(60) * (1 if not gameOver else 0)

  #screen.fill((56,128,4))
  screen.fill((0,0,0))

  #pygame.draw.rect(screen, (128,128,118), (0,50, 400, 200))
  #pygame.draw.rect(screen, (255,255,255), (0, 150, 400, 2))
  


  if gameOver == False:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      playerCar.moveUp(1)
    if keys[pygame.K_s] and  not globalY < 200 :
      playerCar.moveDown(1)
  
  
    if playerCar.rect.y < 120: 
      playerCar.moveDown(1)
      globalY += 1
  
    
    if keys[pygame.K_a]:
      playerCar.moveLeft(1)
    if keys[pygame.K_d]:
      playerCar.moveRight(1)
   
    globalY += 0.1
    frames += 1
    if(frames % 10 == 0):
      frames = 0
      playerCar.moveDown(1)




  

  hit_list = pygame.sprite.spritecollide(playerCar, enemy_sprites, False)
  #print(hit_list)

  for i in section:
    i.draw(screen, globalY, dt)
  all_sprites.draw(screen)
  #wall_list.draw(screen)

  enemy_sprites.draw(screen)

  if playerCar.rect.y > 300:
    gameOver = True
    screen.blit(bird, (-5, 50))


  pygame.display.update()

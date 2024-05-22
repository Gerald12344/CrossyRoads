import pygame

WHITE = (255, 255, 255)


# This is the class
class Car(pygame.sprite.Sprite):

  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)

    pygame.draw.rect(self.image, color, (0,0, width, height))

    self.rect = self.image.get_rect()



  def moveRight(self, distance):
    self.rect.x += distance
    hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    for block in hit_list:
      self.rect.right = block.rect.left
    

  def moveLeft(self, distance):
    self.rect.x -= distance
    hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    for block in hit_list:
      self.rect.left = block.rect.right


  def isCoilliding(self):
    hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    return not len(hit_list) > 0

  
  def moveUp(self, distance):
    self.rect.y -= distance
    hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    for block in hit_list:
      self.rect.top = block.rect.bottom

  def moveDown(self, distance):
    self.rect.y += distance
    hit_list = pygame.sprite.spritecollide(self, self.walls, False)
    for block in hit_list:
      self.rect.bottom = block.rect.top

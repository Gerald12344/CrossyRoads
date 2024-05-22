import pygame

WHITE = (255, 255, 255)



# This is the class
class EnemyCar(pygame.sprite.Sprite):

  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)

    pygame.draw.rect(self.image, color, (0,0, width, height))

    self.rect = self.image.get_rect()

  def moveRight(self, distance):
    self.checkOffScreen()
    self.rect.x += distance

  def moveLeft(self, distance):
    self.checkOffScreen()
    self.rect.x -= distance


  def checkOffScreen(self):
    if self.rect.x + self.rect.width < -10:
      self.rect.x = 400
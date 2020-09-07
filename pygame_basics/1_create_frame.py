import pygame

pygame.init()
pygame.display.set_caption('lesson 1 : create frame')

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.update()

pygame.quit()
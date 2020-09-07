import os
import pygame

# init
pygame.init()
pygame.display.set_caption('project lesson 1 : init')

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
sprite_path = os.path.join(current_path, 'res')

background = pygame.image.load(os.path.join(sprite_path, 'background.png'))

stage = pygame.image.load(os.path.join(sprite_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(sprite_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH / 2 - character_width / 2
character_y_pos = SCREEN_HEIGHT - character_height - stage_height

running = True
while running:
  dt = clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(background, (0, 0))
  screen.blit(stage, (0, (SCREEN_HEIGHT - stage_height)))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update()

pygame.quit()
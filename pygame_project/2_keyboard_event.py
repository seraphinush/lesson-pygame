import os
import pygame

# init
pygame.init()
pygame.display.set_caption('project lesson 2 :  keyboard event')

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
sprite_path = os.path.join(current_path, 'res')

background = pygame.image.load(os.path.join(sprite_path, 'background.png'))
stage = pygame.image.load(os.path.join(sprite_path, 'stage.png'))
character = pygame.image.load(os.path.join(sprite_path, 'character.png'))
weapon = pygame.image.load(os.path.join(sprite_path, 'weapon.png'))

stage_size = stage.get_rect().size
stage_height = stage_size[1]

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH / 2 - character_width / 2
character_y_pos = SCREEN_HEIGHT - character_height - stage_height

character_to_x = 0
character_to_y = 0
CHARACTER_SPEED = 5

weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapon
WEAPON_SPEED = 10
weapons = []

running = True
while running:
  dt = clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        pass
      elif event.key == pygame.K_DOWN:
        pass
      elif event.key == pygame.K_LEFT:
        character_to_x -= CHARACTER_SPEED
      elif event.key == pygame.K_RIGHT:
        character_to_x += CHARACTER_SPEED
      elif event.key == pygame.K_SPACE:
        weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
        weapon_y_pos = character_y_pos
        weapons.append([weapon_x_pos, weapon_y_pos])

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        character_to_x = 0
  
  character_x_pos += character_to_x
  
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > SCREEN_WIDTH - character_width:
    character_x_pos = SCREEN_WIDTH - character_width
  
  weapons = [[w[0], w[1] - WEAPON_SPEED] for w in weapons]
  weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

  screen.blit(background, (0, 0))

  for weapon_x_pos, weapon_y_pos in weapons:
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

  screen.blit(stage, (0, (SCREEN_HEIGHT - stage_height)))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update()

pygame.quit()
import pygame
import random

pygame.init()
pygame.display.set_caption('lesson 8.5 : quiz')

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('./res/background.png')
character = pygame.image.load('./res/character.png')
enemy = pygame.image.load('./res/enemy.png')

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH / 2 - character_width / 2
character_y_pos = SCREEN_HEIGHT - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, SCREEN_WIDTH)
enemy_y_pos = 0 - enemy_height

to_x = 0
to_y = 0
CHARACTER_SPEED = 0.5
ENEMY_SPEED = 0.3

clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)

point = 0

running = True
while running:
  dt = clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # movement
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        to_x -= CHARACTER_SPEED
      elif event.key == pygame.K_RIGHT:
        to_x += CHARACTER_SPEED
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
      elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0

  character_x_pos += to_x * dt
  character_y_pos += to_y * dt

  enemy_y_pos += ENEMY_SPEED * dt

  if enemy_y_pos > SCREEN_HEIGHT:
    enemy_y_pos = 0 - enemy_height
    enemy_x_pos = random.randint(0, SCREEN_WIDTH)
    point += 1

  # boundary check
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > SCREEN_WIDTH - character_width:
    character_x_pos = SCREEN_WIDTH - character_width

  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > SCREEN_HEIGHT - character_height:
    character_y_pos = SCREEN_HEIGHT - character_height

  # collision
  character_rect = character.get_rect()
  character_rect.left = int(character_x_pos)
  character_rect.top = int(character_y_pos)

  enemy_rect = enemy.get_rect()
  enemy_rect.left = int(enemy_x_pos)
  enemy_rect.top = int(enemy_y_pos)

  # render
  screen.blit(background, (0, 0))
  screen.blit(character, (int(character_x_pos), int(character_y_pos)))
  screen.blit(enemy, (int(enemy_x_pos), int(enemy_y_pos)))

  score = game_font.render('score : ' + str(int(point)), True, (255, 255, 255))
  screen.blit(score, (10, 10))

  if character_rect.colliderect(enemy_rect):
    running = False

  pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
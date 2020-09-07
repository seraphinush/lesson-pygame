import pygame

pygame.init()
pygame.display.set_caption('lesson 3 : main sprite')

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('./res/background.png')
character = pygame.image.load('./res/character.png')

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #screen.fill((0, 0, 255))
  screen.blit(background, (0, 0))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update()

pygame.quit()
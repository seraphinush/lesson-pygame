import os
import pygame

# init
pygame.init()
pygame.display.set_caption('pang')

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
sprite_path = os.path.join(current_path, 'res')

# load images
background = pygame.image.load(os.path.join(sprite_path, 'background.png'))
stage = pygame.image.load(os.path.join(sprite_path, 'stage.png'))
character = pygame.image.load(os.path.join(sprite_path, 'character.png'))
weapon = pygame.image.load(os.path.join(sprite_path, 'weapon.png'))
ball_images = [
  pygame.image.load(os.path.join(sprite_path, 'ball1.png')),
  pygame.image.load(os.path.join(sprite_path, 'ball2.png')),
  pygame.image.load(os.path.join(sprite_path, 'ball3.png')),
  pygame.image.load(os.path.join(sprite_path, 'ball4.png'))
]

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

BALL_SPEED_X = 3
BALL_SPEED_Y = [-18, -15, -12, -9]
balls = []
balls.append({
  'pos_x': 50,
  'pos_y': 50,
  'img_idx': 0,
  'to_x': BALL_SPEED_X,
  'to_y': -6,
  'init_speed_y': BALL_SPEED_Y[0]
})

weap_to_rm = -1
ball_to_rm = -1

# font
game_font = pygame.font.Font(None, 40)
TOTAL_TIME = 10
start_tick = pygame.time.get_ticks()
game_result = 'Game Over'

def reset():
  global character_x_pos
  global character_y_pos
  global CHARACTER_SPEED
  global WEAPON_SPEED
  global BALL_SPEED_X
  global BALL_SPEED_Y
  global balls
  global weap_to_rm
  global ball_to_rm
  global start_tick

  character_x_pos = SCREEN_WIDTH / 2 - character_width / 2
  character_y_pos = SCREEN_HEIGHT - character_height - stage_height
  CHARACTER_SPEED = 5
  WEAPON_SPEED = 10
  BALL_SPEED_X = 3
  BALL_SPEED_Y = [-18, -15, -12, -9]
  balls = []
  balls.append({
    'pos_x': 50,
    'pos_y': 50,
    'img_idx': 0,
    'to_x': BALL_SPEED_X,
    'to_y': -6,
    'init_speed_y': BALL_SPEED_Y[0]
  })
  weap_to_rm = -1
  ball_to_rm = -1
  start_tick = pygame.time.get_ticks()

# state
running = True
pause = False

reset()

while running:
  dt = clock.tick(60)

  # pause
  if pause:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        pause = False
        start_tick = pygame.time.get_ticks()
        break

    game_result = 'Pause'
    msg = game_font.render(game_result, True, (255, 255, 0))
    msg_rect = msg.get_rect(center=(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)))
    screen.blit(msg, msg_rect)

    pygame.display.update()
    continue

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
      elif event.key == pygame.K_r:
        reset()
      elif event.key == pygame.K_ESCAPE:
        pause = True

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

  for ball_idx, ball_val in enumerate(balls):
    ball_pos_x = ball_val['pos_x']
    ball_pos_y = ball_val['pos_y']
    ball_img_idx = ball_val['img_idx']

    ball_size = ball_images[ball_img_idx].get_rect().size
    ball_width = ball_size[0]
    ball_height = ball_size[1]

    if ball_pos_x < 0 or ball_pos_x > SCREEN_WIDTH - ball_width:
      ball_val['to_x'] = -ball_val['to_x']
    
    if ball_pos_y >= SCREEN_HEIGHT - stage_height - ball_height:
      ball_val['to_y'] = ball_val['init_speed_y']
    else:
      ball_val['to_y'] += 0.5

    ball_val['pos_x'] += ball_val['to_x']
    ball_val['pos_y'] += ball_val['to_y']

  # collision
  character_rect = character.get_rect()
  character_rect.left = int(character_x_pos)
  character_rect.top = int(character_y_pos)

  for ball_idx, ball_val in enumerate(balls):
    ball_pos_x = ball_val['pos_x']
    ball_pos_y = ball_val['pos_y']
    ball_img_idx = ball_val['img_idx']

    ball_rect = ball_images[ball_img_idx].get_rect()
    ball_rect.left = int(ball_pos_x)
    ball_rect.top = int(ball_pos_y)

    if character_rect.colliderect(ball_rect):
      running = False
      break

    for weap_idx, weap_val in enumerate(weapons):
      weapon_pos_x = weap_val[0]
      weapon_pos_y = weap_val[1]

      weapon_rect = weapon.get_rect()
      weapon_rect.left = int(weapon_pos_x)
      weapon_rect.top = int(weapon_pos_y)

      if weapon_rect.colliderect(ball_rect):
        weap_to_rm = weap_idx
        ball_to_rm = ball_idx

        # split        
        if ball_img_idx < 3:
          ball_width = ball_rect[0]
          ball_height = ball_rect[1]
          sm_ball_rect = ball_images[ball_img_idx + 1].get_rect()
          sm_ball_width = sm_ball_rect.size[0]
          sm_ball_height = sm_ball_rect.size[1]

          balls.append({
            'pos_x': ball_pos_x + ball_width / 2 - sm_ball_width / 2,
            'pos_y': ball_pos_y + ball_height / 2 - sm_ball_height / 2,
            'img_idx': ball_img_idx + 1,
            'to_x': -BALL_SPEED_X,
            'to_y': -6,
            'init_speed_y': BALL_SPEED_Y[ball_img_idx + 1]
          })
          balls.append({
            'pos_x': ball_pos_x + ball_width / 2 - sm_ball_width / 2,
            'pos_y': ball_pos_y + ball_height / 2 - sm_ball_height / 2,
            'img_idx': ball_img_idx + 1,
            'to_x': BALL_SPEED_X,
            'to_y': -6,
            'init_speed_y': BALL_SPEED_Y[ball_img_idx + 1]
          })
        break
    else:
      continue
    break
      
  if ball_to_rm > -1:
    del balls[ball_to_rm]
    ball_to_rm = -1

  if weap_to_rm > -1:
    del weapons[weap_to_rm]
    weap_to_rm = -1

  # win condition
  if len(balls) == 0:
    game_result = 'Win'
    running = False

  # timer
  elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
  timer = game_font.render('Time : {}'.format(int(TOTAL_TIME - elapsed_time)), True, (255, 255, 255))

  # render
  screen.blit(background, (0, 0))

  for weapon_x_pos, weapon_y_pos in weapons:
    screen.blit(weapon, (int(weapon_x_pos), int(weapon_y_pos)))

  for idx, val in enumerate(balls):
    ball_pos_x = val['pos_x']
    ball_pos_y = val['pos_y']
    ball_img_idx = val['img_idx']
    screen.blit(ball_images[ball_img_idx], (int(ball_pos_x), int(ball_pos_y)))

  screen.blit(stage, (0, (SCREEN_HEIGHT - stage_height)))
  screen.blit(character, (int(character_x_pos), int(character_y_pos)))

  screen.blit(timer, (10, 10))

  # game over
  if (TOTAL_TIME - elapsed_time) <= 0:
    game_result = 'Time Over'
    running = False

  pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)))
screen.blit(msg, msg_rect)

pygame.display.update()
pygame.time.delay(2000)

pygame.quit()

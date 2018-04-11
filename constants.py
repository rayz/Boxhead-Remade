import pygame
import os


os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])


clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
RED = (250, 20 , 0)

boxpic = pygame.image.load(("images/boxhead.png"))
bloodpic = pygame.image.load(('images/blood.png'))
bloodpic = pygame.transform.scale(bloodpic, (50,50))


player_up_pic = pygame.image.load(("images/player_up.png"))
player_up_pic = pygame.transform.scale(player_up_pic, (25,25))

player_upleft_pic = pygame.image.load(("images/player_upleft.png"))
player_upleft_pic = pygame.transform.scale(player_upleft_pic, (25,25))

player_upright_pic = pygame.image.load(("images/player_upright.png"))
player_upright_pic = pygame.transform.scale(player_upright_pic, (25,25))



player_down_pic = pygame.image.load(("images/player_down.png"))
player_down_pic = pygame.transform.scale(player_down_pic, (25,25))

player_downleft_pic = pygame.image.load(("images/player_downleft.png"))
player_downleft_pic = pygame.transform.scale(player_downleft_pic, (25,25))

player_downright_pic = pygame.image.load(("images/player_downright.png"))
player_downright_pic = pygame.transform.scale(player_downright_pic, (25,25))




player_left_pic = pygame.image.load(("images/player_left.png"))
player_left_pic = pygame.transform.scale(player_left_pic, (25,25))

player_right_pic = pygame.image.load(("images/player_right.png"))
player_right_pic = pygame.transform.scale(player_right_pic, (25,25))
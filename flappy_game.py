
import random #for generating random numbers
import sys
from pip import main # for exiting the game by sys.exit() to exit the programme
import pygame
import pygame.locals import *

from main import FPSCLOCK #basic pygame imports

#global variables for game

FPS = 32
SCREENWIDTH = 289   
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode(( SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = 'D:\\FLAPPYBIRD GAME\\gallery\\sprites\\bird.png'
BACKGROUND = 'D:\\FLAPPYBIRD GAME\\gallery\\sprites\\g.png'
PIPE = 'D:\\FLAPPYBIRD GAME\\gallery\\sprites\\pipe.png'


if __name__ == '__main__':
    #this will be the main function where our game will start
    pygame.init()#it initialize all pygame modules
    FPSCLOCK=  pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\0.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\1.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\2.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\3.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\4.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\5.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\6.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\7.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\8.png').convert_alpha(),
        pygame.image.load('D:\\FLAPPYBIRD GAME\\gallery\sprites\\9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load("D:\FLAPPYBIRD GAME\gallery\sprites\message1.png")
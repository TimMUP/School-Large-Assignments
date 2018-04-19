from math import *
from pygame import *
from random import *

#Initializing and staring pygames
init()
SIZE = (1000, 700)
screen = display.set_mode(SIZE)

#Setting colors for use later
GREY = (192, 192, 192)
DARK_GREY = (96, 96, 96)
ORANGE = (255, 128, 0)
PINK = (255, 51, 153)
BLUE = (77, 129, 249)
VIOLET = (238, 130, 238)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHEAT_YELLOW = (188, 185, 93)
WHEAT_OUTLINE = (182, 180, 106)

#Colors for day time
GREEN = (0, 153, 0)
SUN_YELLOW = (255, 255, 0)
SKY_BLUE = (90, 180, 240)
BARN_ROOF = (251, 252, 234)
BARN_SHADEROOF = (223, 223, 223)
BARN_CONNECTOR = (40, 52, 56)
BARN_VENT = (228, 228, 228)
BARN_WINDOW = (192, 192, 192)
BARN_BROWN = (102, 0, 0)
SIDEBARN_BROWN = (75, 0, 0)
STONE_GREY = (128, 128, 128)
STONE_BLACK = (64, 64, 64)
DIRT_BROWN = (153, 76, 0)
DIRT_DARKBROWN = (102, 51, 0)
TRACTOR_WHEEL = (37, 17, 8)
TRACTOR_WHEELTRIM = (229, 216, 99)
TRACTOR_GREEN = (20, 84, 15)

#Colors for night time
MOON_GREY = (255, 255, 204)
DARK_GREEN = (8, 75, 8)
SKY_DARKBLUE = (0, 0, 5)
NBARN_ROOF = (224, 225, 208)
NBARN_SHADEROOF = (187, 188, 178)
NBARN_CONNECTOR = (25, 25, 25)
NBARN_VENT = (216, 216, 216)
NBARN_WINDOW = (172, 172, 172)
NBARN_BROWN = (88, 6, 6)
NSIDEBARN_BROWN = (40, 0, 0)
NSTONE_GREY = (96, 96, 96)
NSTONE_BLACK = (32, 32, 32)
NDIRT_BROWN = (102, 51, 0)
NDIRT_DARKBROWN = (51, 25, 0)
NTRACTOR_WHEEL = (16, 7, 4)
NTRACTOR_WHEELTRIM = (193, 184, 97)
NTRACTOR_GREEN = (11, 51, 9)

#Corlor set for rainbow bunny
BUNNY_PINK = (232, 183, 229)
BUNNY_GREEN = (188, 255, 33)
BUNNY_TURQUOISE = (36, 255, 167)
BUNNY_BLUE = (36, 153, 255)
BUNNY_PURPLE = (116, 46, 255)
BUNNY_ORANGE = (255, 157, 46)
BUNNY_DARKPINK = (186, 108, 147)
BUNNY_EYE = (44, 145, 176)

#Variables for use later in program
day = True
starCounter = 0
balloonCounter = 0
stoneCounter = 0
eggCounter = 0
dirtCounter = 0
rabbitCounter = 0
STONE_FILL = 0
STONE_OUTLINE = 0
DIRT_FILL = 0
DIRT_FILL = 0

#Draws Random pixel rabbits around, made of hundreds of rect functions by coloring each pixel in indivisualy
def drawRandomPixelRabbit(x, y, s):
    draw.rect (screen, BLACK, (x, y + 13*s, s, 7*s))
    draw.rect (screen, BLACK, (x + s, y + 11*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 2*s, y + 10*s, s, s))
    draw.rect (screen, BLACK, (x + 3*s, y + 6*s, s, 5*s))
    draw.rect (screen, BLACK, (x + 2*s, y + 2*s, s, 4*s))
    draw.rect (screen, BLACK, (x + 3*s, y + 1*s, s, s))
    draw.rect (screen, BLACK, (x + 4*s, y, 2*s, s))
    draw.rect (screen, BLACK, (x + 6*s, y + 1*s, 2*s, s))
    draw.rect (screen, BLACK, (x + 7*s, y + 2*s, s, 3*s))
    draw.rect (screen, BLACK, (x + 8*s, y + 3*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 9*s, y + 2*s, s, s))
    draw.rect (screen, BLACK, (x + 10*s, y + 1*s, 3*s, s))
    draw.rect (screen, BLACK, (x + 13*s, y + 2*s, s, 8*s))
    draw.rect (screen, BLACK, (x + 14*s, y + 10*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 15*s, y + 11*s, s, s))
    draw.rect (screen, BLACK, (x + 16*s, y + 12*s, 8*s, s))
    draw.rect (screen, BLACK, (x + 23*s, y + 13*s, 3*s, s))
    draw.rect (screen, BLACK, (x + 26*s, y + 14*s, s, s))
    draw.rect (screen, BLACK, (x + 27*s, y + 15*s, s, s))
    draw.rect (screen, BLACK, (x + 28*s, y + 16*s, s, s))
    draw.rect (screen, BLACK, (x + 29*s, y + 17*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 30*s, y + 19*s, s, 5*s))
    draw.rect (screen, BLACK, (x + 31*s, y + 20*s, s, 4*s))
    draw.rect (screen, BLACK, (x + 32*s, y + 21*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 29*s, y + 24*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 28*s, y + 26*s, s, s))
    draw.rect (screen, BLACK, (x + 27*s, y + 27*s, s, s))
    draw.rect (screen, BLACK, (x + 16*s, y + 28*s, 12*s, s))
    draw.rect (screen, BLACK, (x + 16*s, y + 27*s, s, s))
    draw.rect (screen, BLACK, (x + 17*s, y + 26*s, s, s))
    draw.rect (screen, BLACK, (x + 14*s, y + 25*s, 7*s, s))
    draw.rect (screen, BLACK, (x + 13*s, y + 26*s, s, s))
    draw.rect (screen, BLACK, (x + 12*s, y + 27*s, s, s))
    draw.rect (screen, BLACK, (x + 7*s, y + 28*s, 5*s, s))
    draw.rect (screen, BLACK, (x + 4*s, y + 27*s, 4*s, s))
    draw.rect (screen, BLACK, (x + 8*s, y + 26*s, s, s))
    draw.rect (screen, BLACK, (x + 9*s, y + 25*s, s, s))
    draw.rect (screen, BLACK, (x + 10*s, y + 24*s, s, s))
    draw.rect (screen, BLACK, (x + 4*s, y + 26*s, s, s))
    draw.rect (screen, BLACK, (x + 5*s, y + 25*s, s, s))
    draw.rect (screen, BLACK, (x + 6*s, y + 23*s, s, 2*s))
    draw.rect (screen, BLACK, (x + 2*s, y + 22*s, 4*s, s))
    draw.rect (screen, BLACK, (x + 1*s, y + 20*s, s, 2*s))
    draw.rect (screen, WHITE, (x + 1*s, y + 13*s, s, 7*s))
    draw.rect (screen, WHITE, (x + 2*s, y + 11*s, s, 11*s))
    draw.rect (screen, BUNNY_PINK, (x + 2*s, y + 20*s, s, 2*s))
    draw.rect (screen, WHITE, (x + 3*s, y + 2*s, s, 4*s))
    draw.rect (screen, WHITE, (x + 3*s, y + 11*s, s, 11*s))
    draw.rect (screen, BUNNY_PINK, (x + 3*s, y + 20*s, s, s))
    draw.rect (screen, WHITE, (x + 4*s, y + s, s, 21*s))
    draw.rect (screen, WHITE, (x + 5*s, y + s, s, 21*s))
    draw.rect (screen, BUNNY_GREEN, (x + 5*s, y + 13*s, s, 2*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 5*s, y + 15*s, s, 2*s))
    draw.rect (screen, BUNNY_BLUE, (x + 5*s, y + 17*s, s, 1*s))
    draw.rect (screen, WHITE, (x + 6*s, y + 2*s, s, 21*s))
    draw.rect (screen, BUNNY_GREEN, (x + 6*s, y + 11*s, s, 4*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 6*s, y + 15*s, s, 2*s))
    draw.rect (screen, BUNNY_BLUE, (x + 6*s, y + 17*s, s, 3*s))    
    draw.rect (screen, BUNNY_PURPLE, (x + 6*s, y + 20*s, s, s))  
    draw.rect (screen, WHITE, (x + 7*s, y + 5*s, s, 22*s))
    draw.rect (screen, BUNNY_GREEN, (x + 7*s, y + 11*s, s, 5*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 7*s, y + 16*s, s, s))
    draw.rect (screen, BUNNY_BLUE, (x + 7*s, y + 17*s, s, 3*s))    
    draw.rect (screen, BUNNY_PURPLE, (x + 7*s, y + 20*s, s, s)) 
    draw.rect (screen, WHITE, (x + 8*s, y + 5*s, s, 21*s))
    draw.rect (screen, RED, (x + 8*s, y + 5*s, s, 3*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 8*s, y + 8*s, s, 5*s))
    draw.rect (screen, BUNNY_GREEN, (x + 8*s, y + 13*s, s, s))
    draw.rect (screen, BLACK, (x + 8*s, y + 14*s, s, 4*s))
    draw.rect (screen, BUNNY_BLUE, (x + 8*s, y + 18*s, s, 3*s))    
    draw.rect (screen, BUNNY_PURPLE, (x + 8*s, y + 20*s, s, 2*s))
    draw.rect (screen, WHITE, (x + 9*s, y + 3*s, s, 22*s))
    draw.rect (screen, RED, (x + 9*s, y + 3*s, s, 5*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 9*s, y + 8*s, s, 5*s))
    draw.rect (screen, BLACK, (x + 9*s, y + 13*s, s, 5*s))
    draw.rect (screen, BUNNY_EYE, (x + 9*s, y + 14*s, s, s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 9*s, y + 18*s, s, s))
    draw.rect (screen, BUNNY_BLUE, (x + 9*s, y + 19*s, s, 3*s))    
    draw.rect (screen, WHITE, (x + 10*s, y + 2*s, s, 22*s))
    draw.rect (screen, RED, (x + 10*s, y + 2*s, s, 4*s))
    draw.rect (screen, BUNNY_DARKPINK, (x + 10*s, y + 6*s, s, 3*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 10*s, y + 9*s, s, 4*s))
    draw.rect (screen, BLACK, (x + 10*s, y + 13*s, s, 5*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 10*s, y + 18*s, s, s))
    draw.rect (screen, BUNNY_BLUE, (x + 10*s, y + 19*s, s, 3*s))  
    draw.rect (screen, WHITE, (x + 11*s, y + 2*s, s, 26*s))
    draw.rect (screen, RED, (x + 11*s, y + 2*s, s, s))
    draw.rect (screen, BUNNY_DARKPINK, (x + 11*s, y + 3*s, s, 6*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 11*s, y + 9*s, s, 4*s))
    draw.rect (screen, BLACK, (x + 11*s, y + 13*s, s, 5*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 11*s, y + 18*s, s, 2*s))
    draw.rect (screen, BUNNY_BLUE, (x + 11*s, y + 20*s, s, 2*s))     
    draw.rect (screen, WHITE, (x + 12*s, y + 2*s, s, 25*s))
    draw.rect (screen, RED, (x + 12*s, y + 2*s, s, s))
    draw.rect (screen, BUNNY_DARKPINK, (x + 12*s, y + 3*s, s, 7*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 12*s, y + 10*s, s, 3*s))
    draw.rect (screen, BLACK, (x + 12*s, y + 13*s, s, 4*s))
    draw.rect (screen, BUNNY_GREEN, (x + 12*s, y + 17*s, s, s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 12*s, y + 18*s, s, 2*s))
    draw.rect (screen, BUNNY_BLUE, (x + 12*s, y + 20*s, s, 1*s))        
    draw.rect (screen, WHITE, (x + 13*s, y + 10*s, s, 16*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 13*s, y + 10*s, s, 3*s))
    draw.rect (screen, BUNNY_GREEN, (x + 13*s, y + 13*s, s, 6*s))
    draw.rect (screen, BUNNY_TURQUOISE, (x + 13*s, y + 19*s, s, s))
    draw.rect (screen, WHITE, (x + 14*s, y + 12*s, s, 13*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 14*s, y + 12*s, s, s))
    draw.rect (screen, BUNNY_GREEN, (x + 14*s, y + 13*s, s, 6*s)) 
    draw.rect (screen, WHITE, (x + 15*s, y + 12*s, s, 13*s))
    draw.rect (screen, WHITE, (x + 16*s, y + 13*s, s, 12*s))
    draw.rect (screen, WHITE, (x + 17*s, y + 13*s, s, 12*s))
    draw.rect (screen, WHITE, (x + 18*s, y + 13*s, s, 12*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 18*s, y + 16*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 18*s, y + 18*s, s, 3*s))
    draw.rect (screen, WHITE, (x + 19*s, y + 13*s, s, 12*s))
    draw.rect (screen, RED, (x + 19*s, y + 14*s, s, 3*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 19*s, y + 17*s, s, s))
    draw.rect (screen, BUNNY_GREEN, (x + 19*s, y + 18*s, s, 3*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 19*s, y + 21*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 19*s, y + 23*s, s, 1*s))   
    draw.rect (screen, RED, (x + 20*s, y + 13*s, s, 3*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 20*s, y + 16*s, s, 3*s))
    draw.rect (screen, BUNNY_GREEN, (x + 20*s, y + 19*s, s, 3*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 20*s, y + 22*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 20*s, y + 24*s, s, s))  
    draw.rect (screen, WHITE, (x + 21*s, y + 13*s, s, 15*s))
    draw.rect (screen, RED, (x + 21*s, y + 13*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 21*s, y + 17*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 21*s, y + 19*s, s, 3*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 21*s, y + 22*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 21*s, y + 24*s, s, 2*s))
    draw.rect (screen, BUNNY_PURPLE, (x + 21*s, y + 26*s, s, 1*s))
    draw.rect (screen, RED, (x + 22*s, y + 13*s, s, 5*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 22*s, y + 18*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 22*s, y + 20*s, s, 2*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 22*s, y + 22*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 22*s, y + 24*s, s, 2*s))
    draw.rect (screen, BUNNY_PURPLE, (x + 22*s, y + 26*s, s, 2*s))    
    draw.rect (screen, RED, (x + 23*s, y + 14*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 23*s, y + 18*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 23*s, y + 20*s, s, 2*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 23*s, y + 22*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 23*s, y + 24*s, s, 3*s))
    draw.rect (screen, BUNNY_PURPLE, (x + 23*s, y + 27*s, s, 1*s))    
    draw.rect (screen, RED, (x + 24*s, y + 14*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 24*s, y + 1   c 8*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 24*s, y + 20*s, s, 3*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 24*s, y + 23*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 24*s, y + 25*s, s, 2*s))
    draw.rect (screen, BUNNY_PURPLE, (x + 24*s, y + 27*s, s, 1*s))    
    draw.rect (screen, RED, (x + 25*s, y + 14*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 25*s, y + 18*s, s, 2*s))
    draw.rect (screen, BUNNY_GREEN, (x + 25*s, y + 20*s, s, 3*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 25*s, y + 23*s, s, 2*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 25*s, y + 25*s, s, 3*s)) 
    draw.rect (screen, RED, (x + 26*s, y + 15*s, s, 3*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 26*s, y + 18*s, s, 3*s))
    draw.rect (screen, BUNNY_GREEN, (x + 26*s, y + 21*s, s, 2*s))    
    draw.rect (screen, BUNNY_TURQUOISE, (x + 26*s, y + 23*s, s, 3*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 26*s, y + 26*s, s, 2*s))
    draw.rect (screen, RED, (x + 27*s, y + 16*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 27*s, y + 20*s, s, 3*s))  
    draw.rect (screen, BUNNY_TURQUOISE, (x + 27*s, y + 23*s, s, 3*s))   
    draw.rect (screen, BUNNY_BLUE, (x + 27*s, y + 26*s, s, s))     
    draw.rect (screen, RED, (x + 28*s, y + 17*s, s, 4*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 28*s, y + 20*s, s, 3*s))  
    draw.rect (screen, BUNNY_GREEN, (x + 28*s, y + 23*s, s, s))  
    draw.rect (screen, BUNNY_TURQUOISE, (x + 28*s, y + 24*s, s, 2*s))      
    draw.rect (screen, RED, (x + 29*s, y + 19*s, s, 2*s))
    draw.rect (screen, BUNNY_ORANGE, (x + 29*s, y + 20*s, s, 3*s))  
    draw.rect (screen, BUNNY_GREEN, (x + 29*s, y + 23*s, s, s))  
    draw.rect (screen, WHITE, (x + 6*s, y + 25*s, s, s))
    draw.rect (screen, WHITE, (x + 5*s, y + 26*s, 2*s, s))
    draw.rect (screen, WHITE, (x + 10*s, y + 25*s, s, 3*s))
    draw.rect (screen, WHITE, (x + 9*s, y + 26*s, s, 2*s))
    draw.rect (screen, WHITE, (x + 8*s, y + 27*s, s, s))
    draw.rect (screen, WHITE, (x + 18*s, y + 26*s, 3*s, s))
    draw.rect (screen, WHITE, (x + 17*s, y + 27*s, 4*s, s))
    
#Draws a bunny ballon made of enlarged pixels
def drawRandomBalloonDay(x, y):
    draw.arc (screen, BLACK, (x + 35, y + 70, 20, 100), 0.5 *pi, 1.5 *pi, 2)
    draw.arc (screen, BLACK, (x + 30, y + 165, 20, 100), 1.5 *pi, 2.5 *pi, 2)    
    draw.rect (screen, WHITE, (x + 10, y + 15, 5, 15))
    draw.rect (screen, WHITE, (x + 15, y + 10, 5, 10))
    draw.rect (screen, WHITE, (x + 65, y + 5, 10, 5))
    draw.rect (screen, WHITE, (x + 60, y + 10, 5, 10))
    draw.rect (screen, WHITE, (x + 55, y + 20, 5, 10))
    draw.rect (screen, WHITE, (x + 50, y + 30, 5, 5))
    draw.rect (screen, WHITE, (x + 20, y + 45, 5, 20))
    draw.rect (screen, WHITE, (x + 25, y + 40, 5, 30))
    draw.rect (screen, WHITE, (x + 30, y + 40, 5, 30))
    draw.rect (screen, WHITE, (x + 35, y + 40, 5, 30))
    draw.rect (screen, WHITE, (x + 40, y + 40, 5, 30))
    draw.rect (screen, WHITE, (x + 45, y + 40, 5, 30))
    draw.rect (screen, WHITE, (x + 50, y + 40, 5, 15))
    draw.rect (screen, WHITE, (x + 55, y + 45, 5, 20))
    draw.rect (screen, WHITE, (x + 5, y + 75, 10, 5))
    draw.rect (screen, WHITE, (x + 65, y + 75, 10, 5))
    draw.rect (screen, BLACK, (x + 10, y + 30, 10, 5))
    draw.rect (screen, BLACK, (x + 5, y + 15, 5, 15))
    draw.rect (screen, BLACK, (x + 10, y + 10, 5, 5))
    draw.rect (screen, BLACK, (x + 15, y + 5, 10, 5))
    draw.rect (screen, BLACK, (x + 25, y + 10, 5, 10))
    draw.rect (screen, BLACK, (x + 30, y + 20, 5, 10))
    draw.rect (screen, BLACK, (x + 35, y + 30, 15, 5))
    draw.rect (screen, BLACK, (x + 50, y + 20, 5, 10))
    draw.rect (screen, BLACK, (x + 55, y + 10, 5, 10))
    draw.rect (screen, BLACK, (x + 60, y + 5, 5, 5))
    draw.rect (screen, BLACK, (x + 65, y + 0, 15, 5))
    draw.rect (screen, BLACK, (x + 80, y + 5, 5, 15))
    draw.rect (screen, BLACK, (x + 75, y + 20, 5, 5))
    draw.rect (screen, BLACK, (x + 70, y + 25, 5, 5))
    draw.rect (screen, BLACK, (x + 65, y + 30, 5, 5))
    draw.rect (screen, BLACK, (x + 50, y + 35, 15, 5))
    draw.rect (screen, BLACK, (x + 60, y + 40, 5, 5))
    draw.rect (screen, BLACK, (x + 65, y + 45, 5, 25))
    draw.rect (screen, BLACK, (x + 60, y + 70, 15, 5))
    draw.rect (screen, BLACK, (x + 75, y + 75, 5, 10))
    draw.rect (screen, BLACK, (x + 60, y + 85, 15, 5))
    draw.rect (screen, BLACK, (x + 55, y + 80, 5, 5))
    draw.rect (screen, BLACK, (x + 15, y + 75, 50, 5))
    draw.rect (screen, BLACK, (x + 5, y + 70, 15, 5))
    draw.rect (screen, BLACK, (x + 0, y + 75, 5, 10))
    draw.rect (screen, BLACK, (x + 5, y + 85, 15, 5))
    draw.rect (screen, BLACK, (x + 20, y + 80, 5, 5))
    draw.rect (screen, BLACK, (x + 10, y + 45, 5, 30))
    draw.rect (screen, BLACK, (x + 15, y + 40, 5, 5))
    draw.rect (screen, BLACK, (x + 20, y + 35, 5, 5))
    draw.rect (screen, GREY, (x + 15, y + 20, 5, 10))
    draw.rect (screen, GREY, (x + 20, y + 10, 5, 25))
    draw.rect (screen, DARK_GREY, (x + 20, y + 25, 5, 5))
    draw.rect (screen, GREY, (x + 25, y + 20, 5, 20))
    draw.rect (screen, PINK, (x + 25, y + 25, 5, 10))
    draw.rect (screen, GREY, (x + 30, y + 30, 5, 10))
    draw.rect (screen, GREY, (x + 35, y + 35, 15, 5))
    draw.rect (screen, GREY, (x + 75, y + 5, 5, 15))
    draw.rect (screen, GREY, (x + 70, y + 15, 5, 10))
    draw.rect (screen, GREY, (x + 65, y + 25, 5, 5))
    draw.rect (screen, GREY, (x + 60, y + 30, 5, 5))
    draw.rect (screen, GREY, (x + 20, y + 40, 5, 5))
    draw.rect (screen, PINK, (x + 65, y + 10, 10, 5))
    draw.rect (screen, PINK, (x + 65, y + 10, 5, 15))
    draw.rect (screen, PINK, (x + 60, y + 20, 10, 5))
    draw.rect (screen, PINK, (x + 60, y + 20, 5, 10))
    draw.rect (screen, PINK, (x + 55, y + 30, 5, 5))
    draw.rect (screen, GREY, (x + 55, y + 40, 5, 5))
    draw.rect (screen, GREY, (x + 60, y + 45, 5, 25))
    draw.rect (screen, GREY, (x + 15, y + 45, 5, 25))
    draw.rect (screen, GREY, (x + 20, y + 70, 40, 5))
    draw.rect (screen, GREY, (x + 5, y + 80, 15, 5))
    draw.rect (screen, GREY, (x + 60, y + 80, 15, 5))
    draw.rect (screen, PINK, (x + 20, y + 65, 10, 5))
    draw.rect (screen, PINK, (x + 50, y + 65, 10, 5))
    draw.rect (screen, BLACK, (x + 25, y + 55, 5, 10))
    draw.rect (screen, BLACK, (x + 50, y + 55, 5, 10))

#Draws the wooden fence which is apart of the background
def drawFence(x):
    draw.polygon (screen, NDIRT_BROWN, [(x, 500),(x, 440),(x + 10, 430),(x + 20, 440),(x + 20, 500)], 0)
    draw.polygon (screen, NDIRT_DARKBROWN, [(x, 500),(x, 440),(x + 10, 430),(x + 20, 440),(x + 20, 500)], 3)
    draw.rect (screen, NDIRT_BROWN, (x + 20, 460, 10, 15), 0)
    draw.rect (screen, NDIRT_DARKBROWN, (x + 20, 460, 10, 15), 3)
    
#Draws the wheat roll beside the barn
def drawWheatRoll():
    draw.rect (screen, WHEAT_YELLOW, (100, 480, 80, 60), 0)
    draw.ellipse (screen, WHEAT_YELLOW, (90, 480, 20, 60), 0)
    draw.ellipse (screen, WHEAT_OUTLINE, (90, 480, 20, 60), 4)
    draw.ellipse (screen, WHEAT_YELLOW, (170, 480, 20, 60), 0)
    draw.arc (screen, WHEAT_OUTLINE, (170, 480, 20, 60), 1.5 *pi, 2.5 *pi, 4)
    draw.arc (screen, WHEAT_OUTLINE, (130, 480, 20, 60), 1.75 *pi, 2.5 *pi, 2)
    draw.arc (screen, WHEAT_OUTLINE, (145, 480, 20, 60), 1.50 *pi, 2.25 *pi, 2)

#Draws the tractor beside the barn
def drawTractor():
    global TRACTOR_GREEN, TRACTOR_WHEEL, TRACTOR_WHEELTRIM
    #Changes the colors used if night time
    if day == False:
        TRACTOR_GREEN = NTRACTOR_GREEN
        TRACTOR_WHEELTRIM = NTRACTOR_WHEELTRIM
        TRACTOR_WHEEL = NTRACTOR_WHEEL
    draw.ellipse (screen, TRACTOR_GREEN, (790, 390, 100, 25), 0)
    draw.polygon (screen, BARN_CONNECTOR, [(730, 470), (730, 440), (735, 440),(735, 410), (740, 410), (740, 440), (745, 440), (745, 470)])
    draw.ellipse (screen, TRACTOR_GREEN, (710, 465, 150, 15), 0)
    draw.polygon (screen, TRACTOR_GREEN, [(700, 540),(700, 480),(710, 470),(790, 470),(800, 400),(880, 400),(890, 475),(900, 475),(910, 480),(910, 540),(850, 560),(710, 560)])
    draw.polygon (screen, STONE_GREY, [(795, 470),(805, 410),(840, 410),(840, 520),(795, 520)], 0)
    draw.polygon (screen, STONE_GREY, [(845, 500),(845, 410),(875, 410),(885, 510),(885, 500)], 0)
    draw.ellipse (screen, STONE_GREY, (790, 470, 15, 50), 0)
    draw.arc (screen, TRACTOR_GREEN, (815, 495, 110, 110), 0.25 *pi, 1 *pi, 5)
    draw.ellipse (screen, TRACTOR_WHEEL, (820, 500, 100, 100), 0)
    draw.ellipse (screen, TRACTOR_WHEELTRIM, (845, 525, 50, 50), 0)
    draw.ellipse (screen, TRACTOR_WHEEL, (700, 540, 60, 60), 0)
    draw.ellipse (screen, TRACTOR_WHEELTRIM, (715, 555, 30, 30), 0)
    
#Drawing the dirt trail by repeatedly drawing lines of random dirts to form a trail
def drawDirtTrail(minX, maxX, Y):
    global dirtCounter, DIRT_FILL, DIRT_OUTLINE
    if day == True:
        DIRT_FILL = DIRT_BROWN
        DIRT_OUTLINE = DIRT_DARKBROWN
    else:
        DIRT_FILL = NDIRT_BROWN
        DIRT_OUTLINE = NDIRT_DARKBROWN
    while dirtCounter < 20:
        x = randint(minX, maxX)
        y = Y
        draw.ellipse (screen, DIRT_FILL, (x, y - 10, 20, 10), 0)
        draw.ellipse (screen, DIRT_OUTLINE, (x, y - 10, 20, 10), 2)
        draw.ellipse (screen, DIRT_FILL, (x + 15, y - 5, 15, 7), 0)
        draw.ellipse (screen, DIRT_OUTLINE, (x + 15, y - 5, 15, 7), 1)
        randomStoneX = x + randint(-20, 20)
        randomStoneY = y + randint(-20, 20)
        draw.ellipse (screen, DIRT_FILL, (randomStoneX, randomStoneY, 15, 7), 0)
        draw.ellipse (screen, DIRT_OUTLINE, (randomStoneX, randomStoneY, 15, 7), 1)        
        dirtCounter = dirtCounter + 1    
    dirtCounter = 0

#Draws 4 random rabbits on the field
def drawRandomRabbit():
    global rabbitCounter
    while rabbitCounter < 5:
        x = randint(0, 700)
        y = randint(500, 700)
        draw.ellipse (screen, WHITE, (x, y, 50, 30), 0)
        draw.ellipse (screen, GREY, (x, y, 50, 30), 4)
        draw.ellipse (screen, WHITE, (x + 30, y - 10, 25, 25), 0)
        draw.ellipse (screen, GREY, (x + 30, y - 10, 25, 25), 3)
        draw.ellipse (screen, WHITE, (x + 32, y - 20, 10, 20), 0)
        draw.ellipse (screen, GREY, (x + 32, y - 20, 10, 20), 3)
        draw.ellipse (screen, WHITE, (x + 44, y - 20, 10, 20), 0)
        draw.ellipse (screen, GREY, (x + 44, y - 20, 10, 20), 3)      
        draw.ellipse (screen, WHITE, (x + 28, y + 16, 15, 20), 0)
        draw.ellipse (screen, GREY, (x + 28, y + 16, 15, 20), 3)
        draw.ellipse (screen, WHITE, (x + 6, y + 16, 15, 20), 0)
        draw.ellipse (screen, GREY, (x + 6, y + 16, 15, 20), 3)
        draw.ellipse (screen, WHITE, (x + 3, y, 10, 10), 0)
        draw.ellipse (screen, GREY, (x + 3, y, 10, 10), 2)
        rabbitCounter = rabbitCounter + 1

#Draws random groups of stones
def drawRandomStone():
    global stoneCounter, STONE_FILL, STONE_OUTLINE
    if day == True:
        STONE_FILL = STONE_GREY
        STONE_OUTLINE = STONE_BLACK
    else:
        STONE_FILL = NSTONE_GREY
        STONE_OUTLINE = NSTONE_BLACK
    while stoneCounter < 10:
        x = randint(0, 1000)
        y = randint(550, 700)        
        draw.ellipse (screen, STONE_FILL, (x, y - 10, 20, 10), 0)
        draw.ellipse (screen, STONE_OUTLINE, (x, y - 10, 20, 10), 2)
        draw.ellipse (screen, STONE_FILL, (x + 15, y - 5, 15, 7), 0)
        draw.ellipse (screen, STONE_OUTLINE, (x + 15, y - 5, 15, 7), 1)
        randomStoneX = x + randint(-20, 20)
        randomStoneY = y + randint(-20, 20)
        draw.ellipse (screen, STONE_FILL, (randomStoneX, randomStoneY, 15, 7), 0)
        draw.ellipse (screen, STONE_OUTLINE, (randomStoneX, randomStoneY, 15, 7), 1)        
        stoneCounter = stoneCounter + 1

#Function to draw random eggs with random colors
def drawRandomEgg():
    global eggCounter
    while eggCounter < 5:
        x = randint(0, 1000)
        y = randint(550, 700)
        draw.ellipse (screen, PINK, (x, y - 10, 20, 30), 0)
        draw.ellipse (screen, BLUE, (x, y - 10, 20, 30), 2)
        draw.ellipse (screen, VIOLET, (x + 15, y + 5, 20, 15), 0)
        draw.ellipse (screen, BLUE, (x + 15, y + 5, 20, 15), 1)
        randomStoneX = x + randint(-20, 20)
        randomStoneY = y + randint(-2, 10)
        draw.ellipse (screen, VIOLET, (randomStoneX, randomStoneY, 8, 10), 0)
        draw.ellipse (screen, BLUE, (randomStoneX, randomStoneY, 8, 10), 1)        
        eggCounter = eggCounter + 1
    
#Function to draw random birds with radious of 1 to 3 in the background
def drawRandomBalloonNight():
    global balloonCounter
    while balloonCounter < 15:
        x = randint(0, 1000)
        y = randint(0, 400)
        draw.arc (screen, WHITE, (x - 5, y + 20, 10, 20), 0.5 *pi, 1.5 *pi, 2)
        draw.arc (screen, WHITE, (x - 5, y + 40, 10, 20), 1.5 *pi, 2.5 *pi, 2)
        draw.ellipse (screen, PINK, (x - 10, y - 10, 20, 30), 0)
        draw.arc (screen, BLUE, (x - 10, y - 10, 20, 30), 0, 2*pi, 2)
        draw.arc (screen, VIOLET, (x - 10, y - 15, 20, 30), 1.20 *pi, 1.80 *pi, 2)
        draw.arc (screen, ORANGE, (x - 10, y - 24, 20, 30), 1.20 *pi, 1.80 *pi, 2)
        balloonCounter = balloonCounter + 1
        
#Function to draw random circles with radious of 1 to 3 in the background
def drawRandomStars():
    global starCounter
    while starCounter < 30:
        radious = randint(1, 3)
        x = randint(0, 1000)
        y = randint(0, 500)
        draw.circle (screen, WHITE, (x,y), radious, 0)
        starCounter = starCounter + 1

#Chooses and draws a background randomely between day and night 
def drawBackground():
    global day
    fenceCount = 0
    x = randint (0, 1)
    if x == 0:
        #Day Time Background
        draw.rect (screen, SKY_BLUE, (0, 0, 1000, 500))
        draw.rect (screen, GREEN, (0, 500, 1000, 300))
        draw.circle (screen, SUN_YELLOW, (825, 120), randint(40, 60), 0)
        while fenceCount < 35:
            drawFence(fenceCount *30)
            fenceCount = fenceCount + 1
        day = True
    else:
        #Night Time Background
        draw.rect (screen, SKY_DARKBLUE, (0, 0, 1000, 500))
        draw.rect (screen, DARK_GREEN, (0, 500, 1000, 300))
        draw.circle (screen, MOON_GREY, (825, 120), randint(40, 60), 0)
        draw.circle (screen, SKY_DARKBLUE, (800, 140), randint(40, 60), 0)
        while fenceCount < 35:
            drawFence(fenceCount *30)
            fenceCount = fenceCount + 1        
        day = False

#Draws the barn infront of the background, choosing between day or night colors by the time of the background
def drawBarn():
    if day == True:
        #Drawing side barn with darker colors
        draw.polygon (screen, SIDEBARN_BROWN, [(520, 360),(520, 500),(730, 500),(730, 360)])
        draw.polygon (screen, BARN_ROOF, [(470, 250),(520, 360),(740, 360),(740, 250)], 0)
        draw.polygon (screen, BARN_SHADEROOF, [(500, 300),(520, 360),(740, 360),(740, 300)], 0)
        draw.line (screen, BARN_CONNECTOR, (500, 300), (740, 300), 5)
        draw.line (screen, BARN_CONNECTOR, (460, 250),(740, 250),5)
        draw.line (screen, BARN_CONNECTOR, (740, 250),(740, 360),5)
        draw.line (screen, BARN_CONNECTOR, (520, 360),(740, 360),5)
        draw.line (screen, BARN_VENT, (680, 382), (720, 382), 1)
        draw.line (screen, BARN_VENT, (680, 384), (720, 384), 1)
        draw.line (screen, BARN_VENT, (680, 386), (720, 386), 1)
        draw.line (screen, BARN_VENT, (680, 388), (720, 388), 1)
        draw.line (screen, BARN_VENT, (680, 390), (720, 390), 1)
        draw.line (screen, BARN_VENT, (680, 392), (720, 392), 1)
        draw.line (screen, BARN_VENT, (680, 394), (720, 394), 1)
        draw.line (screen, BARN_VENT, (680, 396), (720, 396), 1)
        draw.line (screen, BARN_VENT, (680, 398), (720, 398), 1)
        draw.rect (screen, BARN_CONNECTOR, (680, 380, 40, 20), 4)
        draw.polygon (screen, BARN_ROOF, [(580, 400),(580, 440),(620, 440),(620, 400)], 0)
        draw.polygon (screen, BARN_WINDOW, [(585, 405),(585, 415),(595, 415),(595, 405)], 0)
        draw.polygon (screen, BARN_WINDOW, [(585, 425),(585, 435),(595, 435),(595, 425)], 0)
        draw.polygon (screen, BARN_WINDOW, [(605, 405),(605, 415),(615, 415),(615, 405)], 0)
        draw.polygon (screen, BARN_WINDOW, [(605, 425),(605, 435),(615, 435),(615, 425)], 0)
        draw.polygon (screen, BARN_CONNECTOR, [(580, 400),(580, 440),(620, 440),(620, 400)], 4)
        draw.polygon (screen, BARN_BROWN, [(580, 455),(580, 460),(620, 460),(620, 455)], 0)
        draw.polygon (screen, BARN_CONNECTOR, [(580, 455),(580, 460),(620, 460),(620, 455)], 2)
        draw.line (screen, BARN_CONNECTOR, (600, 400), (600, 440), 2)
        draw.line (screen, BARN_CONNECTOR, (580, 420), (620, 420), 2)
        draw.line (screen, BARN_WINDOW, (640, 490), (660, 490), 2)
        draw.line (screen, BARN_WINDOW, (640, 480), (660, 480), 2)
        draw.line (screen, BARN_WINDOW, (640, 470), (660, 470), 2)
        draw.line (screen, BARN_WINDOW, (640, 460), (660, 460), 2)
        draw.line (screen, BARN_WINDOW, (640, 450), (660, 450), 2)
        draw.line (screen, BARN_WINDOW, (640, 440), (660, 440), 2)
        draw.line (screen, BARN_WINDOW, (640, 430), (660, 430), 2)
        draw.line (screen, BARN_WINDOW, (640, 420), (660, 420), 2)
        draw.line (screen, BARN_WINDOW, (640, 410), (660, 410), 2)
        draw.line (screen, BARN_WINDOW, (640, 400), (660, 400), 2)
        draw.line (screen, BARN_CONNECTOR, (640, 400), (640, 500), 4)
        draw.line (screen, BARN_CONNECTOR, (660, 400), (660, 500), 4)    
        #Drawing front barn with brighter colors
        draw.polygon (screen, BARN_BROWN, [(280, 520),(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 360),(520, 520)], 0)
        draw.polygon (screen, BARN_ROOF, [(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 360),(520, 350), (500, 295), (460, 235), (420, 215), (380, 215), (340, 235), (300, 290), (280, 350)], 0)
        draw.polygon (screen, BARN_CONNECTOR, [(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 362),(520, 352), (500, 290), (460, 235), (420, 215), (380, 215), (340, 235), (300, 290), (280, 350)], 2)
        draw.lines (screen, BARN_ROOF, False,[(340, 520),(340, 380),(460, 380),(460, 520)], 5)
        draw.line (screen, BARN_ROOF, (400, 520), (400, 380), 8)
        draw.polygon (screen, BARN_ROOF, [(340, 380),(340, 390),(390, 520),(400, 520),(400, 510),(350, 380)], 0)
        draw.polygon (screen, BARN_ROOF, [(400, 510),(400, 520),(410, 520),(460, 390),(460, 380),(450, 380)], 0)
        draw.polygon (screen, BARN_ROOF, [(410, 380),(400, 380),(400, 390),(450, 520),(460, 520),(460, 510)], 0)
        draw.polygon (screen, BARN_ROOF, [(390, 380),(400, 380),(400, 390),(350, 520),(340, 520),(340, 510)], 0)
        draw.polygon (screen, BARN_ROOF, [(280, 500),(280, 490),(310, 520),(300, 520)], 0)
        draw.polygon (screen, BARN_ROOF, [(520, 500),(500, 520),(490, 520),(520, 490)], 0)
        draw.line (screen, BARN_BROWN, (400, 520), (400, 370), 2)
        draw.polygon (screen, BARN_ROOF, [(400, 240),(360, 270),(370, 320),(430, 320), (440, 270)], 0)
        draw.polygon (screen, SIDEBARN_BROWN, [(400, 250),(370, 274),(376, 314),(424, 314), (430, 274)], 0)
        draw.polygon (screen, BARN_CONNECTOR, [(400, 240),(360, 270),(370, 320),(430, 320), (440, 270)], 4)
        draw.polygon (screen, BARN_CONNECTOR, [(400, 250),(370, 274),(376, 314),(424, 314), (430, 274)], 4)
        #Draws stone on the side of the barn for decoration
        draw.ellipse (screen, STONE_FILL, (250, 495, 40, 30), 0)
        draw.ellipse (screen, STONE_OUTLINE, (250, 495, 40, 30), 4)        
        draw.ellipse (screen, STONE_FILL, (280, 515, 20, 10), 0)
        draw.ellipse (screen, STONE_OUTLINE, (280, 515, 20, 10), 2)
    else:
        draw.polygon (screen, NSIDEBARN_BROWN, [(520, 360),(520, 500),(730, 500),(730, 360)])
        draw.polygon (screen, NBARN_ROOF, [(470, 250),(520, 360),(740, 360),(740, 250)], 0)
        draw.polygon (screen, NBARN_SHADEROOF, [(500, 300),(520, 360),(740, 360),(740, 300)], 0)
        draw.line (screen, NBARN_CONNECTOR, (500, 300), (740, 300), 5)
        draw.line (screen, NBARN_CONNECTOR, (460, 250),(740, 250),5)
        draw.line (screen, NBARN_CONNECTOR, (740, 250),(740, 360),5)
        draw.line (screen, NBARN_CONNECTOR, (520, 360),(740, 360),5)
        draw.line (screen, NBARN_VENT, (680, 382), (720, 382), 1)
        draw.line (screen, NBARN_VENT, (680, 384), (720, 384), 1)
        draw.line (screen, NBARN_VENT, (680, 386), (720, 386), 1)
        draw.line (screen, NBARN_VENT, (680, 388), (720, 388), 1)
        draw.line (screen, NBARN_VENT, (680, 390), (720, 390), 1)
        draw.line (screen, NBARN_VENT, (680, 392), (720, 392), 1)
        draw.line (screen, NBARN_VENT, (680, 394), (720, 394), 1)
        draw.line (screen, NBARN_VENT, (680, 396), (720, 396), 1)
        draw.line (screen, NBARN_VENT, (680, 398), (720, 398), 1)
        draw.rect (screen, NBARN_CONNECTOR, (680, 380, 40, 20), 4)
        draw.polygon (screen, NBARN_ROOF, [(580, 400),(580, 440),(620, 440),(620, 400)], 0)
        draw.polygon (screen, NBARN_WINDOW, [(585, 405),(585, 415),(595, 415),(595, 405)], 0)
        draw.polygon (screen, NBARN_WINDOW, [(585, 425),(585, 435),(595, 435),(595, 425)], 0)
        draw.polygon (screen, NBARN_WINDOW, [(605, 405),(605, 415),(615, 415),(615, 405)], 0)
        draw.polygon (screen, NBARN_WINDOW, [(605, 425),(605, 435),(615, 435),(615, 425)], 0)
        draw.polygon (screen, NBARN_CONNECTOR, [(580, 400),(580, 440),(620, 440),(620, 400)], 4)
        draw.polygon (screen, NBARN_BROWN, [(580, 455),(580, 460),(620, 460),(620, 455)], 0)
        draw.polygon (screen, NBARN_CONNECTOR, [(580, 455),(580, 460),(620, 460),(620, 455)], 2)
        draw.line (screen, NBARN_CONNECTOR, (600, 400), (600, 440), 2)
        draw.line (screen, NBARN_CONNECTOR, (580, 420), (620, 420), 2)
        draw.line (screen, NBARN_WINDOW, (640, 490), (660, 490), 2)
        draw.line (screen, NBARN_WINDOW, (640, 480), (660, 480), 2)
        draw.line (screen, NBARN_WINDOW, (640, 470), (660, 470), 2)
        draw.line (screen, NBARN_WINDOW, (640, 460), (660, 460), 2)
        draw.line (screen, NBARN_WINDOW, (640, 450), (660, 450), 2)
        draw.line (screen, NBARN_WINDOW, (640, 440), (660, 440), 2)
        draw.line (screen, NBARN_WINDOW, (640, 430), (660, 430), 2)
        draw.line (screen, NBARN_WINDOW, (640, 420), (660, 420), 2)
        draw.line (screen, NBARN_WINDOW, (640, 410), (660, 410), 2)
        draw.line (screen, NBARN_WINDOW, (640, 400), (660, 400), 2)
        draw.line (screen, NBARN_CONNECTOR, (640, 400), (640, 500), 4)
        draw.line (screen, NBARN_CONNECTOR, (660, 400), (660, 500), 4)    
        #Drawing front barn with brighter colors
        draw.polygon (screen, NBARN_BROWN, [(280, 520),(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 360),(520, 520)], 0)
        draw.polygon (screen, NBARN_ROOF, [(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 360),(520, 350), (500, 295), (460, 235), (420, 215), (380, 215), (340, 235), (300, 290), (280, 350)], 0)
        draw.polygon (screen, NBARN_CONNECTOR, [(280, 360),(300, 300),(340, 240),(380, 220),(420, 220),(460, 240),(500, 300),(520, 362),(520, 352), (500, 290), (460, 235), (420, 215), (380, 215), (340, 235), (300, 290), (280, 350)], 2)
        draw.lines (screen, NBARN_ROOF, False,[(340, 520),(340, 380),(460, 380),(460, 520)], 5)
        draw.line (screen, NBARN_ROOF, (400, 520), (400, 380), 8)
        draw.polygon (screen, NBARN_ROOF, [(340, 380),(340, 390),(390, 520),(400, 520),(400, 510),(350, 380)], 0)
        draw.polygon (screen, NBARN_ROOF, [(400, 510),(400, 520),(410, 520),(460, 390),(460, 380),(450, 380)], 0)
        draw.polygon (screen, NBARN_ROOF, [(410, 380),(400, 380),(400, 390),(450, 520),(460, 520),(460, 510)], 0)
        draw.polygon (screen, NBARN_ROOF, [(390, 380),(400, 380),(400, 390),(350, 520),(340, 520),(340, 510)], 0)
        draw.polygon (screen, NBARN_ROOF, [(280, 500),(280, 490),(310, 520),(300, 520)], 0)
        draw.polygon (screen, NBARN_ROOF, [(520, 500),(500, 520),(490, 520),(520, 490)], 0)
        draw.line (screen, NBARN_BROWN, (400, 520), (400, 370), 2)
        draw.polygon (screen, NBARN_ROOF, [(400, 240),(360, 270),(370, 320),(430, 320), (440, 270)], 0)
        draw.polygon (screen, NSIDEBARN_BROWN, [(400, 250),(370, 274),(376, 314),(424, 314), (430, 274)], 0)
        draw.polygon (screen, NBARN_CONNECTOR, [(400, 240),(360, 270),(370, 320),(430, 320), (440, 270)], 4)
        draw.polygon (screen, NBARN_CONNECTOR, [(400, 250),(370, 274),(376, 314),(424, 314), (430, 274)], 4)  
        draw.ellipse (screen, STONE_FILL, (250, 495, 40, 30), 0)
        draw.ellipse (screen, STONE_OUTLINE, (250, 495, 40, 30), 4)
        draw.ellipse (screen, STONE_FILL, (280, 515, 20, 10), 0)
        draw.ellipse (screen, STONE_OUTLINE, (280, 515 , 20, 10), 2)            

#Excecuting the predefined functions
drawBackground()
drawRandomStone()
if day == True:
    drawDirtTrail(350, 450, 520)
    drawDirtTrail(340, 440, 530)
    drawDirtTrail(330, 430, 540)
    drawDirtTrail(320, 420, 550)    
    drawDirtTrail(310, 410, 560)
    drawDirtTrail(300, 400, 570) 
    drawDirtTrail(295, 395, 580)
    drawDirtTrail(300, 400, 590) 
    drawDirtTrail(310, 410, 600) 
    drawDirtTrail(320, 420, 610) 
    drawDirtTrail(330, 430, 620) 
    drawDirtTrail(340, 440, 630) 
    drawDirtTrail(350, 450, 640)
    drawDirtTrail(355, 455, 650)
    drawDirtTrail(350, 450, 660)
    drawDirtTrail(340, 440, 670)
    drawDirtTrail(330, 430, 680)    
    drawDirtTrail(320, 420, 690)
    drawDirtTrail(310, 410, 700)     
    drawBarn()
    drawRandomEgg()
    drawWheatRoll()
    drawTractor()
    drawRandomPixelRabbit(randint(0, 600), randint(450, 650), randint(2, 4))
    drawRandomPixelRabbit(randint(0, 600), randint(450, 650), randint(2, 4))
    drawRandomPixelRabbit(randint(0, 600), randint(450, 650), randint(2, 4))
    drawRandomPixelRabbit(randint(0, 600), randint(450, 650), randint(2, 4))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
    drawRandomBalloonDay(randint(0, 800), randint(0, 350))
else:
    drawRandomStars()
    drawDirtTrail(350, 450, 520)
    drawDirtTrail(340, 440, 530)
    drawDirtTrail(330, 430, 540)
    drawDirtTrail(320, 420, 550)
    drawDirtTrail(310, 410, 560) 
    drawDirtTrail(300, 400, 570) 
    drawDirtTrail(295, 395, 580) 
    drawDirtTrail(300, 400, 590) 
    drawDirtTrail(310, 410, 600) 
    drawDirtTrail(320, 420, 610)
    drawDirtTrail(330, 430, 620) 
    drawDirtTrail(340, 440, 630) 
    drawDirtTrail(350, 450, 640)
    drawDirtTrail(355, 455, 650)
    drawDirtTrail(350, 450, 660)
    drawDirtTrail(340, 440, 670)
    drawDirtTrail(330, 430, 680)
    drawDirtTrail(320, 420, 690)
    drawDirtTrail(310, 410, 700)    
    drawBarn()
    drawRandomEgg()
    drawWheatRoll()
    drawTractor()
    drawRandomRabbit()
    drawRandomBalloonNight()
display.flip()


time.wait(10000)
quit()
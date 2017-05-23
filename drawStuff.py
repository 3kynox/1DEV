import os, sys, pygame
from pygame.locals import *
from pygame.color import *

pygame.init()

# Fonts
font1 = pygame.font.SysFont('Geneva',40, True)
font2 = pygame.font.SysFont('Geneva',100, True)
font3 = pygame.font.SysFont('Geneva',18, True)
caps = pygame.font.SysFont('Geneva',140, True)

# Colors
White = 255, 255, 255
Red = 255, 0, 0
Green = 0, 255, 0
Purple = 65, 28, 139
Blue = 0, 0, 255
Black = 0, 0, 0

def drawStuff(surface):
    # Text
    surface.blit(font1.render('1', False, White),[110,20])
    surface.blit(font1.render('2', False, White),[110,120])
    surface.blit(font1.render('3', False, White),[110,220])
    surface.blit(font1.render('4', False, White),[110,320])
    surface.blit(font1.render('CREDITS', False, White),[0,690])
    surface.blit(font1.render('BALL', False, White),[150,690])

    ### IMAGES ###

    # Left panel
    pygame.draw.rect(surface, Blue,[20,50,200,40],2)
    pygame.draw.rect(surface, Blue,[20,150,200,40],2)
    pygame.draw.rect(surface, Blue,[20,250,200,40],2)
    pygame.draw.rect(surface, Blue,[20,350,200,40],2)
    pygame.draw.rect(surface, Blue,[20,720,80,40],2)
    pygame.draw.rect(surface, Blue,[150,720,80,40],2)

    # Plane 1
    plane1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/avion_1.png"))
    surface.blit(plane1, [10,550])

    # Plane 2
    plane2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/avion_2.png"))
    surface.blit(plane2, [760, 200])

    # Inner-left
    pygame.draw.polygon(surface, Blue, [[340,520],[340,610],[335,620],[350,650],[385,660],[400,645]])
    pygame.draw.rect(surface, Purple, [254,520,30,10])
    pygame.draw.rect(surface, Purple, [300,520,30,10])
    pygame.draw.line(surface, Purple, [280,530],[302,530], 2)
    pygame.draw.line(surface, Purple, [280,523],[333,523], 2)
    pygame.draw.line(surface, Blue, [333,523],[338,523], 2)
    pygame.draw.line(surface, Green, [265,535],[265,545], 2)
    pygame.draw.line(surface, Green, [290,535],[290,545], 2)
    pygame.draw.line(surface, Green, [310,535],[310,545], 2)
    pygame.draw.line(surface, Red, [330,535],[330,545], 2)
    surface.blit(font3.render('D    R   O  P', True, White),[259,505])
    surface.blit(pygame.transform.rotate(font3.render('300', True, Green),270),[305,555])
    surface.blit(font3.render('LIT', True, Green),[280,480])
    surface.blit(font3.render('5000', True, Green),[275,465])


    ## inner-right
    pygame.draw.circle(surface, White, [721,147], 4)
    pygame.draw.line(surface, Purple, [695,690],[695,768],2)
    pygame.draw.polygon(surface, Blue, [[590,635],[610,660],[660,640],[660,540],[650,520]])
    pygame.draw.polygon(surface, Purple, [[670,490],[680,470],[690,500],[690,530]])


    ## right trigger
    pygame.draw.polygon(surface, Green, [[590,690],[630,690],[640,705],[640,690],[693,690],[693,655]])


    ## left trigger
    pygame.draw.polygon(surface, Green, [[300,600],[300,690],[340,690],[340,705],[350,690],[400,690],[330,670]])

    ## Top-left module
    pygame.draw.polygon(surface, White, [[318,240],[365,240],[365,120],[380,100],[410,80],[350,70],[318,100]])
    pygame.draw.circle(surface, Black, [343,170],22)
    pygame.draw.line(surface, Purple, [320,160],[320,180],3)
    pygame.draw.line(surface, Purple, [365,160],[365,180],3)
    pygame.draw.line(surface, White, [400,225],[430,225],4)


    ## Right panel --peut mieux faire
    surface.blit(font1.render('subLOGIC', False, Purple),[800,10])
    surface.blit(caps.render('N', False, Blue),[760,70])
    surface.blit(font2.render('ight', False, Green),[840,92])
    surface.blit(caps.render('M', False, Green),[940,150])
    surface.blit(font2.render('i', False, Blue),[970,250])
    surface.blit(font2.render('s', False, Blue),[960,300])
    surface.blit(font2.render('s', False, Blue),[960,350])
    surface.blit(font2.render('i', False, Blue),[970,430])
    surface.blit(font2.render('o', False, Blue),[960,480])
    surface.blit(font2.render('n', False, Blue),[960,530])
    pygame.draw.circle(surface, White, [853,95], 13)
    pygame.draw.circle(surface, White, [983,253], 13)
    pygame.draw.circle(surface, White, [983,433], 13)

    ## Boxes
    pygame.draw.rect(surface, White, [760,590,260,80], 2)
    pygame.draw.rect(surface, White, [760,680,260,80], 2)

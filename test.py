"""
@ToDo Describe what's missing
- 1st task ...
"""

__version__ = "$Id:$"
__docformat__ = "reStructuredText"

# -*- coding: utf-8 -*-
import sys, random, pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

pygame.init()

def main():
    # Init vars
    running = True
    clock = pygame.time.Clock()
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Night Mission - PinBall")

    # Images loading
    #surface = pygame.image.load("images/background.jpg")

    # Physics
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    # Balls
    balls = []

    # walls
    static_lines = [pymunk.Segment(space.static_body, (150, 100.0), (50.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (450.0, 100.0), (550.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (50.0, 550.0), (300.0, 600.0), 1.0)
                    ,pymunk.Segment(space.static_body, (300.0, 600.0), (550.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (300.0, 420.0), (400.0, 400.0), 1.0)]

    for line in static_lines:
        line.elasticity = 0.7
        line.group = 1
    space.add(static_lines)

    #Colors
    White = 255,255,255
    Red = 255,0,0
    Green = 0,255,0
    Purple = 164,72,255
    Blue = 0,0,255

    # basic stuff
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Night Mission - PinBall")
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0,0,0))
    font1 = pygame.font.SysFont('Geneva',40, True)
    font2 = pygame.font.SysFont('Geneva',100, True)
    caps = pygame.font.SysFont('Geneva',140,True)
    progress = True

    #left panel
    pygame.draw.rect(surface, Blue,[20,50,200,40],2)
    pygame.draw.rect(surface, Blue,[20,150,200,40],2)
    pygame.draw.rect(surface, Blue,[20,250,200,40],2)
    pygame.draw.rect(surface, Blue,[20,350,200,40],2)
    pygame.draw.rect(surface, Blue,[20,720,80,40],2)
    pygame.draw.rect(surface, Blue,[150,720,80,40],2)

        #text
    surface.blit(font1.render('1', False, White),[110,20])
    surface.blit(font1.render('2', False, White),[110,120])
    surface.blit(font1.render('3', False, White),[110,220])
    surface.blit(font1.render('4', False, White),[110,320])
    surface.blit(font1.render('CREDITS', False, White),[0,690])
    surface.blit(font1.render('BALL', False, White),[150,690])

        #plane 1
    plane1 = pygame.image.load('images/avion1.png')
    surface.blit(plane1, [10,550])

    #pinball
    pygame.draw.line(surface, White, [251,385],[250,768],4)
    pygame.draw.polygon(surface, White, [[250,385],[265,380],[265,50],[280,30],[370,30],[420,0],[250,0]])
    pygame.draw.line(surface, White, [265,0],[655,0],6)
    pygame.draw.polygon(surface, White, [[740,120],[740,768],[750,768],[750,0],[655,0],[655,4],[700,15],[710,25],[720,40],[730,55]])

    #right panel --peut mieux faire
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

        #plane 2
    plane2 = pygame.image.load('images/avion2.png')
    surface.blit(plane2, [760, 200])

        #boxes
    pygame.draw.rect(surface, White, [760,590,260,80], 2)
    pygame.draw.rect(surface, White, [760,680,260,80], 2)



# Main Loop
    while running:
        # Events loop
        for event in pygame.event.get():
            # Manage quit / closing window event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()

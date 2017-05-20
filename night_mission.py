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
    progress = True
    clock = pygame.time.Clock()
    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Night Mission - PinBall")
    surface = pygame.Surface(screen.get_size())
    ### inutile - laisse pour plus tard au besoin ###
    #surface = surface.convert()
    #surface.fill((0,0,0))

    # Physics
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    # Balls
    balls = []

    # Some Walls
    static_lines = [pymunk.Segment(space.static_body, (150, 100.0), (50.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (450.0, 100.0), (550.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (50.0, 550.0), (300.0, 600.0), 1.0)
                    ,pymunk.Segment(space.static_body, (300.0, 600.0), (550.0, 550.0), 1.0)
                    ,pymunk.Segment(space.static_body, (300.0, 420.0), (400.0, 400.0), 1.0)]

    for line in static_lines:
        line.elasticity = 0.7
        line.group = 1
    space.add(static_lines)

    # Fonts
    font1 = pygame.font.SysFont('Geneva',40, True)
    font2 = pygame.font.SysFont('Geneva',100, True)
    caps = pygame.font.SysFont('Geneva',140, True)

    # Colors
    White = 255, 255, 255
    Red = 255, 0, 0
    Green = 0, 255, 0
    Purple = 65, 28, 139
    Blue = 0, 0, 255
    Black = 0, 0, 0

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
    plane1 = pygame.image.load("images/avion_1.png")
    surface.blit(plane1, [10,550])

    # Plane 2
    plane2 = pygame.image.load('images/avion_2.png')
    surface.blit(plane2, [760, 200])

    # Left border
    pygame.draw.line(surface, White, [251,385],[250,768],4)
    pygame.draw.polygon(surface, White, [[250,385],[265,380],[265,50],[280,30],[370,30],[420,0],[250,0]])

    # Inner-left
    pygame.draw.polygon(surface, Blue, [[266,375],[312,358],[266,260]])
    pygame.draw.lines(surface, White, False, [[266,375],[312,358],[266,260]],4)
    pygame.draw.polygon(surface, Blue, [[335,520],[335,610],[330,620],[335,630],[360,645],[370,635]])
    pygame.draw.lines(surface, White, True, [[335,520],[335,610],[330,620],[335,630],[360,645],[370,635]], 3)
    pygame.draw.rect(surface, Purple, [254,540,20,10])
    pygame.draw.rect(surface, Purple, [300,540,20,10])
    pygame.draw.line(surface, Purple, [254,530],[254,560], 2)
    pygame.draw.line(surface, Purple, [270,530],[270,620], 2)
    pygame.draw.line(surface, Purple, [270,542],[300,542], 2)
    pygame.draw.line(surface, Purple, [270,550],[302,550], 2)
    pygame.draw.line(surface, White, [270,620],[298,620], 2)

    # Top border
    pygame.draw.line(surface, White, [265,0],[655,0],6)

    # Right border
    pygame.draw.polygon(surface, White, [[740,120],[740,768],[750,768],[750,0],[655,0],[655,4],[700,15],[710,25],[720,40],[730,55]])
    pygame.draw.lines(surface, White, False, [[715,768],[715,650],[750,650]],2)

    # Inner-right
    pygame.draw.line(surface, Blue,[715,649],[715,150],4)
    pygame.draw.circle(surface, White, [716,153], 4)
    pygame.draw.line(surface, White, [715,150],[735,140],4)
    pygame.draw.polygon(surface, Blue,[[715,470],[690,420],[705,370],[670,320],[715,250]])
    pygame.draw.lines(surface, White, False, [[712,470],[688,420],[703,370],[668,320],[712,250]],4)
    pygame.draw.line(surface, White, [690,650],[715,650],2)
    pygame.draw.line(surface, Purple, [690,690],[690,768],4)
    pygame.draw.polygon(surface, Blue, [[620,650],[630,655],[660,640],[660,550],[655,540]])
    pygame.draw.lines(surface, White, True, [[620,650],[630,655],[660,640],[660,550],[655,540]], 3)
    pygame.draw.polygon(surface, Purple, [[660,470],[670,460],[680,480],[680,520]])
    pygame.draw.lines(surface, White, True, [[660,470],[670,460],[680,480],[680,520]],2)

    # Right trigger
    pygame.draw.polygon(surface, Green, [[590,690],[635,690],[635,705],[650,690],[688,690],[688,655]])
    pygame.draw.lines(surface, White, False, [[590,690],[635,690],[635,705],[650,690],[688,690]],3)
    pygame.draw.lines(surface, White, False, [[690,690],[690,653],[688,655],[688,640]],4)
    pygame.draw.line(surface, Green, [683,660],[683,620],6)

    # Left trigger
    pygame.draw.polygon(surface, Green, [[300,600],[300,690],[340,690],[340,705],[350,690],[400,690],[330,670]])
    pygame.draw.lines(surface, White, True, [[300,600],[300,690],[340,690],[340,705],[350,690],[400,690],[330,670]],3)

    # Top-left module
    pygame.draw.line(surface, White, [292,70],[292,250],6)
    pygame.draw.polygon(surface, White, [[290,250],[320,310],[400,280],[400,250],[293,250]])
    pygame.draw.line(surface, Green, [300,260],[400,260],8)
    pygame.draw.lines(surface, Purple, True, [[305,270],[305,273],[390,273],[395,270]],4)
    pygame.draw.lines(surface, Green, True, [[310,280],[312,284],[370,284],[390,280]],4)
    pygame.draw.polygon(surface, Purple, [[317,290],[325,305],[365,290]])
    pygame.draw.polygon(surface, White, [[393,149],[393,120],[410,110],[410,160],[400,170]])
    pygame.draw.line(surface, Green, [396,249],[396,150],8)
    pygame.draw.polygon(surface, White, [[360,60],[320,100],[320,220],[370,220],[370,110],[400,90]])
    pygame.draw.line(surface, Purple, [366,55],[380,66],3)
    pygame.draw.line(surface, Green, [385,70],[403,83],3)
    pygame.draw.circle(surface, Black,[346,165],24)
    pygame.draw.line(surface, Green, [323,215],[368,215],8)
    pygame.draw.line(surface, Purple, [320,160],[320,170],2)
    pygame.draw.line(surface, Purple, [370,160],[370,170],2)
    pygame.draw.line(surface, White, [400,220],[430,220],6)
    pygame.draw.line(surface, White, [430,210],[430,240],6)

    # Middle module
    pygame.draw.line(surface, White, [450,120],[450,160],6)
    pygame.draw.line(surface, White, [490,110],[490,150],6)
    pygame.draw.line(surface, White, [530,100],[530,140],6)
    pygame.draw.line(surface, White, [570,100],[570,140],6)
    pygame.draw.line(surface, White, [610,110],[610,150],6)
    pygame.draw.line(surface, White, [650,120],[650,160],6)

    # Right panel --peut mieux faire
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

    # Boxes
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

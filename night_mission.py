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
    surface = pygame.image.load("images/background.jpg")

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

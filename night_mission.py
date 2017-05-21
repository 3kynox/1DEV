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
from drawStuff import *

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
    surface = pygame.Surface(screen.get_size())

    # Physics
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    draw_options = pymunk.pygame_util.DrawOptions(surface)

    fp = [(5,-5), (-85, 0), (5,5)]
    mass = 100
    moment = pymunk.moment_for_poly(mass, fp)

    # Balls
    balls = []

    # Global walls (Comment changer la couleur ? Ou rendre invisible ces lignes ?)
    global_walls = [pymunk.Segment(space.static_body, (250, 0), (250, 383), 1.0),
                    pymunk.Segment(space.static_body, (250, 383), (265, 390), 1.0),
                    pymunk.Segment(space.static_body, (265, 390), (265, 718), 1.0),
                    pymunk.Segment(space.static_body, (265, 718), (280, 738), 1.0),
                    pymunk.Segment(space.static_body, (280, 738), (370, 738), 1.0),
                    pymunk.Segment(space.static_body, (370, 738), (415, 765), 1.0),
                    pymunk.Segment(space.static_body, (415, 765), (655, 765), 1.0),
                    pymunk.Segment(space.static_body, (655, 765), (700, 753), 1.0),
                    pymunk.Segment(space.static_body, (700, 753), (732, 713), 1.0),
                    pymunk.Segment(space.static_body, (732, 713), (742, 648), 1.0),
                    pymunk.Segment(space.static_body, (742, 648), (742, 0), 1.0)]

    for line in global_walls:
        line.elasticity = 0.7
        line.group = 1
    space.add(global_walls)

    left_shape = [pymunk.Segment(space.static_body, (280, 258), (280, 168), 1.0),
                   pymunk.Segment(space.static_body, (280, 168), (300, 168), 1.0),
                   pymunk.Segment(space.static_body, (300, 168), (330, 100), 1.0),
                   pymunk.Segment(space.static_body, (330, 100), (375, 87), 1.0)]

    for line in left_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(left_shape)

    right_shape = [pymunk.Segment(space.static_body, (740, 118), (680, 118), 1.0),
                   pymunk.Segment(space.static_body, (680, 118), (680, 114), 1.0),
                   pymunk.Segment(space.static_body, (680, 114), (605, 86), 1.0)]

    for line in right_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(right_shape)

    # "bumpers"
    for p in [(460,570), (650,570), (550, 440)]:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = p
        shape = pymunk.Circle(body, 13)
        shape.elasticity = 1.5
        space.add(shape)

    for p in [(430,430), (550,520)]:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = p
        shape = pymunk.Circle(body, 20)
        shape.elasticity = 1.5
        space.add(shape)

    # Right flipper
    r_flipper_body = pymunk.Body(mass, moment)
    r_flipper_body.position = 600, 82
    r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
    space.add(r_flipper_body, r_flipper_shape)

    r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    r_flipper_joint_body.position = r_flipper_body.position
    j = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0,0), (0,0))
    s = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.15, 20000000,900000)
    space.add(j, s)

    # Left flipper
    l_flipper_body = pymunk.Body(mass, moment)
    l_flipper_body.position = 380, 82
    l_flipper_shape = pymunk.Poly(l_flipper_body, [(-x,y) for x,y in fp])
    space.add(l_flipper_body, l_flipper_shape)

    l_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    l_flipper_joint_body.position = l_flipper_body.position
    j = pymunk.PinJoint(l_flipper_body, l_flipper_joint_body, (0,0), (0,0))
    s = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.15, 20000000, 900000)
    space.add(j, s)

    r_flipper_shape.group = l_flipper_shape.group = 1
    r_flipper_shape.elasticity = l_flipper_shape.elasticity = 0.4

    ### Main Loop ###
    while running:
        ### Clear screen and draw stuff
        surface.fill((0, 0, 0))
        drawStuff(surface)

        # Define mouse position
        mouseX = pygame.mouse.get_pos()[1]
        mouseY = pygame.mouse.get_pos()[0]

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
                elif event.key == K_j:
                    r_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * 40000, (-100,0))
                elif event.key == K_f:
                    l_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * -40000, (-100,0))
                elif event.type == KEYDOWN and event.key == K_b:
                    mass = 1
                    radius = 10
                    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
                    body = pymunk.Body(mass, inertia)
                    x = random.randint(350,600)
                    body.position = x, 400
                    shape = pymunk.Circle(body, radius, (0,0))
                    shape.elasticity = 0.95
                    space.add(body, shape)
                    balls.append(shape)

        # Display Rasta Rockets
        space.debug_draw(draw_options)

        r_flipper_body.position = 600, 82
        l_flipper_body.position = 380, 82
        r_flipper_body.velocity = l_flipper_body.velocity = 0,0

        # Remove any balls outside
        to_remove = []
        for ball in balls:
            if ball.body.position.get_distance((300,300)) > 1000:
                to_remove.append(ball)

        for ball in to_remove:
            space.remove(ball.body, ball)
            balls.remove(ball)

        # Update physics
        dt = 1.0/60.0/5.
        for x in range(5):
            space.step(dt)

        clock.tick(50)
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.set_caption("Night Mission - PinBall - " + "FPS: " + str(clock.get_fps()) + " - Mouse Position : " + "mouseX: {0} - mouseY: {1}".format(mouseX, mouseY))

if __name__ == '__main__': main()

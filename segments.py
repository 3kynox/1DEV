import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

# Colors
White = 255, 255, 255
Red = 255, 0, 0
Green = 0, 255, 0
Purple = 65, 28, 139
Blue = 0, 0, 255
Black = 0, 0, 0

def drawSegments(space):
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
                   pymunk.Segment(space.static_body, (330, 100), (375, 87), 1.0),
                   pymunk.Segment(space.static_body, (340, 248), (340, 158), 1.0),
                   pymunk.Segment(space.static_body, (340, 158), (335, 147), 1.0),
                   pymunk.Segment(space.static_body, (335, 147), (350, 118), 1.0),
                   pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                   pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                   pymunk.Segment(space.static_body, (385, 108), (400, 123), 1.0),
                   pymunk.Segment(space.static_body, (303, 258), (303, 228), 1.0),
                   pymunk.Segment(space.static_body, (325, 258), (325, 228), 1.0)]

    for line in left_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(left_shape)

    right_shape = [pymunk.Segment(space.static_body, (740, 118), (680, 118), 1.0),
                   pymunk.Segment(space.static_body, (680, 118), (680, 114), 1.0),
                   pymunk.Segment(space.static_body, (680, 114), (605, 86), 1.0),
                   pymunk.Segment(space.static_body, (650, 248), (660, 228), 1.0),
                   pymunk.Segment(space.static_body, (660, 228), (660, 128), 1.0),
                   pymunk.Segment(space.static_body, (660, 128), (610, 108), 1.0),
                   pymunk.Segment(space.static_body, (610, 108), (590, 133), 1.0),
                   pymunk.Segment(space.static_body, (680, 298), (690, 270), 1.0),
                   pymunk.Segment(space.static_body, (690, 270), (690, 240), 1.0),
                   pymunk.Segment(space.static_body, (690, 240), (670, 278), 1.0),
                   pymunk.Segment(space.static_body, (670, 278), (680, 298), 1.0)]

    for line in right_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(right_shape)

    # Much elasticity for that ones
    left_right_panes = [pymunk.Segment(space.static_body, (340, 248), (400, 123), 1.0),
                        pymunk.Segment(space.static_body, (650, 248), (590, 133), 1.0)]

    for line in left_right_panes:
        line.elasticity = 1.2
        line.group = 1
    space.add(left_right_panes)

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

    ## Colors
White = 255, 255, 255
Red = 255, 0, 0
Green = 0, 255, 0
Purple = 65, 28, 139
Blue = 0, 0, 255
Black = 0, 0, 0

    ## Poly's body_type
b = pymunk.Body(body_type=pymunk.Body.STATIC)

    ## C'est parti ...
def drawSegments(space):
    global_walls = [pymunk.Segment(space.static_body, (250, 0), (250, 390), 2),
                    pymunk.Segment(space.static_body, (250, 384), (264, 393), 4),
                    pymunk.Segment(space.static_body, (256, 390), (256, 768), 8),
                    pymunk.Segment(space.static_body, (260, 730), (280, 745), 8),
                    pymunk.Segment(space.static_body, (278, 738), (370, 738), 4),
                    pymunk.Segment(space.static_body, (370, 738), (415, 765), 4),
                    pymunk.Segment(space.static_body, (415, 765), (750, 765), 4),
                    pymunk.Segment(space.static_body, (655, 768), (700, 753), 8),
                    pymunk.Segment(space.static_body, (700, 753), (735, 720), 8),
                    pymunk.Segment(space.static_body, (725, 768), (750, 648), 4),
                    pymunk.Segment(space.static_body, (750, 768), (750, 0), 6),
                    pymunk.Segment(space.static_body, (702, 752), (730, 752), 9),
                    pymunk.Segment(space.static_body, (265, 391), (302, 412), 2),
                    pymunk.Segment(space.static_body, (302, 411), (264, 505), 2),
                    pymunk.Segment(space.static_body, (718, 500), (678, 450), 2),
                    pymunk.Segment(space.static_body, (678, 450), (718, 400), 2),
                    pymunk.Segment(space.static_body, (718, 412), (697, 382), 2),
                    pymunk.Segment(space.static_body, (697, 382), (718, 309), 2),
                    pymunk.Segment(space.static_body, (290, 680), (290, 510), 2),
                    pymunk.Segment(space.static_body, (290, 510), (328, 425), 2),
                    pymunk.Segment(space.static_body, (460, 650), (460, 610), 3),
                    pymunk.Segment(space.static_body, (500, 660), (500, 620), 3),
                    pymunk.Segment(space.static_body, (540, 670), (540, 630), 3),
                    pymunk.Segment(space.static_body, (580, 670), (580, 630), 3),
                    pymunk.Segment(space.static_body, (620, 660), (620, 620), 3),
                    pymunk.Segment(space.static_body, (660, 650), (660, 610), 3),
                    pymunk.Segment(space.static_body, (430, 550), (430, 520), 2),
                    pymunk.Segment(space.static_body, (400, 495), (297, 495), 4),
                    pymunk.Segment(space.static_body, (318, 670), (318, 527), 1),
                    pymunk.Segment(space.static_body, (318, 527), (365, 527), 1),
                    pymunk.Segment(space.static_body, (366, 527), (366, 650), 1),
                    pymunk.Segment(space.static_body, (366, 650), (380, 667), 1),
                    pymunk.Segment(space.static_body, (380, 667), (410, 690), 1),
                    pymunk.Segment(space.static_body, (410, 690), (349, 699), 1),
                    pymunk.Segment(space.static_body, (350, 699), (319, 670), 1),
                    pymunk.Segment(space.static_body, (276, 168), (300, 168), 1.0),
                    pymunk.Poly(b, [(330,427),(400,490),(400,490),(300,490)]),
                    pymunk.Poly(b, [(393,580),(393,650),(410,660),(410,590)]),
                    pymunk.Poly(b,[(260,768),(260,740),(370,740),(420,768)]),
                    pymunk.Poly(b,[(745,768),(745,680),(740,680),(736,720),(715,768)])]

    for line in global_walls:
        line.elasticity = 0.7
        line.group = 1
        line.color = White
    space.add(global_walls)

        ## Blue polygons
    blue_pols = [pymunk.Poly(b,[(265,392),(300,412),(265,500)]),
                pymunk.Poly(b, [(720,500),(680,450),(720,400)]),
                pymunk.Poly(b, [(720,410),(700,380),(720,310)]),
                pymunk.Segment(space.static_body, (720,0),(720,620),1)
    ]

    for pol in blue_pols:
        pol.elasticity = 0.7
        pol.color = Blue
    space.add(blue_pols)

        ## Green lines
    green_lines = [pymunk.Segment(space._static_body, (396,498), (396,600),4),
                pymunk.Segment(space._static_body, (305,487), (390,487),4),
                pymunk.Segment(space._static_body, (315,465), (363,465),6),
                pymunk.Segment(space._static_body, (687,110), (687,200),4)]

    for pol in green_lines:
        pol.elasticity = 0.7
        pol.color = Green
    space.add(green_lines)

        ## Purple lines
    purple_lines = [pymunk.Segment(space.static_body, (300, 258), (300, 228), 1.0),
                    pymunk.Segment(space.static_body, (320, 258), (320, 228), 1.0),
                    pymunk.Segment(space.static_body, (276, 258), (276, 168), 1.0)]

    for line in purple_lines:
        line.elasticity = 0.7
        line.color = Purple
    space.add(purple_lines)


    left_shape = [pymunk.Segment(space.static_body, (300, 168), (329, 100), 1.0),
                  pymunk.Segment(space.static_body, (329, 99), (375, 87), 1.0),
                        ## blue pol solid state
                  pymunk.Segment(space.static_body, (340, 248), (340, 158), 1.0),
                  pymunk.Segment(space.static_body, (340, 158), (335, 147), 1.0),
                  pymunk.Segment(space.static_body, (335, 147), (350, 118), 1.0),
                  pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                  pymunk.Segment(space.static_body, (350, 118), (385, 108), 1.0),
                  pymunk.Segment(space.static_body, (385, 108), (400, 123), 1.0)]

    for line in left_shape:
        line.elasticity = 0.7
        line.group = 1
    space.add(left_shape)

    right_shape = [pymunk.Segment(space.static_body, (745, 118), (695, 118), 1),
                   pymunk.Segment(space.static_body, (693, 78), (693, 118), 2),
                   #pymunk.Segment(space.static_body, (680, 118), (680, 114), 1.0),
                   #pymunk.Segment(space.static_body, (680, 114), (605, 86), 1.0),
                        ## blue pol solid state
                   pymunk.Segment(space.static_body, (650, 248), (660, 228), 1),
                   pymunk.Segment(space.static_body, (660, 228), (660, 128), 1),
                   pymunk.Segment(space.static_body, (660, 128), (610, 108), 1),
                   pymunk.Segment(space.static_body, (610, 108), (590, 133), 1),
                        ## purple pol solid state
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

        ## bumpers
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

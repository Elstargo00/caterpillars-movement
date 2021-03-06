from turtle import Turtle
import time
import random

STARTING_POSITIONS = [(-130, 150), (-180, 150), (-230, 150), (-280, 150)]
STARTING_INNER_POSITION1 = [ tuple(map(sum, zip(point,(8, -9)))) for point in STARTING_POSITIONS ]
STARTING_INNER_POSITION2 = [ tuple(map(sum, zip(point,(-9, 8)))) for point in STARTING_POSITIONS ]
RELATIVE_DISTANCE_INNER1 = [ tuple(map(lambda point1, point2: point1 - point2, STARTING_POSITIONS[i], STARTING_INNER_POSITION1[i])) for i in range(len(STARTING_POSITIONS)) ]
RELATIVE_DISTANCE_INNER2 = [ tuple(map(lambda point1, point2: point1 - point2, STARTING_POSITIONS[i], STARTING_INNER_POSITION2[i])) for i in range(len(STARTING_POSITIONS)) ]
MOVING_DISTANCE = random.randint(40, 50)
BLACK = (44, 53, 55)
YELLOW = (255, 184, 19)

class Caterpillar():
    
    def __init__(self):
        self.segments = []
        self.inner_segments1 = []
        self.inner_segments2 = []
        self.create_caterpillar(STARTING_POSITIONS)
        
    
    def create_caterpillar(self, position):
        for i, position in enumerate(STARTING_POSITIONS):
            a_segment = Turtle("circle")
            an_inner_segment1 = Turtle("circle")
            an_inner_segment2 = Turtle("circle")
            a_segment.speed(1)
            an_inner_segment1.speed(1)
            an_inner_segment2.speed(1)
            a_segment.turtlesize(3, 3, 3)
            an_inner_segment2.turtlesize(0.8, 0.8, 0.8)
            an_inner_segment2.turtlesize(0.4, 0.4, 0.4)
            if i % 2 == 0:
                a_segment.pen(fillcolor=YELLOW, pencolor=BLACK)
                an_inner_segment1.pen(fillcolor=BLACK, pencolor=YELLOW)
                an_inner_segment2.pen(fillcolor=BLACK, pencolor=YELLOW)
            else:
                a_segment.pen(fillcolor=YELLOW, pencolor=BLACK)
                an_inner_segment1.pen(fillcolor=BLACK, pencolor=YELLOW)
                an_inner_segment2.pen(fillcolor=BLACK, pencolor=YELLOW)
            a_segment.penup()
            an_inner_segment1.penup()
            an_inner_segment2.penup()
            a_segment.goto(position)
            an_inner_segment1.goto(STARTING_INNER_POSITION1[i])
            an_inner_segment2.goto(STARTING_INNER_POSITION2[i])
            self.segments.append(a_segment)
            self.inner_segments1.append(an_inner_segment1)
            self.inner_segments2.append(an_inner_segment2)
        
    def move(self, screen):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            (new_x, new_y) = (self.segments[seg_num - 1].xcor() - random.uniform(8, 13), self.segments[seg_num - 1].ycor())
            self.segments[seg_num].goto(new_x,new_y)
            (new_inner1_x, new_inner1_y) = (new_x + RELATIVE_DISTANCE_INNER1[seg_num - 1][1], new_y + RELATIVE_DISTANCE_INNER1[seg_num - 1][0])
            (new_inner2_x, new_inner2_y) = (new_x + RELATIVE_DISTANCE_INNER2[seg_num - 1][1], new_y + RELATIVE_DISTANCE_INNER2[seg_num - 1][0])
            self.inner_segments1[seg_num].goto(new_inner1_x, new_inner1_y)
            self.inner_segments2[seg_num].goto(new_inner2_x, new_inner2_y)
            screen.update()
            time.sleep(0.5)
        self.segments[0].forward(MOVING_DISTANCE)
        self.inner_segments1[0].forward(MOVING_DISTANCE)
        self.inner_segments2[0].forward(MOVING_DISTANCE)
        screen.update()
        time.sleep(0.5)

            
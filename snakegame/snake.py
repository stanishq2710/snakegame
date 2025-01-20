import turtle as t

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_segment = t.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # tell last segment to go to the position of second last segment
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0] != DOWN:
            self.segments[0].setheading(UP)
        # change the position of first segments as while moving the other segments will follow the first segment

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0] != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0] != LEFT:
            self.segments[0].setheading(RIGHT)



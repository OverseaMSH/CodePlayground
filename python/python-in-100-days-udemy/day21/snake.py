from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakeSquares = []
        self.snakeStage = 0
        self.create_snake()
        self.head = self.snakeSquares[0]

    def create_snake(self):

        for i in range(self.snakeStage+3):
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(MOVE_DISTANCE*-i, 0)
            self.snakeSquares.append(snake)

    def add_snake_square(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(MOVE_DISTANCE*position[0], MOVE_DISTANCE*position[1])
        self.snakeSquares.append(snake)

    def extend(self):
        self.add_snake_square(self.snakeSquares[-1].position())

    def move(self):
        for sqNum in range(len(self.snakeSquares)-1, 0, -1):
            newX = self.snakeSquares[sqNum-1].xcor()
            newY = self.snakeSquares[sqNum-1].ycor()
            self.snakeSquares[sqNum].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=690, height=690)
screen.bgcolor("black")
screen.title("Sadegh day20 snake game")
snakeSquares = []
snakeStage = 0
for i in range(snakeStage+3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.goto(-20*i, 0)
    snakeSquares.append(snakeSquares)





screen.exitonclick()

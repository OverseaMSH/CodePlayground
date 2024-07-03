import turtle as tt
import random

tt.colormode(255)
tt.speed("fastest")
circleBoard = tt.Turtle()
tt.hideturtle()  

rgbColors = [(253, 252, 241), (238, 251, 245), (188, 19, 46), (244, 233, 61), (252, 230, 236), 
             (217, 238, 244), (195, 76, 34), (218, 66, 106), (15, 142, 89), (196, 176, 19), 
             (21, 125, 173), (108, 182, 209), (18, 167, 213), (209, 153, 90), (26, 40, 75), 
             (36, 43, 110), (79, 175, 96), (181, 44, 65), (235, 231, 5), (216, 67, 48), 
             (217, 129, 153), (125, 185, 119), (238, 161, 180), (8, 61, 38), (148, 209, 221), 
             (9, 92, 53), (6, 87, 109), (160, 30, 27), (237, 169, 162), (159, 212, 183)]

circleBoard.setheading(225)
circleBoard.penup()
circleBoard.forward(300)
circleBoard.setheading(0)

for i in range(1, 101):
    circleBoard.dot(20, random.choice(rgbColors))
    circleBoard.penup()
    circleBoard.forward(50)
    if i % 10 == 0:
        circleBoard.setheading(90)
        circleBoard.forward(50)
        circleBoard.setheading(180)
        circleBoard.forward(500)
        circleBoard.setheading(0)

tt.Screen().exitonclick()

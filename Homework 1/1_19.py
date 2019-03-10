import turtle

turtle.pensize (5)

point1 = (40,-69.28)
point2 = (-40,-69.28)
point3 = (-80,-9.8)
point4 = (-40, 69)
point5 = (40,69)
point6 = (80,0)

turtle.penup ()
turtle.goto (point1)
turtle.pendown ()
turtle.goto (point2)
turtle.goto(point3)
turtle.goto(point4)
turtle.goto(point5)
turtle.goto(point6)
turtle.goto(point1)

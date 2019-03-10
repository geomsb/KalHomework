import turtle

Point0 = (0,0)
Point1 = (0,-100)
Point1time = (0,-120)
Point2 = (90,0)
Point2arrow = (80,0)
Point3 = (0,80)
Point3arrow = (0,80)
Point4 = (-95,0)
Point4arrow = (-50,0)

turtle.penup ()
turtle.goto (Point1)
turtle.pendown()
turtle.circle (100)


turtle.penup ()
turtle.goto (Point1)
turtle.write (" 6")
turtle.penup ()
turtle.goto (Point2)
turtle.write (" 3")
turtle.goto (Point3)
turtle.write ("12")
turtle.goto (Point4)
turtle.write (" 9")

turtle.penup ()
turtle.goto (Point0)

turtle.pendown ()
turtle.goto (Point2arrow)
turtle.penup ()
turtle.goto (Point0)
turtle.pendown ()
turtle.goto (Point4arrow)
turtle.penup ()
turtle.goto (Point0)
turtle.pensize (3)
turtle.pendown ()
turtle.goto (Point3arrow)

turtle.penup ()
turtle.goto (Point1time)
turtle.write ("9:15:00")


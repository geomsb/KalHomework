import turtle

turtle.pensize (5)

def drawChessboard(startx, endx, starty, endy):
    turtle.penup ()
    turtle.goto (startx,starty)
    turtle.pendown ()

    for row in range (0,8):
        for column in range (0,8):

            if row % 2 == 0:

                if column % 2 >0:
                    turtle.color("black")
                else:
                    turtle.color ("black","white")
                turtle.begin_fill()

            else:
                if column % 2 ==0:
                    turtle.color("black")
                else:
                    turtle.color ("black","white")
                turtle.begin_fill()
                
            for square in range (0,4):
                turtle.forward ((endx - startx) / 8)
                turtle.right (90)

            turtle.end_fill ()
            
            turtle.forward ((endx - startx) / 8)

        turtle.penup()
        turtle.right (90)
        turtle.forward ((endx - startx) / 8)
        turtle.right (90)
        turtle.forward (endx - startx)
        turtle.left (180)
        turtle.pendown ()
  
        
drawChessboard(-100, 100, 100, -100)
drawChessboard (140, 340, 100, -100)

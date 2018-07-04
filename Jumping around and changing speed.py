import turtle 

ninja = turtle.Turtle()

ninja.speed(20)

for i in range(180):
    ninja.forward(100)
    ninja.right(300)
    ninja.forward(50)
    ninja.left(100)
    ninja.forward(50)
    ninja.right(100)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()

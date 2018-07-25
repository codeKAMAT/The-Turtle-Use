import turtle
star = turtle.Turtle()

val = 194
for m in range(20): 
    for i in range(5):
        star.forward(val)  
        star.right(144)
    val = val - 10

    
turtle.done()

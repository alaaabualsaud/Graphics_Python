import turtle

def draw_tringle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(120)
        some_turtle.left(120)
        some_turtle.forward(120)  
def draw_art(): 
    window = turtle.Screen()
    window.bgcolor("yellow")
#Create the turtle Tom - Draw a tringle 
    Tom = turtle.Turtle()
    Tom.shape("turtle")
    Tom.color("blue")
    Tom.speed(4)
    draw_tringle(Tom)

    for i in range(1,36):
        draw_tringle(Tom)
        Tom.right(10)
#create the turtle Alaa - Draw a Circle    
   # Alaa = turtle.Turtle()
    #Alaa.shape("arrow")
   # Alaa.color("red")
    #Alaa.speed(4)
    #Alaa.circle(100)

    window.exitonclick()
draw_art()    
draw_square()

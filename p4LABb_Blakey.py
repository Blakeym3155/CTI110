import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


t.pensize(3)            
t.pencolor("purple")    
t.shape("turtle")




t.left(90)
t.forward(90)
t.right(145)
t.forward(90)
t.left(120)
t.forward(90)
t.right(145)
t.forward(90)

t.penup()
t.left(90)
t.forward(100)
t.pendown()
t.circle(20, extent = 180)
t.circle(-20, extent = -180)
t.left(-90)
t.forward(80)

import turtle

def restart():
    turtle.reset()

#북쪽 
def w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

#서쪽 
def a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

#남쪽 
def s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

#동쪽 
def d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


turtle.shape('turtle')

turtle.onkey(restart, 'Escape')

turtle.onkey(w, 'w')
turtle.onkey(a, 'a')
turtle.onkey(s, 's')
turtle.onkey(d, 'd')

turtle.listen()




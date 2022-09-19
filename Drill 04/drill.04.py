import turtle

count_row=0
count_raw=0
x=200
y=200

while (count_row<6):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward (500)
    y = y-100
    count_row = count_row+1

turtle.right(90)
if(count_row==6):
    x = 200
    y = 200
    while (count_raw<6):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward (500)
        x = x+100
        count_raw = count_raw+1

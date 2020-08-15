import turtle
monica =turtle.Turtle()
monica.speed(1)
monica.color('red')

sides = 5
distance = 100
angle = 144
for i in range(sides):
    monica.forward(distance)
    monica.right(angle)
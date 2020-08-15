import turtle
monica =turtle.Turtle()
monica.speed(1)
monica.color('red')

sides = 4
distance = 100
angle = 360/4
distance2 = 40
for _ in range(sides):
    monica.forward(distance)
    monica.left(angle)
    for _ in range(sides):
        monica.forward(distance2)
        monica.left(angle)
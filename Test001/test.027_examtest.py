import turtle
import time
x=turtle.Turtle()

#海龟
# x.speed(8)
# x.color('red','yellow')
# x.begin_fill()
# for _ in range(50):
#     x.forward(200)
#     x.left(170)
# x.end_fill()
# time.sleep(10)

# 五角星
# x.speed(5)
# # x.color("red","yellow")
# x.pensize(5)
# x.pencolor("yellow")
# x.fillcolor("green")
# x.begin_fill()
# for _ in range(5):
#     x.forward(100)
#     x.left(144)
# x.end_fill()
# time.sleep(5)
#
# 正五边形
x.speed(5)
# x.color("red","yellow")
x.pensize(5)
x.pencolor("yellow")
x.fillcolor("green")
x.begin_fill()
for i in range(5):
    x.forward(100)
   # x.left(72)
    x.right(72)
x.end_fill()
time.sleep(5)
# x.speed(5)
# for i in range(8):
#     x.forward(50)
#     x.right(45)
# time.sleep(5)
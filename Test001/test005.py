# import turtle
# x=turtle.Turtle()
# x.fillcolor('yellow')
# x.begin_fill()
# for i in range(5):
#     x.forward(100)
#     x.right(144)
# x.end_fill()

# for i in range(6):
#     x.right(60)
#     for i in range(4):
#         x.forward(50)
#         x.right(90)

# for i in range(4):
#     x.forward(100)
#     x.right(90)

# for i in range(3):
#     x.forward(100)
#     x.right(120)
#
# for i in range(4):
#     x.forward(100)
#     x.right(90)
#     for i in range(4):
#         x.forward(30)
#         x.right(90)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("初始化方法！！！！")
    def ChinesePeople(self):
        print("我会讲中国话！汉语！")
    def USAPeople(self):
        print("I can speak English!")

class Student(Person):
    def Study(self):
        print("我可以学习新的知识！")

if __name__ == '__main__':
    x1=Person("sunyun",20)
    x1.age=20
    x1.name='sunyun'
    x1.ChinesePeople()
x2=Student("huahua",89)
x2.Study()
x2.ChinesePeople()
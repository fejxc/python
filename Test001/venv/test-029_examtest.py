#练习使用类
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("i can speak!")
class dog(Animal):
    def speak(self):
        print("我叫："+self.name+"  汪汪汪--------->>>>>")
    def kanjia(self):
        print("我可以看家！！！！")
class cat(Animal):
    collor="yellow"
    def speak(self):
        print("喵喵------>>>>>")
    def catchFish(self):
        print("我可以抓鱼！！！！")
if __name__ == '__main__':
    x=dog("小狗花花")
    x.speak()
    x.kanjia()
    y=Animal("动物")
    y.speak()
    z=cat("miaomao")
    print(z.collor)
    z.speak()
    z.catchFish()
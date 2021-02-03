'''
定义三个类，小猫小狗和人
小狗：姓名，年龄（默认1岁）；吃饭，玩，睡觉，看家（格式：名字是xx，年龄xx岁的小狗在xx）
小猫：姓名，年龄（默认1岁）；吃饭，玩，睡觉，捉老鼠（格式：名字是xx，年龄是xx岁的小猫在xx）
人：姓名，年龄（默认1岁），宠物；吃饭，玩，睡觉（格式：名字是xx，年龄xx岁的小猫在xx）；养宠物（让所有的宠物吃饭，玩，睡觉），让宠物工作（让所有的宠物根据自己的职责开始工作）
'''

#********************************代码1******************************
# class Dog():
#     def __init__(self,name,age = 1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("名字是{}，年龄{}岁的小狗在吃饭".format(self.name,self.age))
#
#     def play(self):
#         print("名字是{}，年龄{}岁的小狗在玩耍".format(self.name,self.age))
#
#     def sleep(self):
#         print("名字是{}，年龄{}岁的小狗在睡觉".format(self.name, self.age))
#
#     def watch(self):
#         print("名字是{}，年龄{}岁的小狗在看家".format(self.name, self.age))
#
# d =Dog("小黑",18)
# d.eat()

#********************************代码2******************************
# class Dog():
#     def __init__(self,name,age = 1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s在吃饭"% self)
#
#     def play(self):
#         print("%s在玩"% self)
#
#     def sleep(self):
#         print("%s在睡觉"% self)
#
#     def watch(self):
#         print("%s在看家"% self)
#
#     def __str__(self):
#         return "名字是{}，年龄{}岁的小狗".format(self.name, self.age)
#
# d =Dog("小黑",18)
# d.eat()

#********************************代码3******************************
class Animal:
    def __init__(self,name,age = 1):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self)

    def play(self):
        print("%s在玩" % self)

    def sleep(self):
        print("%s在睡觉" % self)


class Dog(Animal):
    def __init__(self, name, age=1):
       super().__init__(name ,age)

    def work(self):
        print("%s在看家"%self)


    def __str__(self):
        return "名字是{}，年龄{}岁的小狗".format(self.name, self.age)

class Cat(Animal):
    def __init__(self, name,age=1):
       super().__init__(name ,age)

    def work(self):
        print("%s在捉老鼠"%self)

    def __str__(self):
        return "名字是{}，年龄{}岁的小猫".format(self.name, self.age)

class Person(Animal):
    def __init__(self, name, pets,age=1):
       super().__init__(name ,age)
       self.pets = pets

    def yangpets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.leep()

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()



    def __str__(self):
        return "名字是{}，年龄{}岁的人".format(self.name, self.age)


d =Dog("小黑",2)
c =Cat("小红",3)
p =Person("sz",[d,c],18)
p.make_pets_work()
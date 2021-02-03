#计算器，实现一些基本的操作，如加减乘除，以及打印结果

#------------------------------------------------------代码1------------------------------------------------------
# def jia (n1,n2):
#     return n1+n2
# def jian(n1,n2):
#     return n1-n2
# def cheng(n1,n2):
#     return n1*n2
# def chu(n1,n2):
#     return n1/n2
#
# #计算（2+6-4）*5
# r1 = jia(2,6)
# r2= jian(r1-4)
# r3=cheng(r2,5)
# print(r3)

#------------------------------------------------------代码2------------------------------------------------------
# r1,r2,r3这里调用很麻烦
# result = 0
# def first_value(n):
#     global result
#     result = n
# def jia (n):
#     global result
#     result +=n
# def jian (n):
#     global result
#     result -=n
# def cheng (n):
#     global result
#     result *=n
# def chu (n):
#     global result
#     result =result/n
# first_value(2)
# jia(6)
# jian(4)
# cheng(5)
# print(result)


#------------------------------------------------------代码3------------------------------------------------------
#代码2有两个问题，1是result是全局变量不安全；2是代码散乱，零散
# class Caculator:
#     __result = 0
#     @classmethod
#     def first_value(cls,n):
#         cls.__result = n
#     @classmethod
#     def jia(cls,n):
#         cls.__result += n
#     @classmethod
#     def jian(cls,n):
#         cls.__result -= n
#     @classmethod
#     def cheng(cls,n):
#         cls.__result *= n
#     @classmethod
#     def chu(cls,n):
#         cls.__result = cls.__result / n
# 
#     @classmethod
#     def show(cls):
#         print("计算的结果：%d"%cls.__result)
# Caculator.first_value(2)
# Caculator.jia(6)
# Caculator.jian(4)
# Caculator.cheng(5)
# Caculator.show()

#------------------------------------------------------代码4------------------------------------------------------
#当多个其他模块调用该计算器时，若其中一个还没show，
# 另一个就开始计算的话，回过头来在show就会发现结果被改变了。
# 解决方法是放在实例属性上。
# class Caculator:
#     def __init__(self,num):
#         self.__result =num
#     def first_value(self,n):
#         self.__result = n
#     def jia(self,n):
#         self.__result += n
#     def jian(self,n):
#         self.__result -= n
#     def cheng(self,n):
#         self.__result *= n
#     def chu(self,n):
#         self.__result = self.__result / n
#     def show(self):
#         print("计算的结果：%d"%self.__result)
# c1 = Caculator(2)
# c1.jia(6)
# c2 =Caculator(3)
# c1.jian(4)
# c1.cheng(5)
# c2.jia(1)
# c1.show()
# c2.show()
#------------------------------------------------------代码5------------------------------------------------------
#增加容错处理，对num和n判断是否是整形
# class Caculator:
#     def check(self,num):
#         if not isinstance(num,int):
#             raise TypeError("当前这个数据类型有误，应该是一个整型数据")
#
#     def __init__(self,num):
#         self.check(num)
#         self.__result =num
#     def jia(self,n):
#         self.check(n)
#         self.__result += n
#     def jian(self,n):
#         self.check(n)
#         self.__result -= n
#     def cheng(self,n):
#         self.check(n)
#         self.__result *= n
#     def chu(self,n):
#         self.check(n)
#         self.__result = self.__result / n
#     def show(self):
#         print("计算的结果：%d"%self.__result)
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#------------------------------------------------------代码6-----------------------------------------------------
#以上加减乘除方法想要添加操作却破坏了原有的代码，造成代码冗余
#采用装饰器设计模式进行优化重构
# class Caculator:
#     def check_zsq(func):
#         def inner(self,n):
#             if not isinstance(n,int):
#                 raise TypeError("当前这个数据类型有误，应该是一个整型数据")
#             return func(self,n)
#         return inner
#     @check_zsq
#     def __init__(self,num):
#         self.__result =num
#     @check_zsq
#     def jia(self,n):
#         self.__result += n
#     @check_zsq
#     def jian(self,n):
#         self.__result -= n
#     @check_zsq
#     def cheng(self,n):
#         self.__result *= n
#     @check_zsq
#     def chu(self,n):
#         self.__result = self.__result / n
#     def show(self):
#         print("计算的结果：%d"%self.__result)
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#------------------------------------------------------代码7-----------------------------------------------------
#如果外界调用check_zsq方法既没有意义，也会报错，所以把他设置成私有方法
# class Caculator:
#     def __check_zsq(func):
#         def inner(self,n):
#             if not isinstance(n,int):
#                 raise TypeError("当前这个数据类型有误，应该是一个整型数据")
#             return func(self,n)
#         return inner
#     @__check_zsq
#     def __init__(self,num):
#         self.__result =num
#     @__check_zsq
#     def jia(self,n):
#         self.__result += n
#     @__check_zsq
#     def jian(self,n):
#         self.__result -= n
#     @__check_zsq
#     def cheng(self,n):
#         self.__result *= n
#     @__check_zsq
#     def chu(self,n):
#         self.__result = self.__result / n
#     def show(self):
#         print("计算的结果：%d"%self.__result)
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#------------------------------------------------------代码7-----------------------------------------------------
# #增加语音播报功能
# import win32com.client
# #1.创建一个播报对象
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# #2.通过这个播报对象播放相对应的语音字符串
# speaker.Speak("我的名字是Caculator,我的主人是王雪")
#
# class Caculator:
#     def __say(self,word):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak(word)
#     def __check_zsq(func):
#         def inner(self,n):
#             if not isinstance(n,int):
#                 raise TypeError("当前这个数据类型有误，应该是一个整型数据")
#             return func(self,n)
#         return inner
#     @__check_zsq
#     def __init__(self,num):
#         self.__say(num)
#         self.__result =num
#     @__check_zsq
#     def jia(self,n):
#         self.__say(n)
#         self.__result += n
#     @__check_zsq
#     def jian(self,n):
#         self.__say(n)
#         self.__result -= n
#     @__check_zsq
#     def cheng(self,n):
#         self.__say(n)
#         self.__result *= n
#     @__check_zsq
#     def chu(self,n):
#         self.__say(n)
#         self.__result = self.__result / n
#     def show(self):
#         self.__say("计算的结果：%d"%self.__result)
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#------------------------------------------------------代码7-----------------------------------------------------
#将__say换成装饰器，并加上语音播报+-*/
# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("我的名字是Caculator,我的主人是王雪")
#
# class Caculator:
#     def __create_say_zsq(word=''):
#         def __say_zsq(func):
#             def inner(self,n):
#                 self.__say(word + str(n))
#                 return func(self,n)
#             return inner
#         return __say_zsq
#
#     def __say(self,word):
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#         speaker.Speak(word)
#
#     def __check_zsq(func):
#         def inner(self,n):
#             if not isinstance(n,int):
#                 raise TypeError("当前这个数据类型有误，应该是一个整型数据")
#             return func(self,n)
#         return inner
#
#     @__check_zsq
#     @__create_say_zsq()
#     def __init__(self,num):
#         self.__result =num
#     @__check_zsq
#     @__create_say_zsq("加")
#     def jia(self,n):
#         self.__result += n
#     @__check_zsq
#     @__create_say_zsq("减")
#     def jian(self,n):
#         self.__result -= n
#     @__check_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self,n):
#         self.__result *= n
#     @__check_zsq
#     @__create_say_zsq("除以")
#     def chu(self,n):
#         self.__result = self.__result / n
#     def show(self):
#         self.__say("计算的结果是：%d"%self.__result)
#
#     @property
#     def result(self):
#         return self.__result
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
# print(c1.result)
#------------------------------------------------------代码8-----------------------------------------------------
#c1c1c1这样调用麻烦，改成链式调用

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("我的名字是Caculator,我的主人是宇宙无敌帅气海海女朋友超级无敌美少女雪雪")

class Caculator:
    def __create_say_zsq(word=''):
        def __say_zsq(func):
            def inner(self,n):
                self.__say(word + str(n))
                return func(self,n)
            return inner
        return __say_zsq

    def __say(self,word):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(word)

    def __check_zsq(func):
        def inner(self,n):
            if not isinstance(n,int):
                raise TypeError("当前这个数据类型有误，应该是一个整型数据")
            return func(self,n)
        return inner

    @__check_zsq
    @__create_say_zsq()
    def __init__(self,num):
        self.__result =num

    @__check_zsq
    @__create_say_zsq("加")
    def jia(self,n):
        self.__result += n
        return self
    @__check_zsq
    @__create_say_zsq("减")
    def jian(self,n):
        self.__result -= n
        return self
    @__check_zsq
    @__create_say_zsq("乘以")
    def cheng(self,n):
        self.__result *= n
        return self
    @__check_zsq
    @__create_say_zsq("除以")
    def chu(self,n):
        self.__result = self.__result / n
        return self
    def show(self):
        self.__say("计算的结果是：%d"%self.__result)
        return self

    def clear(self):
        self.__say("计算器清零")
        self.__result = 0
        return self
    @property
    def result(self):
        return self.__result
c1 = Caculator(2)
c1.jia(6).jian(4).cheng(5).show().jia(500).show().clear().jia(520).show()
print(c1.result)

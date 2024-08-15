# class Student :
#     def __init__(self,name) :
#         self.name = name

# s1 = Student("vicky")
# print(s1.name)
# del s1
# print(s1.name)

# class Account :
#     def __init__(self,acc_no,acc_pass) :
#         self.acc_no = acc_no
#         # make acc_password private
#         self.__acc_pass = acc_pass
#     def reset_pass(self) :
#         print(self.__acc_pass)    

# acc1 = Account(123445,"acde")
# print(acc1.acc_no)
# # make private
# print(acc1.reset_pass())

# class Person :
#     __name = "vikram"

#     def __hello(self) :
#         print("hello person")
#     def welcome(self) :
#         self.__hello()
           

# p1 = Person()
# print(p1.welcome())

# inheritance
# single
# class Car :
  
#     @staticmethod
#     def start() :
#         print("car was start")
#     @staticmethod
#     def stop() :
#         print("car was stop")

# class toyotacar(Car) :
#     def __init__(self,name) :
#         self.name = name

# car1 =  toyotacar("fortuner")
# print(car1.start())

# multi-level 
# class Car :
  
#     @staticmethod
#     def start() :
#         print("car was start")
#     @staticmethod
#     def stop() :
#         print("car was stop")

# class toyotacar(Car) :
#     def __init__(self,brand) :
#         self.brand = brand

# class fortuner(toyotacar):
#     def __init__(self,type) :
#         self.type = type

# car1 = fortuner("disel")
# car1.start()


# multiple
# class A :
#     varA = "welcome to A :"
# class B :
#     varB = "welcome to B "

# class C(A,B) :
#     varC = "welcome to c "

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

# super method
# class Car :
#     def __init__(self,type) :
#         self.type = type
  
#     @staticmethod
#     def start() :
#         print("car was start")
#     @staticmethod
#     def stop() :
#         print("car was stop")

# class toyotacar(Car) :
#     def __init__(self,name,type) :
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = toyotacar("fortuner","electric")
# print(car1.type)

# class method
# class Person :
#     name = "vicky"

#     # def change_name(self,name) :
#     #     self.name = name
#     @classmethod
#     def change_name(cls,name) :
#         cls.name = name

# p1 = Person()
# p1.change_name("vikram")
# print(p1.name)
# print(Person.name)

# propery  decorator
# class Student :
#     def __init__(self,phy,chem,math) :
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percantage(self) :
#         return str((self.phy + self.chem + self.math)/3) + "%"

# std1 = Student(98,97,99)
# print(std1.percantage) 
# std1.phy = 86
# print(std1.percantage)      

# create complex number
class Complex :
    def __init__(self,real,img) :
        self.real = real
        self.img = img
    def showNum(self) :
        print(self.real, "i +",self.img,"j")
    def __add__(self,num2) :
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2) :
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNum()
num2 = Complex(4,2)
num2.showNum()
num3 = num1 + num2
num3.showNum()
num3 = num1 - num2
num3.showNum()
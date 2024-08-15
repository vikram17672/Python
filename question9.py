# class Circle :
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self) :
#         return (22/7) * self.radius ** 2
    
#     def parimeter(self) :
#         return 2*(22/7)*self.radius 
# c1 = Circle(21)
# print(c1.area())
# print(c1.parimeter())


# class Employe :
#     def __init__(self,role,dept,sal) :
#         self.role = role
#         self.dept = dept
#         self.sal = sal
#     def showDetail(self) :
#         print("role :",self.role)
#         print("dept :",self.dept)
#         print("sal :",self.sal)

# class Engineer(Employe) :
#     def __init__(self,age,name) :
#         self.age = age
#         self.name = name
#         super().__init__("Enginner","IT","90000")


# eng1 = Engineer("vikram singh chilwal",19)
# eng1.showDetail()

class Order :
    def __init__(self,item,price) :
        self.item = item
        self.price = price
    def __gt__(self,ord2) :
        return self.price > ord2.price
ord1 = Order("chips",20)
ord2 = Order("tea",10)   

print(ord1>ord2)
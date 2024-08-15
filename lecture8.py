# class Student :
#     # default constructor
#     def __init__(self) :
#         print("adding new database")
#         # paratrimise constestor
#     def __init__(self,name,marks) :
#         self.name = name
#         self.marks = marks
#         # method
#     def hello(self) :
#         print("hello everyone",self.name)    
#     def get_marks(self) :
#         return self.marks

# s1 = Student("vikram",88)
# # print(s1.name,s1.marks) 
# s1.hello() 
# print(s1.get_marks())

# qustions
# class Student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks= marks
#     @staticmethod     
#     def hello():
#         print("hello")  

#     def get_avg(self):
#         sum = 0
#         for val in self.marks :
#             sum +=val
#         print("hi",self.name,"your avg is ",sum/3)
# s1 = Student("vikram chilwal",[99,98,97])  
# s1.get_avg()  
# s1.hello()  

# abstractions
# class car :
#     def __init__(self) :
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self) :
#         self.clutch = True
#         self.acc = True
#     print("car was start") 

# car1 = car()
# car1.start()  

# questions
class Account :
    def __init__(self,balance,acc) :
        self.balance = balance
        self.account_no = acc

    def debit(self,Amount) :
        self.balance -=Amount
        print("remain RS. :",Amount)
        print("total balnce is :",self.get_balance())
    def cadit(self,Amount) :
        self.balance += Amount
        print("Added Rs. is :",Amount)
        print("total balnce is the :",self.get_balance())

    def get_balance(self) :
        return self.balance

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.cadit(500)
acc1.cadit(80000)

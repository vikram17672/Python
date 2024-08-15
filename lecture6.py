# def cal_sum(a,b) :
#     sum = a+b
#     print(sum)
#     return sum

# cal_sum(3,5)
# cal_sum(9,5)

# waf to find the length of elemnts

# citys = ["Delhi","Gurgaon","Almora","Mumbai"]

# def len_print(list) :
#     print(len(list))

# def len_print(list) :
#     for item in list :
#         print(item,end=" ")    
# print(citys)
# len_print(citys)

# fun for factorial
# def cal_fact(n) :
#     fact = 1
#     for i in range(1,n+1) :
#         fact *=i
#     print(fact)    

# cal_fact(5)

# def conveter(usd) :
#     inr = usd*83
#     print(usd ,"usd =",inr ,"inr ")

# conveter(2)   

# recursion
# def show(n) :
#     # base case
#     if(n==0) :
#         return
#     print(n)
#     show(n-1)    
# show(5)

# wap recuricve program for sum first n natural number
# def nat_num(n) :
#     if(n==0) :
#         return 0
#     return nat_num(n-1)+n

# sum = nat_num(5) 
# print(sum)   

def print_list(list,idx=0) :
    if(idx ==len(list)) :
        return 
    print(list[idx])
    print_list(list,idx+1)

fruit = ["mango","banana","apple","gauava"]   
print_list(fruit)     
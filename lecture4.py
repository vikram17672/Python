# info = {
#     "key" : "value",
#     "name" : "vicky",
#     "learn" : "coding",
#     "marks" : 98.7,
#     "age"   : 18,
    
# }
# print(info)

# nested dictionary
student = {
    "name" : "vikram singh",
    "subject" : {
        "chem" : 88,
        "phy" : 99,
        "math" : 78,
    }
}
# print(student["subject"]["phy"])
# print(list(student.items()))
# print(student["name2"]) #error
# print(student.get("name2")) # give None 

# student.update({"city":"Almora"})
# print(student)

# set
# collection = {1,2,3,4,5,"hello","world",4}
# print(collection)
# print(type(collection))

# empty set
# sit = set()
# sit.add(1)
# sit.add(2)
# sit.add(3)
# sit.add(2)
# sit.add("vicky")
# sit.add((1,5,6))
# sit.clear()
# # print(sit)
# print(len(sit))

# collect = {"hello","world","hii","python","vicky"}
# print(collect.pop())

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) #{1,2,3,4}
# print(set1.intersection(set2)) #{2,3}


# questions
# store the follwing word meaning in python dictionary

# dict = {
#     "cat"  : "a small animal",
#     "table" : ["a piece of furniture","list of fact & figure"]

# }
# print(dict)

# give a list of subject of student.assume that one classroom  is requird of 1 subject.how many classroom is requrid for all student
# subject = {
#     "python","java","c++","c","js","python","c++","c","python"
# }
# print(subject)
# print(len(subject))


marks = {}

x = int(input("enter the marks of phy :"))
marks.update({"phy":x})

y = int(input("enter the marks of chem :"))
marks.update({"chem":y})

z = int(input("enter the marks of math :"))
marks.update({"math":z})

print(marks)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# write mode
# f = open("demo.txt","a")
# f.write("hello good night and i love me")
# f.close()

# with open("partice.txt","r") as f :
    # data = f.read()
    # new_data = data.replace("vicky","vikram")
    # print(new_data)

word = "village"
with open("partice.txt","r") as f :
    data = f.read()
    if(data.find(word)!=-1) :
            print("found")
    else :
            print("not found")    

    
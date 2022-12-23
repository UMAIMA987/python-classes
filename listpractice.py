list= [ 1,2,2,4,5,87,9,56,78,51,25,452,24,51,2,45,211,2,4,52,2,45,1,2,5,4,1,2,54,1,1,1,52,455,1,25,4,568,99,55,79,9,]
print(len(list))

# # #=============Methods of list==================

# # #append
# # list.append(45)
# # print(list)

# # #insert
# # list.insert(0,45)
# # print(list)

# # list.insert(16,45)
# # print(list)

# # #extend

# # list.extend(["umaima"])
# # print("new list",list)

newlist=["i am a new list"]
list.extend(newlist)
print(list)


# #==================copy methods in list====================

newlist=list
list.append("added element")    # by reference
print(list)
print(newlist)

# copy by value

newlist=list.copy()
print("newlist",list)
newlist.append(123456)
print(newlist)
print(list)





#==================sir coding sample================


myList = ["python",20,True,"TTS-class"]
#  COPY LIST
myList2 = myList                       # pass by reference
myList2 = myList.copy()              # pass by value
print("myList2",myList2)    
print("myList2",myList2)    
myList2.append("python programming")
print("myList",myList)
print("myList2",myList2)


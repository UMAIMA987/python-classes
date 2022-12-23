#================print in a reverse manner============
#================toughest one=========================

x=input("Enter your first and last name :  ")
y=len(x)
print(y)

# =========without loop==========
print(x[len(x): :-1])



#==============with loops=========
z=-1
for i in range (y,0,-1):
   print(x[z],end=" ")   # bht mushkil se chalaya ha isko
   z=z-1


# ===============practice code============
# =========i dont want to remove that======


# for i in range(y,0,-1):
#    print(x[len(x): :-1])
    
       
   # for m in range (y):

     

# x= "sara"
# print(len(x))
# print(x[6: :-1], sep=" ")
#  #print(x[y: : -1],end="<")
# print(x[:]) 
# print(x[len(x): :-1])



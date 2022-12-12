              #----------input is even or odd--------------------
              #----if input is aplhabets print invalid-----------


x=input("Enter your input : ")

if x.isalpha() == True:
   print("Invalid.Input a Number")
else:
    y=int(x)
    print(type(y),y)
    z=y%2
    if z== 0:
      print("Your input is an even number")
    else: 
      z!=0
      print("Your input is an odd number")







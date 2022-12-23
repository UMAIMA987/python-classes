#================ input are equal or their sum or difference is 5===================

x=int(input("Enter your first number :  "))
y=int(input("Enter your second number :  "))

if x==y or y==x:
    print("TRUE Both numbers are same.")

elif x!=y:
    z=x+y
    u=x-y
    
    if z==5 or u==5:
        print("TRUE your number calculation is equal to 5")
    else:
        print("FALSE") 

    


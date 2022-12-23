#======================Multiplication Table=============

n=int(input("Enter the number of which table you want to print :  "))

for i in range(1,11):
    x=n*i
    print(n , "*", i ,"=" , x)


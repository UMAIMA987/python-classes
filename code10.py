#---------------your input is even or odd-----------

x=int(input("Enter your number : "))
z=x%2
if z == 0:
    print("Your input is an even number")
elif z ==1:
    print("Your input is an odd number")
else :
    print("Invalid")

#================checking palindrome words=================

# Python program to check
# if a string is palindrome
# or not

x=input("Enter your word : " )
y=len(x)-1
w=""

for i in range(y,-1,-1):
    w=w+x[i]


if w==x:
    print("Palindrome")

else:
    print("Not Palindrome")



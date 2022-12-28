#============count the occurences of vowels and consonants========

x=input("Enter your text : ")

vowels=[ "a", "e", "i", "o", "u"]

v=[]
c=[]

for i in range(0,len(x)):

    if x[i] in vowels:
        v.append(x[i])
    else:
        c.append(x[i])

print("Vowels in your words are : " , len(v))
print("Consonants in your words are :  " ,len(c))


#==================== MARK SHEET================

name=input("Enter your name:\t")
eng=int(input("Enter your English marks:\t"))
maths=int(input("Enter your Maths marks:\t"))
phy=int(input("Enter your Physics marks:\t"))
urdu=int(input("Enter your Urdu marks:\t"))
isl=int(input("Enter your Islamiat marks:\t"))

total=eng+maths+phy+urdu+isl
print("Total marks:\t" , total )

percent=(total/500)*100
print("Your Percentage is :\t" , int(percent),"%")


if percent>=80 :
    print("your grade is A+")

elif percent>=70 and percent<80:
    print("your grade is A")

elif percent>=60 and percent<70:
    print("your grade is B")

elif percent>=50 and percent<60:
    print("Your grade is C")

elif percent>=40 and percent<50:
    print("Your grade is D")        

elif percent>=30 and percent<40:
    print("Your grade is E")    
    
else:
    print("Fail")

    


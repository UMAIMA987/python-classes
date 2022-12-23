#CREATE DICTIONARY

std_data= {
    'id' : 1,
    "name":"ali",
    "age":20,
    "course":"python programming"
}
print(std_data)
#CRUD OPERATIONS IN DICTIONARIES


#ACCESS DATA IN DICTIONARIES

print(std_data["name"])
print(std_data["name"],std_data["age"])


#ADD DATA IN DICTIONARIES

std_data["fees"] = 2000
print(std_data)


#DELETE DATA IN DICTIONARIES

del (std_data["course"])
print(std_data)

#UPDATE DATA IN DICTIONARIES

std_data["fees"]= 2500
print("new fees " , std_data)

#DELETE DICTIONARY

# del (std_data)


#METHODS OF DICTIONARIES
#LEN()
#CLEAR()
#VALUES()
#KEYS()

#LEN() IN DICTIONARY
print(len(std_data))

#CLEAR() IN DICTIONARY

# std_data.clear()           # it  only clears your data in dictionary
# print(std_data)            # your dictionary exist with empty data


#PRINT VALUES() IN DICTIONARY

print("values",std_data.values())

#add value in dictionary
std_data["course"]="python programming"
print(std_data)


#PRINT KEYS() IN DICTIONARY

print("keys" ,std_data.keys())

#==============task===========

student=input("Enter your name : ahtesham , ali , ayesha , sana , sara : \t")

std_1={
   
    "id": 1,
    "name": "ahtesham",
    "gender" :"male",
    "age": 25,
    "course" : "python",
    "fees" : 2500

}

std_2={
   
    "id": 2,
    "name": "ali",
    "gender" :"male",
    "age": 25,
    "course" : "python",
    "fees" : 2500

}

std_3={
   
    "id": 3,
    "name": "ayesha",
    "gender" :"female",
    "age": 22,
    "course" : "python",
    "fees" : 2500

}

std_4={
   
    "id": 4,
    "name": "sana",
    "gender" :"female",
    "age": 22,
    "course" : "python",
    "fees" : 2500

}

std_5={
   
    "id": 5,
    "name": "sara",
    "gender" :"female",
    "age": 22,
    "course" : "python",
    "fees" : 2500

}

if student == "ahtesham" or student== "Ahtesham":
    for values in std_1:
        print(std_1[values])

elif student=="ali" or student=="Ali":
    for values in std_2:
        print(std_2[values])

elif student =="ayesha" or  student =="Ayesha":
    for values in std_3:
        print(std_3[values])


elif student=="sana" or student=="Sana":
    for values in std_4:
        print(std_4[values])

elif student =="sara" or student =="Sara":
    for values in std_5:
        print(std_5[values])

else:
    print("Inavlid input")



#=======================Tuples===================

countries=("China","America","Russia","Afghanistan","Pakistan","New zeeland")
print(type(countries))

# change tuple into list

county=list(countries)
print(county)

county.append("India")
print(county)

county.sort()
print(county)

county.pop()
print(county)

county.pop(3)
print(county)

print(county[:])

county[0]="Turkey"
print(county)

county.append("Pakistan")
print(county)

print(county.count("Pakistan"))

#==========change list into tuple===========s

countries2=tuple(county)
print("New Tuple : ",countries2)










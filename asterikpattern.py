
#============print asterisk in increasing and decreasing pattern=======


for i in range(9):
    if i <5 :
         for k in range(i+1):
             print("*",end="")
         print("")   

    else:
         for i in range(9,i,-1):
            print("*",end="")
         print("")  

#=================print 1 -15 ,13 not included==============
# =========================FOR LOOP=========================


for x in range(1,16):
    if x==13:
        continue
    print(x)


#==========================WHILE LOOP===========================

x=0
while x<=15:
    x=x+1
    if x==13:
       continue
    print(x)

v="a,e,i,o,u"
#c="b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
n="1,2,3,4,5,6,7,8,9,0"
x=input("Enter your alphabet : ")
if x in v:
    print("Its a vowel")
elif x in n:
    print("Numbers are not allowed.Enter your alphabet.")    
else:
    print("It's not a vowel.It is a consonant")    
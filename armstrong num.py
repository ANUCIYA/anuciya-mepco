c=input("enter a number:")
num=0
a=c
while(a>=1):
    rem=a%10
    num+=(rem**3)
    a/=10
if (c==num):
    print ("it is an armstrong number")
else:
    print ("it is not an armstrong number")

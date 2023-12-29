import random
list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7,8,9]
i=1
while i<=10:
    a=random.choice(list1)
    b=random.choice(list2)
    c=a*b

    d=int(input("Q."+str(i)+" "+str(a)+"x"+str(b)+"="))
    if(d==c):
        print("CORRECT.")
    else:
        print("INCORRECT.")
    i=i+1
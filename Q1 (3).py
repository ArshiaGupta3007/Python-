a=int(input("ENTER THE NUMBER : "))
sum=0

for i in range(1,a):
        if a%i==0:
            sum=sum+i
if sum==a:
    print(" PERFECT NUMBER")
else :
    print("NOT A PERFECT NUMBER")
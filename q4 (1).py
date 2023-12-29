n=int(input("ENTER NUMBER OF CANDIES :"))
for n in range(0,200):
    if n%5==2:
        if n%6==3:
            if n%7==2:
                print(n," is the number of candies in the bowl.")

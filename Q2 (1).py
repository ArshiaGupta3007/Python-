year=int(input("ENTER THE YEAR :"))
if year%400==0:
    print("LEAP YEAR")
elif year%100==0:
    print("NOT A LEAP YEAR")
elif year%4==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
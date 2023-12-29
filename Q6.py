a = float(input("Enter length of side 1: "))
b= float(input("Enter length of side 2: "))
c= float(input("Enter length of side 3: "))
if a+b >c and b+c >a and a+c>b:
  print("It is a triangle.")
else:
  print("It is not a triangle.")
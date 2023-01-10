import math
for i in range(0,345,15):
    sin = round(math.sin(math.radians(i)),4)
    cos = round(math.cos(math.radians(i)),4)
    print("sin(",i,")=",sin,"\n", "cos(%d)="%i,cos)
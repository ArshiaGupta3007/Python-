import math
for i in range(0,345,15):
    sin = math.sin(math.radians(i))
    cos = math.cos(math.radians(i))
    print("sin(",i,")=",sin,"\n", "cos(%d)="%i,cos)

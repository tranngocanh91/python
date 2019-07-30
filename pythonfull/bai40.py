import math
def canbachai(x1,x2,y1,y2):
    s=(x1-x2)*(x1-x2) +(y1-y2)*(y1-y2)
    b=math.sqrt(s)
    return b
print(canbachai(4,6,0,6))
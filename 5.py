
import math
a=float(input("trvache:a"))
b=float(input("trvache:b"))
c=float(input("trvache:c"))

D=math.pow(b,2)-4*a*c
print(D)

if D<0:
    print("armat chuni")
elif D==0:
    x=-b/2*a
    print(x)
else:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b+math.sqrt(D))/(2*a)
    print(x1)
    print(x2)
import math
x=float(input("trvache:x"))
y=float(input("trvache:y"))

print("luchum:",(math.cos(x)/math.sin(y)*math.fabs(math.pow(x,2)-y))/math.pow(x,2)+math.pow(y,2)+math.log((math.pow(x,2)-1)))

import math
circumference=int(input("write the circumference of the tree: "))
#C=2pi*r=>r=C/2pi=>d=2C/2pi
diameter=(2*circumference)/(2*math.pi)
print(f"the diameter is {round(diameter,2)} cm")
flag=True
if diameter>=50:
    flag=True
else:
    flag=False
print(f"Tree can be cut down: {flag}")
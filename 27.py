border1=float(input("write th num og the lower boundary: "))
border2=float(input("write th num og the upper boundary: "))
number= float(input("write the number you wanna check: "))
if (number >= border1) and (number <= border2):
    print ("The number is within the boundaries")
else:
    print ("The number is not within the boundaries")
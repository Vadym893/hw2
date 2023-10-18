speed = float(input("write vehicle speed: "))
flag=True
if speed >150 or speed<40:
    flag=False
else:
    flag=True
print(f"Speed is Valid: {flag}")
import random
import time
rolls=int(input("how many dices do you want to roll,less than 20: "))
if rolls>20:
    print("Invalid input!!")
    exit()
special_rolls=0
flag=True
for i in range(1,rolls+1):
    dice_result=random.randint(1,6)
    print(f"Attempt {i}. Result: {dice_result}")
    if dice_result==1 or dice_result==6:
        special_rolls+=1
        flag=True
    else:
        flag=False
    print(f"Sprcial dice: {flag}")
    time.sleep(1.5)
print(f"Amount of special dices:{special_rolls}")

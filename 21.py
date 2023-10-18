height_cm = int(input("write your height"))

height_feet = height_cm // 30.48  
height_inches = (height_cm % 30.48) // 2.54  #

print(f"I am {height_cm}cm tall, i.e. {height_feet} feet and {height_inches} inches")
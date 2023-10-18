weight=float(input("write your weight in kg"))
height = int(input("write your height in cm"))
bmi = (weight / (float(height/100)**2))
print(f"Your BMI is: {round(bmi,2)}")
if bmi < 18.5 and bmi>=10 :
    print ("Underweight")
elif bmi >= 18.5 and bmi <= 24.9 :
    print ("Normal Weight")
elif bmi>=25 and bmi<=29.9:
    print ("Overweight")
elif bmi>=30 and bmi<=40:
    print ("Obese")
else:
    print ("Invalid Inputs")
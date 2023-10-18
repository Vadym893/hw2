import random
print("welcome to guess the number game")
computer_guess = random.randint(1,6)
user_number = int(input("Enter a number between 1 and 6: "))
i=1

if user_number == computer_guess:
    print(f"Congratulations you guessed it from the {i} try")
else:
    while user_number!=computer_guess:
        if user_number>6 or user_number<1:
            print("Invalid input! Please enter a valid number.")
        elif user_number > computer_guess:
            print("Your number is too high")
        elif user_number<computer_guess:
            print("your number is too low")
        user_number = int(input("Enter a number between 1 and 6: "))
        i+=1
print(f"Congratulations you guessed it on the {i} try")
phone_number = input("Enter a 9-digit phone number: ")

if len(phone_number) != 9 or not phone_number.isdigit():
    print("Invalid input. Please enter a 16-digit number.")
else:
    formatted_phone_number= '-'.join([phone_number[i:i+3] for i in range(0, 9, 3)])
    print("Formatted credit card number:", formatted_phone_number)
credit_card_number = input("Enter a 16-digit credit card number: ")

if len(credit_card_number) != 16 or not credit_card_number.isdigit():
    print("Invalid input. Please enter a 16-digit number.")
else:
    # Display the credit card number in groups of 4 digits
    formatted_credit_card = ' '.join([credit_card_number[i:i+4] for i in range(0, 16, 4)])
    print("Formatted credit card number:", formatted_credit_card)
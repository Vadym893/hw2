product = str(input("Write a product you are interested in : "))
price = float(input("Write the price of it: "))
discount = int(input("write the dicount: "))
print(f"{product} had price {price}, now with discount of {discount}% costs {round((price*(1-(discount/100))), 2)}, discount was {round(price*(discount/100),2)} zl")
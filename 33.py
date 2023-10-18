password= str(input("write your password,min 8 characters: "))
flag=True
if(len(password)>=8):
    flag=True
else:
    flag=False
print(f"Password is acceptable: {flag}")
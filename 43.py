name=str(input("Write your name  "))
incode_name=""
for i in range (len(name)):
    incode_name+=f"{name[i]}:{ord(name[i]),}"
print(incode_name)
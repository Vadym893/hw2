binary = str(input("write your binary number: "))

result= 0
for i in range(len(binary)):
    if(binary[i]=="0" or binary[i]=="1"):
        continue
    else:
        exit()

for i in range(len(binary)):
    if(binary[len(binary)-i-1]=="1"):
        result += (2 ** i)
    else:
        result+=0

print(result)
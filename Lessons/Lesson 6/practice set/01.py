#Important
num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
num3 = int(input("enter number3:"))
num4 = int(input("enter number4:"))
# print (max(num1,num2,num3,num4 )) #max function find maximum of given numbers -->told by vscode

if(num1>num4):
    f1 = num1
else:
    f1 = num4
    

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print("maximum is: ", f1)
else:
    print("maximum is: ",f2)



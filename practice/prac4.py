a = int(input("Number: "))
prime = True
for i in range(2,a):
    if a%i==0:
        prime = False  
        break
if(prime):
    print("prime") 
else:
    print("not prime")              
    
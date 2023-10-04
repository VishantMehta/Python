sub1 = int(input("Enter marks of subject 1:\n "))
sub2 = int(input("Enter marks of subject 2: \n"))
sub3 = int(input("Enter marks of subject 3: "))

if(sub1>33 or sub2>33 or sub3>33):
    print("you are fail")
elif((sub1+sub2+sub3)/3 <40):
    print("You are fail due to low total")    
else:
    print ("Congratulations you are pass")






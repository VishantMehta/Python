text = input("enter the text: ")

if("make a lot of money" in text): #--> used "in"  
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("The text is not spam")
letter = '''Dear <|NAME|>,You are Selected

Date: <|DATE|>
'''
name = input("Enter Your Name: ")
date=input('Enter Date: ')
letter= letter.replace("<|NAME|>",name)
letter=letter.replace('<|DATE|>',date)
print(letter)


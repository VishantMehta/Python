myDict = {
    "fast": "In a Quick Manner",
    "vansh": "A Coder",
    "marks" : [1,2,5],  #in values of key you can put anything  even list , another dictionary 
    "anotherdict":{"vansh":"player"}
}
# Dictionary methods

# print(myDict.keys()) #--> prints all the keys of  the taken dictionary

# print(type(myDict.keys())) #Type of keys printed are not in list they are of different type but we can cast them in list by list(myDict.key())

# print(myDict.values()) #--> prints the value of dictionary

#print(myDic.items()) #-->prints the (keys,values) of dictionary or basically the content of dictionary

# updatedict = {
#     "Lovish": "Friend",
#     "Divya" : "friend"
# }
# myDict.update(updatedict) #-->Update the dictionary by adding key value pairs from updatedict , it also can update the existing values. 
# print(myDict)

# print(myDict.get("vansh")) #prints value associated with key.
# print(myDict["vansh"]) #prints value associated with key.
#      #difference b/w them
# print(myDict.get("vansh2")) #doesnt throw error as it just search if the key is present.if present give value , if not give none.
# print(myDict["vansh"]) #throws an error as vansh2 is not present.





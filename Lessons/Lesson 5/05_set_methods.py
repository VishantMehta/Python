#Creating a empty set
b = set()

#adding values to empty set:
b.add(4)
b.add(4) #even if u add 4 two times , it will take only one 4 as items cant repeat in sets
b.add(5)
b.add(5)
b.add(7)
# b.add([4,5,6])#can't add list to set as list is hashable (can be changed later)
# b.add({4:5})#can't add dictionary to set as list is hashable (can be changed later)
b.add((4,5,6))# can add tuple as its hashable

#Lenght of the set
# print(len(b)) #print length of set
#Removal of an item
# b.remove(5) #remove 5 from set b

#Pop 
# print(b.pop()) #removes randome element from set





print(b)









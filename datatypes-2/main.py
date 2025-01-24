#dictionaries:
#it is a collection of items in the form of key-value pairs
# my_dict = {key:value}
#it can have duplicate values but not duplicate keys
#keys and values can be of any datatype
#we can update the dictionary so it is mutable.

my_dict = {1:"hello",2:7,3:False,"hey":9,"hey":7}
print(my_dict[1])
print(my_dict["hey"])
my_dict["hey"] = 15
print(my_dict)
print(my_dict["hey"])


#set : unordered collection of items
#wont allow duplicates
#in single execution multiple print statements will print in the same order but in the next execution the order wont be the same
set = {1,2,3,3,4,5,4,"hey"}
print(set)
print(set)
print(set)


#None: none is a datatype which stores nothing in the memory block
#when a var is assigned None it refers to an empty memory block which stores nothing 

a = None
print(a)
print(type(a))
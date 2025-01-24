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

#input():
# it is a function that takes input from the user.
# by deafult the type of the input is string
# if we want to change the type of the input taken we have to type cast it
# to make it readable we have to give a prompt in the double qoutes in the input() so that user will understand what to do

num = input()   #user wont understand what to do as there is no prompt message
num = input("enter the number: ")       # now the user will understand to enter a number
num1 = input("enter the number: ")
num2 = input("enter the second number: ")
print(num1+num2) #5 6 5+6 will return 56 not 11 as they are considered as strings
num = int(input("enter the number: "))  # the entered number will be of string so we are converting it into int before storing it in the variable

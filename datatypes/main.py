#Datatypes : strings,list,tuple,range,boolean

#List: it is a collection of elememts of different datatypes
my_list = [1,2,3,"str",["hey",-2,-4,0]]
print(type(my_list)) #<class 'list'>
print(my_list[0]) #1
print(my_list[-1]) #[-2,-4,0]
print(my_list[4][2]) #0
print(len(my_list)) #5
print(len(my_list[4][0])) #3

#Tuple: it is a collection of elememts of different datatypes but the main difference between list and tuple is it is immutable.
# list vs tuple:
# --> list is mutable whereas tuple is immutable
# --> list is slower whereas tuple is faster
# --> tuple's memory is more efficient as it is immutable so nothing changes
my_tuple1 = ()
my_tuple2 = (1,2,"heylo",24.5,(67,89,43),[78,"misty"])
print(my_tuple2[0]) #1
print(my_tuple2[4][2]) #43
print(my_tuple2[5][1]) #misty

# range : (lower,upper) --> lower(inclusive) && upper(exclusive)
# range(0,10)
# range(0,10,-1)
# range(0,10,2)
# range(10,0,-1)

#boolean : True or False 
# true --> 1
# false --> 0

# print(123=="123")














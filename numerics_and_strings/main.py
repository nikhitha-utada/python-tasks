# slicing using strings with positive indexing
str1="hey this is a string to check all the indexing possibilities"
print(str1[7: ])
print(str1[7: 23])
print(str1[24])
print(str1[23: 7: -1])
print(str1[23: 7])

# slicing using strings with negative indexing
print(str1[-24: -7])
print(str1[-7:-24: -1])
print(str1[-4: -30: -3])

# to know the address value assigned in memory block for a particular variable
str1='hi'
print(id(str1))
str2='hi'
print(id(str2))
str3='str'
print(id(str3))
str4='str'
print(id(str4))
str5='hey'
print(id(str5))
str6='hey'
print(id(str6))

# ..................few datatypes in python.......................
# int(example:2,56,12345, and so on)
2
print(type(2))
# float(example:21.23,5.6,12345.33333, and so on)
5.6
print(type(5.6))
# complex(example:2+3j,6+7j, and so on)
6+7j
print(type(6+7j))
# string(example:'hey',"there", and so on)
str1='hey'
print(type(str1))


# strings are immutable as their sub strings cannot be changed once declared but we can re-assign the entire string to avoid ambiguity in python
str2='Hey There!! How you doing..'
print(str2[12]) 
#now lets try to change a specific index value
str2[12]='p'
print(str2[12])  #it throws an error as strings are immutable and connot be changed but can be re-assigned (the entire string should be changed).

# an alternative is re-assigning it.
str2='Hey There!! pow you doing..'
print(str[12])
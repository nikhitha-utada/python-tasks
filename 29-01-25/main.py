#Logical Operators: they return the operands as the output not only true and false
# and, or, not
# and 
#   --> both should be true
#   --> if the first operator is false output will be false
#   --> even if one operator is false the output will be false
#   --> in logical operator it is not mandatory that true and false will be printed
#   --> if a is true then the output depends on b (a and b)

print(True and False)   #False
print(False and False)  #False
print(True and True)    #True
print(False and False)  #False
print(False and (True and True and True)) #False
print(True and (False and False))   #False

print("--------- Numbers ------------")

# Falsy : 0, None, "", False
# Truthy : Except falsy all are truthy values
# Incase of numbers and strings
print(2 and 3)
print(False and 4)
print(False and "")
print(""  and 3)
print(0 and "")
print("hello" and "hi")
print(True and "empty")
print(None and 3)

# OR: or
# If any one of the operand is false then the output is false
# (a or b) --> if a is false then the output is false
print(True or False)
print(False or True)
print(2 or 3) # if both are truthy then frst operand will be returned
print(None or "") # if both are falsy then frst operand will be returned
print("" or "hello")

#NOT : complement of the input
# if true  <--> false 
# only true or false will be returned unlike and and or

print(not 2)
print(not "")
print(not None)

# Bitwise operators --> &, |, ~, >>, <<, ^
# Note: In logical operators we decide only which operand to return but in bitwise operators the output will be different from the input
#process : 
#        convert it into zeroes and ones
#        now perform the operations bit by bit

print(4 & 12) 
# 4 --> bin(4)--> 0100 (8421 code)
# 12 --> bin(12) --> 1100 (8421 code)
# 0 1 0 0 
#   &
# 1 1 0 0 
# --------
# 0 1 0 0 --> 4 will be output

print(12 | 15)
 
# 12 --> bin(12)--> 1100 (8421 code)
# 15 --> bin(15) --> 1111 (8421 code)
# 1 1 0 0 
#   |
# 1 1 1 1 
# --------
# 1 1 1 1 --> 15 will be output


# xor --> same input then 0 will be output or else 1 will be output
#  0 ^ 0 --> 0
#  0 ^ 1 --> 1
#  1 ^ 0 --> 1
#  1 ^ 1 --> 0
 
print(4 ^ 7)

# 4 --> bin(4)--> 0100 (8421 code)
# 7 --> bin(7) --> 0111 (8421 code)
# 0 1 0 0 
#   ^
# 0 1 1 1 
# --------
# 0 0 1 1 --> 3 will be output

# LEFT SHIFT : <<




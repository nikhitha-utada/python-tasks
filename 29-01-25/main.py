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






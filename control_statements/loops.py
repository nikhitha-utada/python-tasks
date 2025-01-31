#LOOPS:
# To do repeated tasks
# Uses:
#  --> Time
#  --> Money
#  --> Efficiency
#  --> Readable
#  --> less lines of code
#  --> Easier to maintain
#  Types of loops:
    # for loop
    # while loop
    # do while

#  for loop:
# syntax : for i in range(start,end):
#               statements

# Problem Statement-1:
# To print even numbers in the range
# Method-01:
for i in range(0,21):
    if i%2==0:
        print(i)

# Method-02:
for i in range(0,21,2):
    print(i)

#  Problem Statement-2:
# To print mulitples of 3:

for x in range(0,50):
    if x%3==0:
        print(x)

# Problem Statement-3:
# To print odd numbers without using %

for i in range(1,10,2):
    print(i)

# Problem Statement-4:
# To print squares and cubes

for i in range(1,50):
    print(i**2)

# Nested loops:
# syntax: for i in range(start,end):
#           for j in range(start,end):
#                 statements

for outer in range(1,11):
    for inner in range(1,11):
        print(outer,inner) 

# while loops:
# the loop runs until the condition fails
# ctrl c --> keyboard interruption
# syntax : while condition:
#               statements

num=10
while(num>5):
    print(num)
    num-=1

# When to prefer for and while loops:
#  we prefer for loop when we know the number of iterations and while loop when we dont know the number of iterations

num = 5
while(num<26):
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")
    num+=1

# Problem-02:
num = 5
while(num<26):
    if(num%2==0):
        print(num,"even")
    else:
        print(num,"odd")
    num+=1

# converting for to while:
outer = 1
inner = 1
while outer < 11:
    if outer!=5 and outer!=7:
        # inner = 1
        while inner < 11:
            print(outer,inner)
            inner+=1
    outer+=1









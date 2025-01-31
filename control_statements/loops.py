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














# Conditional statements:
#if statement:
# if condition:
    # statements
# else:
    #statements
# Note:
    # Indentation specifies that the code belongs to a same block of code
    # --> atleast one space is required to define the same level block
    # --> preferred indentation is 4 spaces(1 tab)
    # --> there is no rule that both if and else should have same number of spaces but the only thing that is considered is single block of statements should have same level of indentation


# There is an issue here that is if we provide 0 as an input, then it prints negative (It is syntactically correct but logically incorrect)
# num = int(input("Enter the number: "))
# if num>0:
#     print(f"{num} is Positive")
# else:
#     print(f"{num} is Negative")

# # Logically correct Code
num = int(input("Enter the number: "))
if num>0:
    print(f"{num} is Positive")
else:
    if num==0:
        print("It is zero")
    else:
        print(f"{num} is Negative")


# Problem Statement: To print 1 if the input is 1 and to print postive for rest all positive numbers.
num = int(input("Enter the number: "))
if num>0:
    if num==1:
        print("Entered value is 1")
    else:
        print(f"{num} is Positive")
else:
    if num==0:
        print("It is zero")
    else:
        print(f"{num} is Negative")

# else if:
#     AS the requirements are increasing the complexity of the code is increasing so we use else if (elif)
# num>0 and num != 1:  -->another way
#     print(positive)


num = int(input("Enter the number: "))
if num == 0:
    print("0")
elif num == 1:
    print("1")
elif num > 0:
    print("Positive")
elif num == -1:
    print("-1")
elif num == -2:
    print("-2")
else:
    print("negative")


#  Problem Statement : Current bill
#  100 units --> per unit 50 rupees
#  101 to 200 --> per unit 100 rupees
#  201 to 300 --> per unit 150

current_units = int(input("Enter the current units: "))
# if current_units < 0:
#     print("Enter valid current units")
if current_units <= 100:
    current_units *= 50
elif current_units >= 101 and current_units <= 200:
    current_units *= 100
elif current_units >= 201 and current_units <= 300:
    current_units *= 150
else:
    current_units*= 200
print(f"Cost of Current units is {current_units}")


# Only using if and else:
current_units = int(input("Enter the current units: "))
# if current_units < 0:
#     print("Enter valid current units")
if current_units <= 100:
    current_units *= 50
else:
    if current_units >= 101 and current_units <= 200:
        current_units *= 100
    else:
        if current_units >= 201 and current_units <= 300:
            current_units *= 150
print(f"Cost of Current units is {current_units}")


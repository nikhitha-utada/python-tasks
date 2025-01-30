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


# There is an issue here that is if we provide 0 as an input, then it prints negative 
num = int(input("Enter the number: "))
if num>0:
    print(f"{num} is Positive")
else:
    print(f"{num} is Negative")


# function = A block of code that can be runned whenever you want.
# The functions are usefull for spending less time on the same code.
# Here is how to call a function: function_name()

# Now lest create simple function:
def example():
    if i == 1:

        print(f"Hey that is Hey for first time!")
    else:
        print(f"Hey thay is Hey for {i} times")

i = 1
while i < 5:
    example()
    i +=1
# If you dont understand the While code make sure  to see Python While folder!

print(" ") # This is just simple space

# Now I will show you how you can use these () to add temporary variables
def example_2(name, date):
    print(f"Hey the name set in the argument is {name}")
    print(f"The date today is {date}")

example_2("John", "01.05.2025")

# While can be used for so many things as good example for the functions.


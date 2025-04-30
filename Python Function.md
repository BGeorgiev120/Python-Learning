# Python Functions

## What are Functions?
Functions are blocks of code that can be executed whenever needed. They are useful for:
- Reducing code repetition
- Organizing code into logical units
- Making code more readable and maintainable

## Basic Function Syntax
To call a function: `function_name()`

## Simple Function Example
```python
def example():
    if i == 1:
        print(f"Hey that is Hey for first time!")
    else:
        print(f"Hey thay is Hey for {i} times")

# Using the function in a loop
i = 1
while i < 5:
    example()
    i += 1
# If you need more information about While loops, check the Python While folder!
```

The above code creates a simple function and calls it multiple times in a while loop.

## Function Parameters
Functions can accept parameters (inputs) that allow you to pass data to them:

```python
def example_2(name, date):
    print(f"Hey the name set in the argument is {name}")
    print(f"The date today is {date}")

# Calling the function with arguments
example_2("John", "01.05.2025")
```

## When to Use Functions
- When you need to use the same code multiple times
- When you want to break down complex tasks into smaller, manageable pieces
- When you want to make your code more readable and organized

Functions work well with loops and other Python structures to create efficient, reusable code.
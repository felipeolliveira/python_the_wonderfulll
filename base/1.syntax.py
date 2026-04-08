# This is a simple Python script to demonstrate basic syntax and control flow.
"""
This is a docstring that provides a description of the script.
It can be used to explain the purpose of the code and how it works.
In this case, it is just a placeholder text to show where the docstring would go in a real script.
"""

print("Sintaxy Test")

variable = 10

if variable > 5:
    print("Variable is greater than 5")
else:
    print("Variable is less than or equal to 5")

#
# Typing:
# - Python is a dynamically typed language, which means that you don't need to declare the type of a variable when you create it.
# - However, you can use type hints to indicate the expected type of a variable, function parameter, or return value.
# - Type hints are not enforced by the Python interpreter, but they can be used by tools like linters and IDEs to provide better code analysis and autocompletion.
# - Is strongly recommended to use type hints to create contracts, functions, and variables that knows their type, this will help to avoid bugs and make the code more readable and maintainable.
name = "Alice"
name = 0  # This is valid in Python, but it can lead to confusion and errors if not used carefully.

age: int = 30
# This is also valid, but it can lead to confusion and errors if not used carefully.
# If use a linter with type checking (basedpyright, ruff, etc), it will raise a warning or error.
# age = "thirty"


# This function knows that type of arguments and return value, this is a good practice to avoid bugs and make the code more readable and maintainable.
def sum(x: int | float, y: int | float) -> int | float:
    return x + y

#
# Functions:
# - reusable pieces of code that perform a specific task
# - can take inputs (parameters) and return outputs (return values)
# - help to organize code and make it more modular
# - can be defined using the 'def' keyword followed by the function name and parentheses
# - can have a docstring (a string literal that describes the function) for documentation purposes, which is placed immediately after the function definition


def greet(name: str) -> str:
    """This function takes a name as input and returns a greeting message."""
    return f"Hello, {name}!"


print(greet("Alice"))


def square(x: int) -> int:
    """This function takes a number as input and returns its square."""
    return x * x


target = 5
print(f"The square of {target} is: {square(target)}")

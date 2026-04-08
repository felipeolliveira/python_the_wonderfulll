#
# Tuples
# - Are immutable sequences, meaning they cannot be changed after creation.
# - Can contain elements of different types.
# - Are defined using parentheses ().
#

my_tuple = (1, "hello", 3.14, [1, 2, 3], (4, 5))
print("My Tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Output: 1
print("Second element:", my_tuple[1])  # Output: "hello"
print("Last element:", my_tuple[-1])  # Output: (4, 5)

# Tuples are immutable, so you cannot change their elements
# The following line would raise an error:
# my_tuple[0] = 10  # This will raise a TypeError

#
# Tuple unpacking
# - You can unpack a tuple into individual variables.
#
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Tuple methods
# - count(): Returns the number of times a specified value appears in the tuple.
# - index(): Returns the index of the first occurrence of a specified value.
print("Count of 1 in my_tuple:", my_tuple.count(1))  # Output: 1
print("Index of 'hello' in my_tuple:", my_tuple.index("hello"))  # Output: 1

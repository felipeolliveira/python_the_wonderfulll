#
# Lists
# - Lists are ordered, mutable collections of items. They can contain elements of different types, including other lists.
# - Lists are defined using square brackets [] and can be modified after creation.
# - You can perform various operations on lists, such as indexing, slicing, appending, and using built-in list methods.
#

my_list = [1, "hello", 3.14, [1, 2, 3], True]
second_element = my_list[1]
slicing = my_list[
    1:4
]  # This will return a new list containing the elements from index 1 to index 3 (index 4 is not included)
slicing_from_start = my_list[
    :3
]  # This will return a new list containing the first three elements of the original list
slicing_to_end = my_list[
    2:
]  # This will return a new list containing the elements from index 2 to the end of the original list
all_but_last = my_list[
    :-1
]  # This will return a new list containing all elements of the original list except the last one
every_two_elements = my_list[
    ::2
]  # This will return a new list containing every second element of the original list, starting from the first element (index 0)


print("\n\nList Operations:")
print("My List:", my_list)
print("Second Element:", second_element)
print("Slicing (index 1 to 3):", slicing)
print("Slicing from start (first 3 elements):", slicing_from_start)
print("Slicing to end (from index 2 to end):", slicing_to_end)
print("All but last element:", all_but_last)
print("Every two elements:", every_two_elements)

#
# List methods
#

print("\n\nList Methods:")

my_list.append("new element")
print("After append:", my_list)

my_list.insert(2, "inserted element")
print("After insert at index 2:", my_list)

my_list.remove("hello")
print("After remove 'hello':", my_list)

# Remove and return the last element of the list
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

my_list.reverse()
print("After reverse:", my_list)

# Sort will only work if all elements in the list are of the same type and are comparable.
# If you try to sort a list with elements of different types, it will raise a TypeError.
list_of_numbers = [10, 55, 34, 12, 13, 6, 788]
print("Before sort:", list_of_numbers)
list_of_numbers.sort()
print("After sort:", list_of_numbers)

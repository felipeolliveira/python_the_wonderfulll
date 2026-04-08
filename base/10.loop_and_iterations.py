#
# Loops
# - for: used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
#   - use the range() function to generate a sequence of numbers for iteration
#   - use the enumerate() function to get both the index and the value when iterating over a sequence
# - while: used to execute a block of code as long as a condition is true
# - break: used to exit a loop prematurely
# - continue: used to skip the current iteration of a loop and move to the next one
# - else: can be used with loops to execute a block of code when the loop is finished (not when it is exited with break)
#

#
# FOR
#
print("\n\nFor Loop:")

my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print("Number from list:", num)

my_tuple = ("a", "b", "c")
for letter in my_tuple:
    print("Letter from tuple:", letter)

my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in my_dict:
    print("Key from dictionary: %s = %s" % (key, my_dict[key]))

for key, value in my_dict.items():
    print("Key from dictionary(items): %s = %s" % (key, value))

print("\n\nFor Loop with range:")

for i in range(5):
    print("Number from range:", i)

for i in range(0, len(my_list)):
    print("Number from list using index with range: %d = %d" % (i, my_list[i]))

for index, value in enumerate(my_list):
    print("Number from list using enumerate: %d = %d" % (index, value))

#
# WHILE
#

print("\n\nWhile Loop:")
count = 0
limit = 10
while count < limit:
    print("Count in while:", count)
    count += 1

count = 0
while True:
    print("Count in infinite while with break:", count)
    count += 1
    if count >= limit:
        break

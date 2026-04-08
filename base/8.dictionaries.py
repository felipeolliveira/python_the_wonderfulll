#
# Dictionary:
# - Unordered collection of key-value pairs
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any type
# - Defined using curly braces {}
#

my_dict = {
    "name": "John",
    "age": 30,
    "is_eternal_student": True,
    "classes": ["Math", "Science", "History"],
    "address": {"street": "123 Main St", "city": "Anytown", "zip": "12345"},
}

print("My Dictionary:", my_dict)

# Accessing values in a dictionary
name = my_dict["name"]
age = my_dict["age"]
is_eternal_student = my_dict["is_eternal_student"]
classes = my_dict["classes"]
city = my_dict["address"]["city"]

print("\n\nAccessing Values")
print("Name:", name)
print("Age:", age)
print("Is Eternal Student:", is_eternal_student)
print("Classes:", classes)
print("City:", city)

# Modifying values in a dictionary
my_dict["age"] = 31  # Update age
my_dict["classes"].append("Art")  # Add a new class to the list
my_dict["address"]["reference"] = "Near the park"  # Add a new key-value pair to the nested dictionary
print("\n\nModified Dictionary")
print(my_dict)

#
# Dictionary methods:
# - keys(): Returns a view object containing the keys of the dictionary.
# - values(): Returns a view object containing the values of the dictionary.
# - items(): Returns a view object containing the key-value pairs of the dictionary as tuples.
# - get(key, default): Returns the value for the specified key if it exists, otherwise returns the default value.
#
# - These view objects are dynamic and reflect changes to the dictionary. They cannot be modified directly,
#   but they can be converted to lists if needed.
#

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
name_value = my_dict.get("name", "Unknown")

print("\n\nDictionary Methods")
print("Keys:", keys, "Type:", type(keys))
print("Values:", values, "Type:", type(values))
print("Items:", items, "Type:", type(items))
print("Get 'name':", name_value)

keys_list = list(keys)
values_list = list(values)
items_list = list(items)
first_item = items_list[0]  # Access the first item (key-value pair) in the items list

print("\n\nConverted to Lists")
print("Keys List:", keys_list, "Type:", type(keys_list))
print("Values List:", values_list, "Type:", type(values_list))
print("Items List:", items_list, "Type:", type(items_list))
print("First Item (key-value pair):", first_item)

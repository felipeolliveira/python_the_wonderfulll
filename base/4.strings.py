# Strings:
# - Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# - They can contain letters, numbers, symbols, and whitespace.
# - Strings are immutable, meaning they cannot be changed after they are created.
# - You can perform various operations on strings, such as concatenation, slicing, and using built-in string methods.
#

name = "John"
last_name = "Doe"
role = "Software Developer"

# Can use triple quotes for multi-line strings
role_description = """John Doe is a Software Developer with extensive experience in Python and web development.
He has worked on various projects, including web applications, data analysis, and automation scripts.
John is passionate about learning new technologies and improving his skills in software development."""

# Can use backslashes to continue a string on the next line without adding a newline character
hobbies = "John enjoys hiking, \
playing guitar, and cooking in his free time."

print("\n\nString Operations:")
print("Name:", name)
print("Last Name:", last_name)
print("Role:", role)
print("Role Description:", role_description)
print("Hobbies:", hobbies)

#
# Interpolation and concatenation
#
full_name_f = f"{name} {last_name}"
full_name_concat = name + " " + last_name
full_name_substitution = (
    "%s %s" % (name, last_name)
)  # This method preserve the type of the variables, so if you use a number it will not be converted to a string
full_name_format_method = "{} {}".format(name, last_name)

print("\n\nString Interpolation and Concatenation:")
print("Full Name (f-string):", full_name_f, "f''")
print("Full Name (+):", full_name_concat)
print("Full Name (%):", full_name_substitution)
print("Full Name (format method):", full_name_format_method)

#
# String methods
#
lower_name = full_name_f.lower()  # Convert to lowercase
upper_name = full_name_f.upper()  # Convert to uppercase
title_name = (
    full_name_f.title()
)  # Convert to title case, where the first letter of each word is capitalized
replaced_role = role.replace("Developer", "Engineer")  # Replace a substring
split_role = role.split()  # Split the string into a list of words
first_letter = full_name_f[0]  # Get the first letter of the string
last_letter = full_name_f[-1]  # Get the last letter of the string
count_o = full_name_f.count("o")  # Count the number of occurrences of 'o' in the string
index_o = full_name_f.find(
    "o"
)  # Find the index of the first occurrence of 'o' in the string
encode_bytes = full_name_f.encode()  # Encode the string to bytes
decode_string = encode_bytes.decode()  # Decode the bytes back to a string
remove_leading_and_trailing = (
    "   John Doe   ".strip()
)  # Remove leading and trailing whitespace (if any)
starts_with_john = full_name_f.startswith(
    "John"
)  # Check if the string starts with "John"
ends_with_doe = full_name_f.endswith("Doe")  # Check if the string ends with "Doe"

print("\n\nString Methods:")
print("Lowercase Name:", lower_name)
print("Uppercase Name:", upper_name)
print("Title Case Name:", title_name)
print("Replaced Role:", replaced_role)
print("Split Role:", split_role)
print("First Letter of Name:", first_letter)
print("Last Letter of Name:", last_letter)
print("Count of 'o' in Name:", count_o, ", Type:", type(count_o))
print("Index of 'o' in Name:", index_o, ", Type:", type(index_o))
print("Encoded Name (bytes):", encode_bytes, ", Type:", type(encode_bytes))
print("Decoded Name (string):", decode_string)
print(
    "Name with Leading and Trailing Whitespace Removed:",
    remove_leading_and_trailing,
)
print("Does the name start with 'John'?", starts_with_john)
print("Does the name end with 'Doe'?", ends_with_doe)

#
# Operators with strings
#
o_in_name = "o" in full_name_f  # Check if 'o' is in the string
not_o_in_name = "o" not in full_name_f  # Check if 'o' is not in the string
repeated_name = full_name_f * 3  # Repeat the string 3 times

print("\n\nString Operators:")
print("Is 'o' in the name?", o_in_name)
print("Is 'o' not in the name?", not_o_in_name)
print("Repeated Name:", repeated_name)

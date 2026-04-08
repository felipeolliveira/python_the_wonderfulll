#
# Variables in Python
#
name = "John"
last_name = "Doe"
age = 30
height = 1.75
is_student = True
classes = ["Math", "Science", "History"]
roles = ("Admin", "User", "Guest")
languages = {"Python": "Programming", "English": "Language", "Spanish": "Language"}

# Types of variables
# Use the type() function to check the type of each variable
print("\n\nVariable Types:")
print("Name:", name, "Type:", type(name))
print("Last Name:", last_name, "Type:", type(last_name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Is Student:", is_student, "Type:", type(is_student))
print("Classes:", classes, "Type:", type(classes))
print("Roles:", roles, "Type:", type(roles))
print("Languages:", languages, "Type:", type(languages))

#
# Type conversion
#
age_str = str(age)  # Convert age to a string
height_int = int(
    height
)  # Convert height to an integer (this will truncate the decimal part)
is_student_str = str(is_student)  # Convert is_student to a string

print("\n\nType Conversion:")
print("Age as string:", age_str, "Type:", type(age_str))
print("Height as integer:", height_int, "Type:", type(height_int))
print("Is Student as string:", is_student_str, "Type:", type(is_student_str))

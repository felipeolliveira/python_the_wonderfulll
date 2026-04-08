#
# Conditionals are used to control the flow of a program based on certain conditions. In Python, we use if, elif, and else statements to create conditionals.
# - if: This statement is used to check a condition. If the condition is true, the code block under the if statement will be executed.
# - elif: This statement is used to check another condition if the previous if statement was false. You can have multiple elif statements to check multiple conditions.
# - else: This statement is used to execute a code block if all the previous conditions (if and elif) were false. It is optional and can be omitted if you don't need to handle the case where all conditions are false.
# - You can also use logical operators (and, or, not) to combine multiple conditions in a single if statement.
#

age = 25
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Logical operators

is_student = True
has_id = False
if is_student and has_id:
    print("You are eligible for a student discount.")
elif is_student and not has_id:
    print("You need to show your ID to get the student discount.")
elif not is_student and has_id:
    print("You are not a student, but you have an ID.")
else:
    print("You are not a student and you don't have an ID.")

if age < 18 or age >= 65:
    print("You are eligible for a discount.")

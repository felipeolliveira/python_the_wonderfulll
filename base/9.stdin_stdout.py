#
# Standard Input (stdin):
#   - The default source of input for a program is the keyboard.
#   - You can use the input() function to read a line of text from the user.
#   - The input() function returns the input as a string.
#   - You can convert the input to other data types if needed (e.g., int, float).
#

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

imc = weight / (height ** 2)

#
# Standard Output (stdout):
#   - The default destination for output from a program is the console (terminal).
#   - You can use the print() function to display output to the user.
#

print("Your IMC is:", imc)

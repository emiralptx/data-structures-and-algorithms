user_string = input("Enter a string: ")
contains_digit = False

for char in user_string:
    if char.isdigit():
        contains_digit = True
        break  # Exit the loop once a digit is found

if contains_digit:
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")
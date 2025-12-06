user_input_string = input("Enter a String: ")
print(f"Original String is: {user_input_string}")

print("Printing only even index characters")
for i in range(0,len(user_input_string),2):
    print(user_input_string[i], end="\n")
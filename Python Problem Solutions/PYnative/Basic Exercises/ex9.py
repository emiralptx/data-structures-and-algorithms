def is_palindrome_number(number):
    """Checks if a given number is a palindrome.

  A palindrome number reads the same forwards and backward.

  Args:
    number: An integer to be checked.

  Returns:
    True if the number is a palindrome, False otherwise.
    """
    num_str = str(number)
    reversed_str = num_str[::-1]

    return num_str == reversed_str

try:
    num = int(input("Enter a number: "))

    if is_palindrome_number(num):
        print(f"The number {num} is a palindrome.")
    else:
        print(f"The number {num} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter an integer.")
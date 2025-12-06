def remove_chars_from_start(original_string,n):
    """
    Removes the first 'n' characters from a string and returns a new string.

  Args:
    original_string: The input string.
    n: The number of characters to remove from the beginning.

  Returns:
    A new string with the first 'n' characters removed.
    If 'n' is greater than or equal to the length of the string, an empty string is returned.
    If 'n' is negative, the original string is returned.
    """
    if n < 0:
        return original_string
    if n >= len(original_string):
        return ""
    return original_string[n:]

# Example usage:
my_string = "Hello World"
n_to_remove = 5
new_string = remove_chars_from_start(my_string, n_to_remove)
print(f"Original string: '{my_string}'")
print(f"New string after removing first {n_to_remove} characters: '{new_string}'")
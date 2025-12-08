def capitalize_words_manual(input_string):
  """
  Capitalizes the first letter of each word in a string by splitting, 
  capitalizing each word, and then joining.
  """
  words = input_string.split()  # Split the string into a list of words
  capitalized_words = [word.capitalize() for word in words] # Capitalize each word
  return " ".join(capitalized_words) # Join the capitalized words back with spaces

# Example usage
my_string = "another example string"
capitalized_string = capitalize_words_manual(my_string)
print(capitalized_string)
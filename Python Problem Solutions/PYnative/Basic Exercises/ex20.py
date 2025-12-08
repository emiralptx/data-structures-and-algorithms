def print_pattern(rows):  
  for i in range(1, rows + 1):
    for j in range(rows - i + 1):
      print(i, end=" ")
    print()

# Print the pattern with 5 rows
print_pattern(5)
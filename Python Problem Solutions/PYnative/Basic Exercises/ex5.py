def check_first_last(input_list):
    """
    Checks if the first and last numbers of a list are the same.

  Args:
    input_list: A list of numbers.

  Returns:
    True if the first and last numbers are the same, False otherwise.
    Returns False if the list has less than two elements.
    """
    if len(input_list) < 2:
        return False
    else:
        return input_list[0] == input_list[-1]
    
# Example usage:
list1 = [10, 20, 30, 10]
list2 = [1, 2, 3, 4]
list3 = [5]
list4 = []

print(f"List {list1}: {check_first_last(list1)}")
print(f"List {list2}: {check_first_last(list2)}")
print(f"List {list3}: {check_first_last(list3)}")
print(f"List {list4}: {check_first_last(list4)}")
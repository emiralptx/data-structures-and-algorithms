def combine_odd_even(list1,list2):
    """
    Creates a new list containing odd numbers from the first list
    and even numbers from the second list.

    Args:
        list1: The first list of numbers.
        list2: The second list of numbers.

    Returns:
        A new list containing odd numbers from list1 and even numbers from list2.
        """
    new_list = []

    # Add odd numbers from list1
    for num in list1:
        if num %2 != 0:
            new_list.append(num)

    # Add even numbers from list2
    for num in list2:
        if num %2 ==0:
            new_list.append(num)

    return new_list

# Example usage:
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [10, 11, 12, 13, 14, 15]

combined_list = combine_odd_even(list_a, list_b)
print(combined_list)
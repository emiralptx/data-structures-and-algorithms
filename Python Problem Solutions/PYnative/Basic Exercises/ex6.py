def divisible_by_5(input_list):
    """Displays numbers from a list that are divisible by 5.

  Args:
    numbers_list: A list of integers.
    """
    print("Numbers divisible by 5: ")
    for number in input_list:
        if number % 5 == 0:
            print(number)

# Example usage:
my_list = [10, 7, 25, 12, 30, 8, 45, 11]
divisible_by_5(my_list)
previous_num = 0

for current_number in range(10):
    sum_of_numbers = current_number + previous_num
    print(f"Current: {current_number}, Previous: {previous_num}, Sum: {sum_of_numbers}")
    previous_num = current_number
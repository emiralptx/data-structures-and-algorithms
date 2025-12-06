def get_digits_reverse(number):
    digits= []

    abs_number = abs(number)
    while abs_number > 0:
        digit = abs_number %10
        digits.append(digit)
        abs_number //= 10
    return digits

num = 12345
reversed_digits = get_digits_reverse(num)
print(f"Digits of {num} in reverse order: {reversed_digits}") 
# Output: Digits of 12345 in reverse order: [5, 4, 3, 2, 1]
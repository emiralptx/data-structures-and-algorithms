def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    if product <=1000:
        return product
    else:
        return num1 + num2

result1 = calculate_product_or_sum(20,30)
print(f"The result for 20 and 30 is: {result1}")

result2= calculate_product_or_sum(40,30)
print(f"The result for 40 and 30 is: {result2}")
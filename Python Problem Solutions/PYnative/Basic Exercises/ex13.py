for i in range(1,11):
    print(f"Multiplication Table of {i}:")
    for j in range(1, 11):
       product = i*j
       print(f"{i} x {j} = {product}")
    print("-" * 20)  # Separator for readability between tables
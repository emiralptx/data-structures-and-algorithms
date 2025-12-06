def exponent(base,exp):
    """Calculates the power of a base raised to an exponent.

  Args:
    base: The base number (integer).
    exp: The exponent (integer).

  Returns:
    An integer representing base raised to the power of exp.
    """
    if exp < 0:
        # Handle negative exponents, returning 0 for integer results
        # or consider raising an error/returning a float if desired.
        return 0
    

    result = 1

    for i in range(exp):
        result *=base

    return result

print(exponent(2,5))
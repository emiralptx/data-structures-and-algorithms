def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_alternate_primes(limit):
    """Prints alternate prime numbers up to a given limit."""
    prime_count = 0  # Counter for prime numbers found
    for num in range(2, limit + 1):
        if is_prime(num):
            if prime_count % 2 == 0:  # Print only alternate primes (0th, 2nd, 4th, etc.)
                print(num, end=" ")
            prime_count += 1

print_alternate_primes(20)
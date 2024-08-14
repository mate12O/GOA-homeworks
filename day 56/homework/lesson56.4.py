def multiply_number(n):
    if n % 2 == 0:
        return n * 8
    else:
        return n * 9

# Example usage
print(multiply_number(4))  # Output: 32 (since 4 is even)
print(multiply_number(5))  # Output: 45 (since 5 is odd)
def check_even_odd(num):
    """Check if a number is even or odd"""
    if num % 2 == 0:
        return f'{num} is Even'
    else:
        return f'{num} is Odd'

# Example usage:
print(check_even_odd(10))  # Output: 10 is Even
print(check_even_odd(7))   # Output: 7 is Odd
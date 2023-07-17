
def get_even_numbers(numbers):
    """This function uses list comprehension to filter out even numbers from a list."""
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    numbers = list(range(10))
    print(get_even_numbers(numbers))

def generate_numbers(min_value, max_value):
    while min_value < max_value:
        yield min_value
        min_value += 1

numbers = generate_numbers(10, 20)
print(type(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
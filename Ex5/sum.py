def my_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + my_sum(numbers[1:])
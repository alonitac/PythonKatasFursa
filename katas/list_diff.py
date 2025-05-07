def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    if len(numbers) == 0:
        return 0
    max = min = numbers[0]
    for num in numbers:
        min = num if num < min else min
        max = num if num > max else max
    return max - min


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed
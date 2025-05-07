def sum_of_digits(input_str):
    """
    Calculates the sum of all digits in the given string.

    Args:
        input_str: the string containing digits and other characters

    Returns:
        the sum of all digits in the string
    """
    s = 0
    zero_ascii_val = ord('0')
    for ch in input_str:
        ch_ascii_val = ord(ch)
        diff_brtween_ch_and_zero_in_ascii = ch_ascii_val - zero_ascii_val
        if 0<=diff_brtween_ch_and_zero_in_ascii<=9 :
            s += diff_brtween_ch_and_zero_in_ascii

    return s


if __name__ == '__main__':
    input0 = "123"
    input1 = "abc123"
    input2 = "5 cats and 2 dogs"
    input3 = "No digits here!"
    print(f"Sum of digits in '{input0}': {sum_of_digits(input0)}")  # Should be 6
    print(f"Sum of digits in '{input1}': {sum_of_digits(input1)}")  # Should be 6
    print(f"Sum of digits in '{input2}': {sum_of_digits(input2)}")  # Should be 7
    print(f"Sum of digits in '{input3}': {sum_of_digits(input3)}")  # Should be 0
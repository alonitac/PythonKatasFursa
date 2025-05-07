def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """
    bucket = [0] * 128
    string = string.lower()
    for ch in string:
        ascii_val_of_ch = ord(ch)
        bucket[ascii_val_of_ch]+=1
    for b in bucket:
        if b > 1 :
            return False
    return True    


if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"
    test0 = "Aa"
    print(f'"{test0}" has all unique characters: {is_unique(test0)}') 
    #print(f'"{test1}" has all unique characters: {is_unique(test1)}')  # Should be False (has repeated 'l')
    #print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    #print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    #print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be True
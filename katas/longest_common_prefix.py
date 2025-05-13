def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    i = 0
    while True:
        if i >= len(strs[0]):
            return strs[0][0:i]
        current_char_to_check = strs[0][i]
        for s in strs:
            if i >= len(s) or s[i] != current_char_to_check:
                return s[0:i]
        i += 1

if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]
    test5 = ["majd","majd","majd","majd","majd"]
    test6 = ["ab","a"]
    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")
    print(f"Longest Common Prefix: {longest_common_prefix(test5)}")
    print(f"Longest Common Prefix: {longest_common_prefix(test6)}")


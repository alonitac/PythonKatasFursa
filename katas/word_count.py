def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    split_sentence_to_words = sentence.split()
    c = 0
    # punctions doesn't count
    for s in split_sentence_to_words:
        if s not in [",",".","?","!","(",")",":",";","[","]"] and s[0] +"" not in [",",".","?","!","(",")",":",";","[","]"]:
            c+=1

    return c


if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words . "
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed
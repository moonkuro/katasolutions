def longest_word(text):
    text = text.split()
    longest_one = max(text, key=len)
    return longest_one
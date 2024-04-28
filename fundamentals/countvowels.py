def get_count(sentence):
    vowelCount = 0
    for v in sentence:
        if v in 'a' 'e' 'i' 'o' 'u':
            vowelCount += 1
    return vowelCount

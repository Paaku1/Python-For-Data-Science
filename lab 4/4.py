def is_pangram(sentence):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence)

    return alphabet_set <= sentence_set

# Example usage:
user = input()  # "The quick brown fox jumps
print(is_pangram(user))

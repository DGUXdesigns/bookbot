def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}

    for char in text:
        letter = char.lower()

        if letter not in char_count:
            char_count[letter] = 1
        else:
            char_count[letter] += 1
    
    return char_count
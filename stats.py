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

def get_count_list(dictionary):
    result = []

    for char in dictionary:
        if char.isalpha():
          result.append({"char": char, "num": dictionary[char]})

    result.sort(key=sort_on, reverse=True)

    return result

def sort_on(items):
  return items["num"]
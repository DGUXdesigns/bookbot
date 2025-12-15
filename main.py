from stats import get_word_count, get_char_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)

    print(f"Found {num_words} total words")
    print(char_count)


    
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


main()
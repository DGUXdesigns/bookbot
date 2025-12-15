from stats import get_word_count, get_char_count, get_count_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1)
    

    book_text = get_book_text(sys.argv[1])
    
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    char_list = get_count_list(char_count)
    print_report(sys.argv[1], num_words, char_list)
    

    
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def print_report(book_path, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()
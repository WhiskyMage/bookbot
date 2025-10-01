from stats import get_num_words
from stats import count_characters

def get_book_text(path_to_file):
        with open(path_to_file) as f:
                book_text = f.read()
                return book_text
                        
def main():
        book_path = "./books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)

        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {book_path}...")
        print ("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print ("--------- Character Count -------")
        char_count = count_characters(text)
        print(f"Found {char_count} total characters")


main()

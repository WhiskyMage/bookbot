from stats import get_num_words
from stats import count_characters
from stats import organizer
import sys

def get_book_text(path_to_file):
        with open(path_to_file) as f:
                book_text = f.read()
                return book_text
                        
def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        else: 
                pass

        book_path = sys.argv[1]
        
        

        text = get_book_text(book_path)
        num_words = get_num_words(text)

        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {book_path}...")
        print ("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print ("--------- Character Count -------")
        char_count = count_characters(text)
        sort_char = organizer(char_count)
        for pairs in sort_char:
                print(f"{pairs['char']}: {pairs['num']}")
        #print(f"Found {char_count} total characters")
        print ("============= END ===============")


main()

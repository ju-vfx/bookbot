import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_characters

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = str(sys.argv[1])
    book_text = get_book_text(book_filepath)
    num_words = get_num_words(book_text)
    characters = get_num_characters(book_text)
    sorted_chars = sorted_characters(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")

main()
from io import TextIOWrapper

def get_file(file_name: str) -> str:
    file: TextIOWrapper = open(f'books/{file_name}', "r", encoding="utf-8")
    return file.read()

def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    char_count_dict: dict[str, int] = {}
    for char in text.lower():
        if char not  in char_count_dict:
            char_count_dict[char] = 0
        else:
            char_count_dict[char] = char_count_dict[char] + 1

    return char_count_dict

def character_count_report(text: str) -> None:
    char_count_dict: dict[str, int] = count_characters(text)
    for character, count in char_count_dict.items():
        print(f"The {character} character was found {count} times")

def generate_report(file_name: str, book_text: str, display_text: bool = False) -> None:
    if display_text:
        print(f"--- Displaying text from books/{file_name} ---")
        print(book_text)
        print("--- End file reading ---")
        
    print(f"--- Begin report on books/{file_name} ---")
    print(count_words(book_text))
    character_count_report(book_text)
    print("--- End report ---")

file_name: str = "frankenstein.txt"
book_text: str = get_file(file_name)
generate_report(file_name, book_text)

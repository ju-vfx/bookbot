def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_num_characters(text: str) -> dict:
    character_count = {}

    for char in text:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char.lower()] += 1
    
    return character_count

def sort_key(items):
    return items["num"]

def sorted_characters(characters: dict) -> list:
    char_dict_list = []

    for char in characters:
        if not char.isalpha():
            continue
        count = characters[char]
        char_dict_list.append({"char": char, "num": count})

    char_dict_list.sort(reverse=True, key=sort_key)
    return char_dict_list
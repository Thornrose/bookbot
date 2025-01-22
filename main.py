def main():
    book_path = "books/frankenstein.txt"
    text = ""
    split_words = []
    count_words = 0
    characters = {}
    characters_list = []

    with open(book_path) as f:
        text = f.read()

    lower_text = text.lower()
    split_words = lower_text.split()
    count_words = len(split_words)

    for char in lower_text:
        if char.isalpha() and char not in characters:
            characters[char] = 1
        elif char.isalpha():
            characters[char] = characters[char] + 1

    for char in characters:
        characters_list.append({"letter": char, "count": characters[char]})

    characters_list.sort(key=sort_on) #reverse was optional

    print(f"--- Begin report of {book_path} --- \n {count_words} words found in the document")
    for char in range(len(characters_list)):
        print(f"The '{characters_list[char]['letter']}' character was found {characters_list[char]['count']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()

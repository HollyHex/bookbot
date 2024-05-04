def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_dict = get_letters_dict(text)
    letter_sorted_list = letter_dicts_to_sorted_list(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"Document word count: {word_count}\n")
    for item in letter_sorted_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    return len(words)


def get_letters_dict(text):
    letters = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in letters:
                letters[lowered] += 1
            else: letters[lowered] = 1
    return letters


def sort_on(dict):
    return dict["count"]


def letter_dicts_to_sorted_list(dict_to_sort):
    sorted_list = []
    for letter in dict_to_sort:
        count = dict_to_sort[letter]
        new_dict = {"letter": letter, "count": count}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()

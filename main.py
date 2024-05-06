
def main():
    book_path = "../books/frankenstein.txt"
    text = get_word(book_path)
    num_words = word_count(text)
    new_dict = letter_count(text)
    sorted_list = sorted_dict(new_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")
    report(sorted_list)
    print("--- End report ---")


def get_word(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    word = text.split()
    return len(word)


def letter_count(text):
    count_words = text.lower()
    word_counting = count_words.split()
    word_dict = {}
    for words in count_words:
        for letter in words:
            if letter.isalpha():
                if letter in word_dict:
                    word_dict[letter] += 1
                else: word_dict.update({letter: 1})
    return word_dict


def sorted_dict(new_dict):
    new_list = sorted(new_dict.items(), key=lambda x: x[1], reverse= True)
    converted_dict = dict(new_list)
    return converted_dict


def report(sorted_list):
    keys = sorted_list.items()
    for i in keys:
        print(f"The '{i[0]}' character was found {i[1]} times")


main()

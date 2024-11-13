def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_chars_list(chars_dict)
    chars_list.sort(reverse=True,key=sort_on)
    # print(chars_list)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for item in chars_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_list(dict):
    new_list = []
    for char in dict:
        if char.isalpha():
            new_list.append({
                "char":char,
                "num":dict[char]
            })
    return new_list
     

def sort_on(dict):
    return dict["num"]

main()

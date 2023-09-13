with open("books/frankenstein.txt") as f:
    book = f.read()

def count_words(book):
    words = book.split()
    print(f"{len(words)} words found in the document \n \n")

def count_letters(book):
    alpha_list = []
    each_char = {}
    lower_case_book = book.lower()
    for letter in lower_case_book:
        if letter in each_char:
            each_char[letter] += 1
        else:
            each_char[letter] = 1
    for key in each_char.keys() :
        if key.isalpha():
            count = each_char[key]
            alpha_list.append(key)
            alpha_list.append(count)
    for i in range(0, len(alpha_list), 2):
        print(f"The {alpha_list[i]} character was found {alpha_list[i + 1]} times")

    

print("--- Begin report of books/frankenstein.txt ---")
count_words(book)
count_letters(book)
print("--- End report ---")

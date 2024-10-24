def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    number = get_words(text)
    raw = character_count(text)
    sorted = making_sorted_list(raw) 
    report(sorted, number)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return (f"{len(words)} words found in the document")

def character_count(text):
    lowered_text = text.lower()
    charcount = {}
    for x in lowered_text:
        if x in charcount:
            charcount[x] += 1
        else:
            charcount[x] = 1

    return charcount

def sort_on(d):
    return d["num"]

def making_sorted_list(num_chars_dict):
    sortedList = []
    for ch in num_chars_dict:
        sortedList.append({"char": ch, "num": num_chars_dict[ch]})
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList

def report(sorted, number):
    print("--- Begin report of books/frankenstein.txt ---")
    print(number)
    print("")
    
    for x in sorted:
        if x["char"].isalpha():
            print(f"The '{x['char']}' character was found {x['num']} times")

    print("--- End report ---")

main()


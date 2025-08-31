# read contets of a text file and pass as string
def get_book_text(path):
    with open(path) as book:
        contents = book.read()
    return contents


# calculate word number of string
def get_word_count(text):
    words = text.split()
    return len(words)


# collect used characters and count them
def get_characters_count(text):
    characters = {}
    normalized = text.lower()
    for n in normalized:
        if n not in characters:
            characters[n] = 1
        else:
            characters[n] += 1
    return(characters)


# filter and sort the character list
# only keep letters and sort in descending order
def get_sorted_list(data):
    sorted_list = []
    for char, num in data.items():
        if True == char.isalpha():
            sorted_list.append({"char" : char, "num" : num})
    sorted_list.sort(key = get_key, reverse = True)
    return(sorted_list)


#helper function for sort()
def get_key(item):
    return item["num"]

string = "aabbbccdddddddd"

def get_frequency(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1

    print(chars)
    biggest = [None, 0]
    second = [None, 0]

    for entry in chars.items():
        char, count = entry
        if count > biggest[1]:
            second,biggest= biggest, entry
        elif count > second[1]:
            second = entry


    return {
        "most-occurring": biggest[0],
        "second-most-occurring": second[0]
    }

print(get_frequency(string))
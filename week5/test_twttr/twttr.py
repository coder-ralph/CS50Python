import string

def main():
    word = input("Enter a word: ")
    shortened_word = shorten(word)
    print("Shortened word:", shortened_word)


def shorten(word):
    vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
    punctuation = set(string.punctuation)
    result = ''.join(char for char in word if char not in vowels and char not in punctuation)
    return result


if __name__ == "__main__":
    main()

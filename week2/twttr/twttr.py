def remove_vowels(text):
    vowels = "aeiouAEIOU"
    text_without_vowels = ""
    for char in text:
        if char not in vowels:
            text_without_vowels += char
    return text_without_vowels


def main():
    text = input("Input: ")
    text_without_vowels = remove_vowels(text)
    print("Output:", text_without_vowels)


if __name__ == "__main__":
    main()

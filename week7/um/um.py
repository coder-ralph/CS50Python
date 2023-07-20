import re

# yummy um um. um, um

def main():
    print(count(input("Text: ")))
    
    
def count(s):
    word_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(word_count)

if __name__ == "__main__":
    main()
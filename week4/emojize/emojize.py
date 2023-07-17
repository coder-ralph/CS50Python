import re

emoji_dict = {
    "thumbs_up": "👍",
    "smile": "😄",
    "1st_place_medal": "🥇",
    "money_bag": "💰",
    "smile_cat": "😸",
    "candy": "🍬",
}

def emojize_text(text):
    words = text.split()
    emojized_words = []
    for word in words:
        if word in emoji_dict:
            emojized_words.append(emoji_dict[word])
        else:
            match = re.match(r":(\w+):", word)
            if match and match.group(1) in emoji_dict:
                emojized_words.append(emoji_dict[match.group(1)])
            else:
                emojized_words.append(word)
    return " ".join(emojized_words)

def main():
    user_input = input("Input: ")
    emojized_text = emojize_text(user_input)
    print(f"Output: {emojized_text}")

if __name__ == "__main__":
    main()

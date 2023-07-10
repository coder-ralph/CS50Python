def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100
    }

    fruit = input("Item: ").lower()

    if fruit in fruits:
        calories = fruits[fruit]
        print(f"Calories: {calories}")
    else:
        print("")

if __name__ == "__main__":
    main()

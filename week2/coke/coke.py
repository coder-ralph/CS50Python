def calculate_change(coins):
    total_cents = sum(coins)
    change = total_cents - 50
    return change


def main():
    accepted_coins = [25, 10, 5]
    coins_inserted = []
    total_cents_inserted = 0

    while total_cents_inserted < 50:
        if total_cents_inserted < 50:
            print("Amount Due:", 50 - total_cents_inserted)

        coin = int(input("Insert Coin: "))
        
        if coin in accepted_coins:
            coins_inserted.append(coin)
            total_cents_inserted += coin

    change = calculate_change(coins_inserted)
    print("Change Owed:", change)


if __name__ == "__main__":
    main()

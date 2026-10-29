
import random

PRODUCTS = {
    "1": ["Pocket Sunrise", "Cloud in a Jar", "Self-Folding Rainbow"],
    "2": ["Teleporting Ramen", "Moonlight Milkshake", "Zero-Gravity Donut"],
    "3": ["Homework-Finishing Robot", "Time-Freezing Watch", "Dream Recorder"]
}

EFFECTS = [
    "makes Mondays feel shorter",
    "turns awkward silence into music",
    "lets you understand what cats are thinking",
    "brings one lost sock back from another universe",
    "changes the color of the sky for five seconds"
]


def get_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput stopped. Run this program in the VS Code Terminal.")
        return None


def dispense_product(button):
    product = random.choice(PRODUCTS[button])
    PRODUCTS[button].remove(product)
    effect = random.choice(EFFECTS)
    return product + " - " + effect


def show_bag(bag):
    if len(bag) == 0:
        print("Your shopping bag is empty.")
    else:
        print("\nYOUR IMPOSSIBLE SHOPPING BAG")
        for number, product in enumerate(bag, 1):
            print(str(number) + ". " + product)


def main():
    print("====================================")
    print("  PARALLEL UNIVERSE VENDING MACHINE")
    print("====================================")

    name = get_input("What is your name? ")
    if name is None:
        return
    if name == "":
        name = "Mystery Shopper"

    coins = 5
    bag = []

    print("Welcome, " + name + "!")
    print("You have 5 free space coins.")

    while True:
        print("Coins left:\n", coins)
        print("1. Mystery objects")
        print("2. Impossible snacks")
        print("3. Future technology")
        print("4. View shopping bag")
        print("5. Exit")

        choice = get_input("Choose 1-5: ")
        if choice is None:
            break

        if choice in PRODUCTS:
            if coins == 0:
                print("You are out of space coins!")
            elif len(PRODUCTS[choice]) == 0:
                print("Sold out! Please choose another category.")
            else:
                prize = dispense_product(choice)
                bag.append(prize)
                coins = coins - 1
                print("\nYou received: " + prize)
                
                if coins == 0:
                    print("You used all 5 space coins!")
                    show_bag(bag)
                    print("Thanks for playing!")
                    break

        elif choice == "4":
            show_bag(bag)

        elif choice == "5":
            print("Thanks for visiting, " + name + "!")
            print("You collected", len(bag), "impossible product(s).")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

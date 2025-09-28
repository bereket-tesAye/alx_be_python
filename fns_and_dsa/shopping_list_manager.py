def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Adding to shopping list
            while True:
                new_item = input("Enter name of the item to add: ").strip().lower()
                if new_item in shopping_list:
                    print(f"{new_item} already exists in the shopping list.")
                else:
                    shopping_list.append(new_item)
                    print(f"{new_item} added to shopping list.")
                confirm = input("Do you want to add more? (yes/no): ").strip().lower()
                if confirm != "yes":
                    break

        elif choice == '2':
            # Removing from shopping list
            new_item = input("Enter the item you want to remove: ").strip().lower()
            if new_item in shopping_list:
                shopping_list.remove(new_item)
                print(f"{new_item} removed from shopping list.")
            else:
                print(f"{new_item} is not in the shopping list.")

        elif choice == '3':
            # Viewing shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

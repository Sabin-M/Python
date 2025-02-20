stationary_items = {}

def add_item():
    item_name = input("Enter the name of the item: ")
    brand_name = input("Enter the brand of the item: ")
    stationary_items[item_name] = brand_name
    print("Item added successfully!")

def delete_item():
    item_name = input("Enter the name of the item to delete: ")
    if item_name in stationary_items:
        del stationary_items[item_name]
        print("Item deleted successfully!")
    else:
        print("Item not found!")

def display_items():
    print("Stationary Items:")
    for item, brand in stationary_items.item():
        print(f"{item} - {brand}")

while True:
    print("Menu:")
    print("1. Add item")
    print("2. Delete item")
    print("3. Display items")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        delete_item()
    elif choice == "3":
        display_items()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

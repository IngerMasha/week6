from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Program Menu:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("X - Exit the Program")

def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    item.save()

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
    else:
        print(f"Error: Item '{name}' not found.")

def update_item_from_menu():
    current_name = input("Enter the current name of the item: ")
    current_price = float(input("Enter the current price of the item: "))
    new_name = input("Enter the new name of the item: ")
    new_price = float(input("Enter the new price of the item: "))
    item = MenuManager.get_by_name(current_name)
    if item:
        item.update(new_name, new_price)
    else:
        print(f"Error: Item '{current_name}' not found.")

def view_item_from_menu():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item '{item.name}' found. Price: {item.price}")
    else:
        print(f"Error: Item '{name}' not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("Restaurant Menu:")
        for item in items:
            print(f"{item.name}: {item.price}")
    else:
        print("The restaurant menu is empty.")

def main():
    while True:
        show_user_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == 'V':
            view_item_from_menu()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'X':
            print("Exiting the program. Restaurant Menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
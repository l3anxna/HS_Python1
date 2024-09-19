inventory = {}

def add_item():
    item_name = input("Enter the item name: ")
    item_quantity = int(input("Enter the item quantity: "))
    
    if item_name in inventory:
        inventory[item_name] += item_quantity
    else:
        inventory[item_name] = item_quantity
    
    print(f"Added {item_quantity} of {item_name} to the inventory.")

def view_inventory():
    print("\nChoose how you want to view the inventory:")
    print("1. View as a simple list")
    print("2. View in alphabetical order")
    print("3. View sorted by quantity")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        print("\nCurrent Inventory (Simple List):")
        if not inventory:
            print("The inventory is empty.")
        else:
            for index, (item, quantity) in enumerate(inventory.items(), start=1):
                print(f"{index}. {item}: {quantity}")
    
    elif choice == '2':
        print("\nItems in Alphabetical Order:")
        if not inventory:
            print("The inventory is empty.")
        else:
            for item in sorted(inventory.keys(), key=lambda x: x.lower()):
                print(f"{item}: {inventory[item]}")
    
    elif choice == '3':
        print("\nItems Sorted by Quantity:")
        if not inventory:
            print("The inventory is empty.")
        else:
            for item, quantity in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
                print(f"{item}: {quantity}")
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

def remove_item():
    item_name = input("Enter the item name to remove: ")
    
    if item_name in inventory:
        item_quantity = int(input("Enter the quantity to remove: "))
        
        if item_quantity > inventory[item_name]:
            print(f"Cannot remove {item_quantity} of {item_name}. Only {inventory[item_name]} available.")
        elif item_quantity == inventory[item_name]:
            del inventory[item_name]
            print(f"Removed {item_name} from the inventory.")
        else:
            inventory[item_name] -= item_quantity
            print(f"Removed {item_quantity} of {item_name}.")
    else:
        print(f"{item_name} not found in the inventory.")

def update_item():
    item_name = input("Enter the item name to update: ")
    
    if item_name in inventory:
        new_quantity = int(input(f"Enter new quantity for {item_name}: "))
        inventory[item_name] = new_quantity
        print(f"Updated {item_name} to {new_quantity}.")
    else:
        print(f"{item_name} not found in the inventory.")

def search_item():
    search_item = input("Enter the item name to search: ").lower() 
    
    lower_case_inventory = {key.lower(): value for key, value in inventory.items()}
    
    if search_item in lower_case_inventory:
        print(f"{search_item.capitalize()}: {lower_case_inventory[search_item]}")
    else:
        print(f"{search_item.capitalize()} not found in the inventory.")

def bulk_add_items():
    while True:
        item_name = input("Enter the item name (or type 'done' to finish): ")
        
        if item_name.lower() == "done":
            break
        
        try:
            item_quantity = int(input("Enter the quantity: "))
            if item_quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
            
            if item_name in inventory:
                inventory[item_name] += item_quantity
            else:
                inventory[item_name] = item_quantity
            
            print(f"Added {item_quantity} of {item_name} to the inventory.")
        
        except ValueError:
            print("Please enter a valid quantity.")

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Remove Item")
    print("4. Update Item Quantity")
    print("5. Search Item")
    print("6. Bulk Add Items")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        update_item()
    elif choice == '5':
        search_item()
    elif choice == '6':
        bulk_add_items()
    elif choice == '7':
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
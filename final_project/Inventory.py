inventory = {}
lending_records = {}

def is_valid_item_name(item_name):
    """Check if the item name is valid (more than 3 characters and contains no numbers)."""
    return item_name.isalpha() and len(item_name) > 3

def add_item():
    """Add an item to the inventory."""
    item_name = input("Enter the item name: ").strip().lower()  # Convert input to lowercase
    while not is_valid_item_name(item_name):
        print("Invalid item name! Please enter a name with at least 3 characters and without numbers or special characters.")
        item_name = input("Enter the item name: ").strip().lower()  # Convert input to lowercase

    try:
        item_quantity = int(input("Enter the item quantity: "))
        while item_quantity < 1:
            print("Quantity must be a positive integer.")
            item_quantity = int(input("Enter the item quantity: "))

        # Use lowercase version of item_name for storage
        if item_name in inventory:
            inventory[item_name] += item_quantity
        else:
            inventory[item_name] = item_quantity

        print(f"\nAdded {item_quantity} of {item_name} to the inventory.")
    except ValueError:
        print("Please enter a valid integer for quantity.")

def view_inventory():
    """View the current inventory in different formats."""
    print("\nChoose how you want to view the inventory:")
    print("1. View as a simple list")
    print("2. View in alphabetical order")
    print("3. View sorted by quantity")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        print("\n===============================")
        print("     Current Inventory         ")
        print("===============================")
        if not inventory:
            print("The inventory is empty.")
        else:
            for index, (item, quantity) in enumerate(inventory.items(), start=1):
                print(f"{index}. {item}: {quantity}")
        print("===============================")
    
    elif choice == '2':
        print("\n===============================")
        print("  Items in Alphabetical Order     ")
        print("===============================")
        if not inventory:
            print("The inventory is empty.")
        else:
            for index, item in enumerate(sorted(inventory.keys(), key=lambda x: x.lower()), start=1):
                print(f"{index}. {item}: {inventory[item]}")
        print("===============================")
    
    elif choice == '3':
        print("\n===============================")
        print("     Items Sorted by Quantity   ")
        print("===============================")
        if not inventory:
            print("The inventory is empty.")
        else:
            for index, (item, quantity) in enumerate(sorted(inventory.items(), key=lambda x: x[1], reverse=True), start=1):
                print(f"{index}. {item}: {quantity}")
        print("===============================")
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

def is_valid_borrower_name(borrower_name):
    """Check if the borrower's name is valid (at least 3 characters, no numbers, no special characters)."""
    return len(borrower_name) >= 3 and borrower_name.isalpha()

def lend_item():
    """Lend an item from the inventory."""
    item_name = input("Enter the item name to lend: ").strip().lower()  # Convert to lowercase for case-insensitivity
    available_items = {key.lower(): value for key, value in inventory.items()}
    
    if item_name in available_items and available_items[item_name] > 0:
        borrower_name = input("Enter the borrower's name: ").strip()
        
        # Validate borrower name
        while not is_valid_borrower_name(borrower_name):
            print("Invalid borrower name! It must be at least 3 characters long and contain only letters.")
            borrower_name = input("Enter the borrower's name: ").strip()
        
        try:
            lend_quantity = int(input(f"How many of {item_name} do you want to lend? "))
            while lend_quantity < 1 or lend_quantity > available_items[item_name]:
                if lend_quantity < 1:
                    print("You must lend at least one item.")
                else:
                    print(f"Only {available_items[item_name]} of {item_name} are available for lending.")
                lend_quantity = int(input(f"How many of {item_name} do you want to lend? "))
            
            # Lend the items
            lending_records.setdefault(borrower_name, {})[item_name] = lending_records.get(borrower_name, {}).get(item_name, 0) + lend_quantity
            inventory[item_name] -= lend_quantity
            print(f"Lent {lend_quantity} of {item_name} to {borrower_name}.")
        except ValueError:
            print("Please enter a valid integer for quantity.")
    else:
        print(f"{item_name.capitalize()} is not available for lending.")

def return_item():
    """Return a lent item back to the inventory."""
    borrower_name = input("Enter the borrower's name: ").strip()
    
    if borrower_name in lending_records:
        item_name = input("Enter the item name to return: ").strip().lower()

        # Check if the borrower has this item lent out
        if item_name in lending_records[borrower_name]:
            try:
                return_quantity = int(input(f"How many of {item_name} do you want to return? "))
                
                # Validate return quantity
                while return_quantity < 1 or return_quantity > lending_records[borrower_name][item_name]:
                    if return_quantity < 1:
                        print("You must return at least one item.")
                    else:
                        print(f"Only {lending_records[borrower_name][item_name]} of {item_name} are lent out by you.")
                    return_quantity = int(input(f"How many of {item_name} do you want to return? "))

                # Return the items
                lending_records[borrower_name][item_name] -= return_quantity
                inventory[item_name] += return_quantity
                
                # Clean up if no items are left lent out by this borrower
                if lending_records[borrower_name][item_name] == 0:
                    del lending_records[borrower_name][item_name]
                
                if not lending_records[borrower_name]:  # If no records left for this borrower
                    del lending_records[borrower_name]

                print(f"Returned {return_quantity} of {item_name} from {borrower_name}.")
            
            except ValueError:
                print("Please enter a valid integer for quantity.")
        
        else:
            print(f"{borrower_name} does not have {item_name.capitalize()} lent out.")
    
    else:
        print(f"No records found for {borrower_name}.")

def view_lending_records():
    """View all current lending records."""
    if not lending_records:
        print("\nNo current lending records.")
    else:
        print("\n===============================")
        print("     Lending Records           ")
        print("===============================")
        
        for borrower, items in lending_records.items():
            items_list = ', '.join([f"{key}: {value}" for key, value in items.items()])
            print(f"{borrower}: {items_list}")
        
        print("===============================")

def remove_item():
    """Remove an item from the inventory."""
    item_name = input("Enter the item name to remove: ")

    # Validate item name
    while not is_valid_item_name(item_name):
        print("Invalid item name! Please enter a name without numbers or special characters.")
        item_name = input("Enter the item name to remove: ")
    
    if item_name in inventory:
        try:
            item_quantity = int(input("Enter the quantity to remove: "))
            
            # Validate quantity
            while item_quantity < 1:
                print("Quantity must be a positive integer.")
                item_quantity = int(input("Enter the quantity to remove: "))
            
            if item_quantity > inventory[item_name]:
                print(f"Cannot remove {item_quantity} of {item_name}. Only {inventory[item_name]} available.")
            elif item_quantity == inventory[item_name]:
                del inventory[item_name]
                print(f"Removed {item_name} from the inventory.")
            else:
                inventory[item_name] -= item_quantity
                print(f"Removed {item_quantity} of {item_name}.")
        
        except ValueError:
            print("Please enter a valid integer for quantity.")
    
    else:
        print(f"{item_name} not found in the inventory.")

def update_item():
    """Update the quantity of an existing item."""
    item_name = input("Enter the item name to update: ")

    # Validate item name
    while not is_valid_item_name(item_name):
        print("Invalid item name! Please enter a name without numbers or special characters.")
        item_name = input("Enter the item name to update: ")
    
    if item_name in inventory:
        try:
            new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            
            # Validate new quantity
            while new_quantity < 1:
                print("Quantity must be a positive integer.")
                new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            
            inventory[item_name] = new_quantity
            print(f"Updated {item_name} to {new_quantity}.")
        
        except ValueError:
            print("Please enter a valid integer for quantity.")
    
    else:
        print(f"{item_name} not found in the inventory.")

def bulk_add_items():
    """Add multiple items to the inventory at once."""
    while True:
        item_name = input("Enter the item name (or type 'done' to finish): ")

        # Validate bulk add name
        while not is_valid_item_name(item_name) and item_name.lower() != "done":
            print("Invalid item name! Please enter a name without numbers or special characters.")
            item_name = input("Enter the item name (or type 'done' to finish): ")
        
        if item_name.lower() == "done":
            break
        
        try:
            item_quantity = int(input("Enter the quantity: "))
            
            # Validate quantity
            while item_quantity < 1:
                print("Quantity must be a positive integer.")
                item_quantity = int(input("Enter the quantity: "))
            
            if item_name in inventory:
                inventory[item_name] += item_quantity
            else:
                inventory[item_name] = item_quantity
            
            print(f"Added {item_quantity} of {item_name} to the inventory.")

        except ValueError:
            print("Please enter a valid integer for quantity.")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n===============================")
        print("  University Inventory System   ")
        print("===============================")
        
      # Main Menu Options
        options = [
            "1. Add Item",
            "2. View Inventory",
            "3. Lend Item",
            "4. Return Item",
            "5. View Lending Records",
            "6. Remove Item",
            "7. Update Item Quantity",
            "8. Bulk Add Items",
            "9. Exit"
      ]
      
      # Display options
        for option in options:
            print(option)

        choice = input("\nChoose an option (1-9): ")

      # Handle user choices
        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            lend_item()
        elif choice == '4':
            return_item()
        elif choice == '5':
            view_lending_records()
        elif choice == '6':
            remove_item()
        elif choice == '7':
            update_item()
        elif choice == '8':
            bulk_add_items()
        elif choice == '9':
            print("\nExiting the University Inventory System.")
            break
        else:
            print("\nInvalid choice! Please choose a valid option.")

# Start the program
if __name__ == "__main__":
    main_menu()
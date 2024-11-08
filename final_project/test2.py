class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = {}

    def borrow_item(self, item_name, quantity):
        """Add an item to the user's borrowed items."""
        if item_name in self.borrowed_items:
            self.borrowed_items[item_name] += quantity
        else:
            self.borrowed_items[item_name] = quantity

    def return_item(self, item_name, quantity):
        """Return an item from the user's borrowed items."""
        if item_name in self.borrowed_items:
            if self.borrowed_items[item_name] >= quantity:
                self.borrowed_items[item_name] -= quantity
                if self.borrowed_items[item_name] == 0:
                    del self.borrowed_items[item_name]
                return True
        return False

    def __str__(self):
        """String representation of the user."""
        return f"User: {self.name}, Borrowed Items: {self.borrowed_items}"


class InventorySystem:
    def __init__(self):
        self.inventory = {}
        self.users = {}

    def is_valid_item_name(self, item_name):
        """Check if the item name is valid (more than 2 characters and contains only letters)."""
        assert isinstance(item_name, str), "Item name must be a string."
        return item_name.isalpha() and len(item_name) > 2

    def add_item(self):
        """Add an item to the inventory."""
        item_name = input("Enter the item name: ").strip().lower()
        
        while not self.is_valid_item_name(item_name):
            print("Invalid item name! Please enter a name with at least 3 characters and without numbers or special characters.")
            item_name = input("Enter the item name: ").strip().lower()

        while True:
            try:
                item_quantity = int(input("Enter the item quantity: "))
                assert item_quantity > 0, "Quantity must be a positive integer."

                if item_name in self.inventory:
                    self.inventory[item_name] += item_quantity
                else:
                    self.inventory[item_name] = item_quantity

                print(f"\nAdded {item_quantity} of {item_name} to the inventory.")
                break
            except ValueError:
                print("Please enter a valid integer for quantity.")
            except AssertionError as e:
                print(e)

    def view_inventory(self):
        """View the current inventory in different formats."""
        print("\nChoose how you want to view the inventory:")
        print("1. View as a simple list")
        print("2. View in alphabetical order")
        print("3. View sorted by quantity")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            print("\n===============================")
            print("       Current Inventory   ")
            print("===============================")
            if not self.inventory:
                print("The inventory is empty.")
            else:
                for index, (item, quantity) in enumerate(self.inventory.items(), start=1):
                    print(f"{index}. {item}: {quantity}")
            print("===============================")
        elif choice == '2':
            print("\n===============================")
            print("  Items in Alphabetical Order   ")
            print("===============================")
            if not self.inventory:
                print("The inventory is empty.")
            else:
                for index, item in enumerate(sorted(self.inventory.keys(), key=lambda x: x.lower()), start=1):
                    print(f"{index}. {item}: {self.inventory[item]}")
            print("===============================")
        elif choice == '3':
            print("\n===============================")
            print("     Items Sorted by Quantity   ")
            print("===============================")
            if not self.inventory:
                print("The inventory is empty.")
            else:
                for index, (item, quantity) in enumerate(sorted(self.inventory.items(), key=lambda x: x[1], reverse=True), start=1):
                    print(f"{index}. {item}: {quantity}")
            print("===============================")
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    def lend_item(self):
        """Lend an item from the inventory."""
        borrower_name = input("Enter your name: ").strip()
        
        if borrower_name not in self.users:
            self.users[borrower_name] = User(borrower_name)

        available_items = {key.lower(): value for key, value in self.inventory.items() if value > 0}

        if not available_items:
            print("No items available for lending.")
            return

        print("\nAvailable items for lending:")
        
        for index, (item_name, quantity) in enumerate(available_items.items()):
            print(f"{index + 1}. {item_name}: {quantity}")

        try:
            item_index = int(input("Select the item number you want to lend: ")) - 1
            
            if item_index < 0 or item_index >= len(available_items):
                print("Invalid selection. Please try again.")
                return
            
            chosen_item = list(available_items.keys())[item_index]
            available_quantity = available_items[chosen_item]
            
            lend_quantity = int(input(f"How many of {chosen_item} do you want to lend? "))
            
            if lend_quantity <= 0 or lend_quantity > available_quantity:
                print("Invalid quantity selected.")
                return
            
            self.users[borrower_name].borrow_item(chosen_item, lend_quantity)
            self.inventory[chosen_item] -= lend_quantity
            
            print(f"Lent {lend_quantity} of {chosen_item} to {borrower_name}.")
        
        except ValueError:
            print("Please enter a valid integer.")

    def return_item(self):
        """Return a lent item back to the inventory."""
        borrower_name = input("Enter your name: ").strip()
        
        if borrower_name not in self.users or not self.users[borrower_name].borrowed_items:
            print(f"No records found for {borrower_name}.")
            return
        
        user = self.users[borrower_name]
        
        if user.borrowed_items:
            print("\nItems you have borrowed:")
            
            for index, (item_name, quantity) in enumerate(user.borrowed_items.items(), start=1):
                print(f"{index}. {item_name}: {quantity}")

            try:
                item_index = int(input("Select the number of the item you want to return: ")) - 1
                
                if item_index < 0 or item_index >= len(user.borrowed_items):
                    print("Invalid selection. Please try again.")
                    return
                
                chosen_item = list(user.borrowed_items.keys())[item_index]
                
                return_quantity = int(input(f"How many of {chosen_item} do you want to return? "))
                
                if user.return_item(chosen_item, return_quantity):
                    self.inventory[chosen_item] += return_quantity
                    print(f"Returned {return_quantity} of {chosen_item} from {borrower_name}.")
                else:
                    print(f"You do not have enough of {chosen_item} to return.")
                
            except ValueError:
                print("Please enter a valid integer.")
        
    def view_lending_records(self):
        """View all current lending records."""
        if not self.users:
            print("\nNo current lending records.")
            return

        for user in self.users.values():
            if user.borrowed_items:
                items_list = ', '.join([f"{key}: {value}" for key, value in user.borrowed_items.items()])
                print(f"{user.name}: {items_list}")

    
    def update_item(self):
        """Update the quantity of an existing item."""
        item_name = input("Enter the item name to update: ")

        while not self.is_valid_item_name(item_name):
            print("Invalid item name! Please enter a name without numbers or special characters.")
            item_name = input("Enter the item name to update: ")
        
        if item_name in self.inventory:
            try:
                new_quantity = int(input(f"Enter new quantity for {item_name}: "))
                assert new_quantity > 0, "Quantity must be a positive integer."
                
                self.inventory[item_name] = new_quantity
                print(f"Updated {item_name} to {new_quantity}.")
            
            except ValueError:
                print("Please enter a valid integer for quantity.")
            except AssertionError as e:
                print(e)

    def bulk_add_items(self):
        """Add multiple items to the inventory at once."""
        while True:
            item_name = input("Enter the item name (or type 'done' to finish): ").strip().lower()

            while not self.is_valid_item_name(item_name) and item_name.lower() != "done":
                print("Invalid item name! Please enter a name without numbers or special characters.")
                item_name = input("Enter the item name (or type 'done' to finish): ")
            
            if item_name.lower() == "done":
                break
            
            try:
                item_quantity = int(input("Enter the quantity: "))
                
                assert item_quantity > 0, "Quantity must be a positive integer."
                
                if item_name in self.inventory:
                    self.inventory[item_name] += item_quantity
                else:
                    self.inventory[item_name] = item_quantity
                
                print(f"Added {item_quantity} of {item_name} to the inventory.")

            except ValueError:
                print("Please enter a valid integer for quantity.")
            except AssertionError as e:
                print(e)

    def main_menu(self):
      """Display the main menu and handle user choices."""
      while True:
          options = [
              "1. Add Item",
              "2. View Inventory",
              "3. Lend Item",
              "4. Return Item",
              "5. View Lending Records",
              "6. Update Item Quantity",
              "7. Bulk Add Items",
              "8. Exit"
          ]
          
          # Display options
          for option in options:
              print(option)

          choice = input("\nChoose an option (1-8): ")

          # Handle user choices
          if choice == '1':
              self.add_item()
          elif choice == '2':
              self.view_inventory()
          elif choice == '3':
              self.lend_item()
          elif choice == '4':
              self.return_item()
          elif choice == '5':
              self.view_lending_records()
          elif choice == '6':
              self.update_item()
          elif choice == '7':
              self.bulk_add_items()
          elif choice == '8':
              print("\nExiting the Inventory System.")
              break
          else:
              print("\nInvalid choice! Please choose a valid option.")

if __name__ == "__main__":
    system = InventorySystem()
    system.main_menu()
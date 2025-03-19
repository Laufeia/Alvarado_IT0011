class Item:
    def __init__(self, item_id, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = []

    def create_item(self):
        try:
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            new_item = Item(item_id, name, description, price)
            self.items.append(new_item)
            print("Item added successfully!")
        except ValueError as e:
            print("Error:", e)

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items:
                print(item)

    def update_item(self):
        item_id = input("Enter item ID to update: ")
        for item in self.items:
            if item.item_id == item_id:
                try:
                    item.name = input("Enter new name: ")
                    item.description = input("Enter new description: ")
                    item.price = float(input("Enter new price: "))
                    if item.price < 0:
                        raise ValueError("Price cannot be negative.")
                    print("Item updated successfully!")
                    return
                except ValueError as e:
                    print("Error:", e)
                    return
        print("Item not found.")

    def delete_item(self):
        item_id = input("Enter item ID to delete: ")
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item deleted successfully!")
                return
        print("Item not found.")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.create_item()
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password 

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Service(Item):
    pass  # Salon-specific services

class Product(Item):
    pass  # Salon-specific products

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append({"item": item, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["item"].price * item["quantity"]
        return total

def authenticate_user(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

def generate_bill(cart):
    print("\n========== Salon Bill ==========")
    for item in cart.items:
        item_type = 'Product' if isinstance(item['item'], Product) else 'Service'
        print(f"{item['item'].name} ({item_type}) - Quantity: {item['quantity']} - Price: ${item['item'].price}")
    print("=================================")
    print(f"Total: ${cart.calculate_total():.2f}")
    print("=================================\n")

def display_items(items, item_type):
    print(f"\nAvailable {item_type}s:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item.name} - ${item.price:.2f}")

def choose_items(items, item_type):
    while True:
        display_items(items, item_type)
        try:
            choice = int(input(f"Select a {item_type} (0 to finish): "))
            if choice == 0:
                break
            selected_item = items[choice - 1]
            quantity = 1 if isinstance(selected_item, Service) else int(input(f"Enter quantity for {selected_item.name}: "))
            return selected_item, quantity
        except (IndexError, ValueError):
            print("Invalid input, please try again.")


def main():
    # Sample services and products

    users = [
        User("user1", "pass1"),
        User("user2", "pass2")
    ]

    # Authenticate user
    logged_in_user = authenticate_user(users)
    if logged_in_user is None:
        print("Authentication failed.")
        return
    print(f"Logged in as {logged_in_user.username}")


    services = [
        Service("Basic Haircut", 30.00),
        Service("Hair Coloring", 120.00),
        Service("Styling", 45.00)
    ]

    products = [
        Product("Shampoo", 15.99),
        Product("Conditioner", 14.99)
    ]

    # Create a shopping cart
    cart = ShoppingCart()

    while True:
        print("\n1. Add Service\n2. Add Product\n3. Generate Bill\n")
        choice = input("Choose an option (1-3): ")

        try:
            if choice == '1':
                service, quantity = choose_items(services, 'Service')
                cart.add_item(service, quantity)
            elif choice == '2':
                product, quantity = choose_items(products, 'Product')
                cart.add_item(product, quantity)
            elif choice == '3':
                generate_bill(cart)
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
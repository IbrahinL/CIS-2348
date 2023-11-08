# creating an iteration for the shopping cart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
# adding items to the cart
    def add_item(self, item):
        self.cart_items.append(item)
#adding the remove function of the cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
# adding the modifying function to the code
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
# adding the quantity items are in the cart function
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
# adding the total cost of the cart function to the code
    def get_cost_of_cart(self):
        return sum(item.item_quantity * item.item_price for item in self.cart_items)
# adding the total amount of items in the cart function
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())

        for item in self.cart_items:
            item.print_item_cost()

        total_cost = self.get_cost_of_cart()
        print("\nTotal: $", total_cost)
# adding the description of the item in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
# the print of the cost of the items
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@ $", self.item_price, " = $", self.item_quantity * self.item_price)
# the print of the description of the item
    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)


# implementing the ItemToPurchase class to the code
item1 = ItemToPurchase("Bottled Water", 1.5, 2, "Deer Park, 12 oz.")
item1.print_item_description()


# implementing the ShoppingCart class to the code
cart = ShoppingCart("John Doe", "February 1, 2016")
item1 = ItemToPurchase("Nike Romaleos", 189, 2, "Weightlifting shoes")
item2 = ItemToPurchase("Chocolate Chips", 3, 5, "Semi-sweet")
item3 = ItemToPurchase("Powerbeats 2 Headphones", 128, 1, "Bluetooth headphones")

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

cart.print_total()
cart.print_descriptions()
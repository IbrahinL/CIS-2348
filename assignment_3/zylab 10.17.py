class ItemToPurchase:
    def __init__(self):
        self.first_item_name = ''
        self.first_item_price = 0
        self.first_item_quantity = 0
        self.second_item_name = ''
        self.second_item_price = 0
        self.second_item_quantity = 0
if __name__ == "__main__":
    item = ItemToPurchase()
    print("Item 1")
    first_item_name = input("Enter the item name:")
    print("")
    first_item_price = int(input("Enter the item price:"))
    print("")
    first_item_quantity = int(input("Enter the item quantity:"))
    print("")
    print("")
    print("Item 2")
    second_item_name = input("Enter the item name:")
    print("")
    second_item_price = int(input("Enter the item price:"))
    print("")
    second_item_quantity = int(input("Enter the item quantity:"))
    
    item.first_item_name = first_item_name
    item.first_item_price = first_item_price
    item.first_item_quantity = first_item_quantity
    item.second_item_name = second_item_name
    item.second_item_price = second_item_price
    item.second_item_quantity = second_item_quantity
    first_formula = item.first_item_quantity *item.first_item_price
    second_formula = item.second_item_quantity *item.second_item_price
    print("")
    print("")
    print("TOTAL COST")
    print(f'{item.first_item_name} {item.first_item_quantity} @ ${item.first_item_price:} = ${first_formula:}')
    print(f'{item.second_item_name} {item.second_item_quantity} @ ${item.second_item_price:} = ${second_formula:}')
    total = first_formula + second_formula
    print("")
    print(f'Total: ${total:}')
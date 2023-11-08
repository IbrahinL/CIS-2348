class FoodItem:
# a constructor to initialize a food item
    def __init__(self, name="None"):
        self.item_name = name
        self.amount_fat = 0.0
        self.amount_carbs = 0.0
        self.amount_protein = 0.0
        self.num_servings = 0.0
# get_calories is the formula on the calories
    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
# print_info prints out the information of the food
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
    if __name__ == "__main__":
        item_name = input()
# prints out the serving of the food
        if item_name == 'Water' or item_name == 'water':
            food_item = FoodItem()
            food_item.print_info()
            print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
#
        else:
            amount_fat = float(input())
            amount_carbs = float(input())
            amount_protein = float(input())
            num_servings = float(input())
# prints out the calories and serving of the food
            food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
            food_item.print_info()
            print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
            print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')

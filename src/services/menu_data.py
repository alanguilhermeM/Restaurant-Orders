import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.source_path = source_path
        self.set_dishes()

    def __repr__(self) -> str:
        return f"MenuData('{self.dishes}')"

    def set_dishes(self):
        with open(self.source_path, "r", newline="") as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")
            next(arquivo_csv)

            for row in arquivo_csv:
                dish_name, price, ingredient_name, amount = row
                price = float(price)
                amount = int(amount)

                dish = next((d for d in self.dishes
                            if d.name == dish_name), None)
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), amount
                )

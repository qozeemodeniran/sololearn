class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    # static method: Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
    @staticmethod
    def validate_toppings(toppings):
        if toppings == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]

if all(Pizza.validate_toppings(i) for i in ingredients):
    pizza = Pizza(ingredients)
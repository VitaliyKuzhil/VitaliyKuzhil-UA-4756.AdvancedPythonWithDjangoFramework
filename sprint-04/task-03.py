
class Pizza:

    order_number = 0

    def __init__(self, ingredients):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self.ingredients = ingredients


    @classmethod
    def garden_feast(cls):
        ingredients = ["spinach", "olives", "mushroom"]
        return cls(ingredients)


    @classmethod
    def four_cheese(cls):
        ingredients = ["mozzarella", "gorgonzola", "parmesan", "cheddar"]
        return cls(ingredients)


    @classmethod
    def caesar(cls):
        ingredients = ["chicken", "bacon", "parmesan", "cherry tomatoes", "lettuce", "caesar sauce"]
        return cls(ingredients)



p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()                  # order 2
p3 = Pizza.caesar()                        # order 3


print(p1.ingredients)# ➞ ["bacon", "parmesan", "ham"]
print(p2.ingredients)# ➞ ["spinach", "olives", "mushroom"]
print(p3.ingredients)#  ➞ ["chicken", "bacon", "parmesan", "cherry tomatoes", "lettuce", "caesar sauce"]


print(p1.order_number) # ➞ 1
print(p2.order_number) # ➞ 2
print(p3.order_number) # ➞ 3
import unittest
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def get_discount(self, amount):
        pass



class FivePercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.95



class TenPercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.90



class TwentyPercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.80



class ThirtyPercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.70



class FiftyPercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.50



class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


    def __str__(self):
        return f'Product: {self.name}, units: {self.price}, price per unit: {self.price}'



class Cart:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        total_price = 0

        for item in self.items:
            price_for_units = item.price * item.count
            if 5 <= item.count <= 6:
                total_price += FivePercentDiscount().get_discount(price_for_units)
            elif 7 <= item.count < 10:
                total_price += TenPercentDiscount().get_discount(price_for_units)
            elif 10 <= item.count < 20:
                total_price += TwentyPercentDiscount().get_discount(price_for_units)
            elif item.count == 20:
                total_price += ThirtyPercentDiscount().get_discount(price_for_units)
            elif item.count > 20:
                total_price += FiftyPercentDiscount().get_discount(price_for_units)
            else:
                total_price += price_for_units

        return total_price



class CartTest(unittest.TestCase):

    def setUp(self):

        self.product1 = Product('Apple', 29, 85)
        self.product2 = Product('Orange', 50, 60)
        self.product3 = Product('Lemon', 40, 50)


    def test_add_item_to_cart(self):

        self.cart = Cart([])

        self.cart.add_item(self.product1)

        self.assertIn(self.product1, self.cart.items)
        self.assertEqual(len(self.cart.items), 1)



    def test_get_total_price(self):
        self.products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))

        self.cart = Cart(self.products)

        self.assertAlmostEqual(self.cart.get_total_price(), 24785.0)
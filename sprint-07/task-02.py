from abc import ABC, abstractmethod



class DiscountStrategy(ABC):

    @abstractmethod
    def get_discount(self, amount):
        pass



class OneSaleDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.50



class TwentyPercentDiscount(DiscountStrategy):

    def get_discount(self, amount):
        return amount * 0.80



class Goods: 
  
    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy


    def price_after_discount(self):
        if self.discount_strategy is not None:
            return self.discount_strategy.get_discount(self.price)
        return self.price


    def __str__(self):
        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'



if __name__ == '__main__':

    on_sale_discount = OneSaleDiscount()
    twenty_percent_discount = TwentyPercentDiscount()

    print(Goods(20000))
    print(Goods(20000,twenty_percent_discount))
    print(Goods(20000, on_sale_discount))

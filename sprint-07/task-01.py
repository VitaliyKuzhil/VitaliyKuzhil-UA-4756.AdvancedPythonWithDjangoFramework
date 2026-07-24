from abc import ABC, abstractmethod



class Product(ABC):

    @abstractmethod
    def cook(self):
        pass



class FettuccineAlfredo(Product):
    def __init__(self):
        self.name = 'Fettuccine Alfredo'


    def cook(self):
        return f'Italian main course prepared: {self.name}'



class Tiramisu(Product):
    def __init__(self):
        self.name = 'Tiramisu'


    def cook(self):
        return f'Italian dessert prepared: {self.name}'



class DuckALOrange(Product):
    def __init__(self):
        self.name = 'Duck À L\'Orange'


    def cook(self):
        return f'French main course prepared: {self.name}'



class CremeBrulee(Product):
    def __init__(self):
        self.name = 'Crème brûlée'


    def cook(self):
        return f'French dessert prepared: {self.name}'



class Factory(ABC):

    @abstractmethod
    def get_dish(self, type_of_meal):
        pass



class ItalianDishesFactory(Factory):
    def __init__(self):
        super().__init__()
        self.factory = self.__class__.__name__

    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo()
        elif type_of_meal == 'dessert':
            return Tiramisu()



class FrenchDishesFactory(Factory):
    def __init__(self):
        self.factory = self.__class__.__name__

    def get_dish(self, type_of_meal):
            if type_of_meal == 'main':
                return DuckALOrange()
            elif type_of_meal == 'dessert':
                return CremeBrulee()



class FactoryProducer:
    def __init__(self):
        self.producer = self.__class__.__name__
        self._factories = {'italian' : ItalianDishesFactory(),
                           'french': FrenchDishesFactory()
                           }


    def get_factory(self, type_of_factory):
        try:
            cooker = self._factories.get(type_of_factory)
        except KeyError:
            return 'Unknown type of factory'
        else:
            return cooker



if __name__ == '__main__':

    manager = FactoryProducer()

    italian_cooker = manager.get_factory('italian')
    french_cooker = manager.get_factory('french')

    order_1 = italian_cooker.get_dish('main')
    print(order_1.cook())
    order_2 = italian_cooker.get_dish('dessert')
    print(order_2.cook())

    order_3 = french_cooker.get_dish('main')
    print(order_3.cook())
    order_4 = french_cooker.get_dish('dessert')
    print(order_4.cook())

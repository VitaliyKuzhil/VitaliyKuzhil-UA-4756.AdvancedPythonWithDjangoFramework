
class Washing:

    def wash(self):
        print(f'{self.__class__.__name__} ...')



class Rinsing:

    def rinse(self):
        print(f'{self.__class__.__name__} ...')



class Spinning:

    def spin(self):
        print(f'{self.__class__.__name__} ...')



class WashingMachine(Washing, Rinsing, Spinning):

    def __init__(self):
        self.__washing = Washing()
        self.__rinsing = Rinsing()
        self.__spinning = Spinning()


    def startWashing(self):
        self.__washing.wash()
        self.__rinsing.rinse()
        self.__spinning.spin()




if __name__ == '__main__':

    washing_machine = WashingMachine()

    washing_machine.startWashing()

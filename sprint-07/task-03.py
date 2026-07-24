
class MotorCycle: 
    """Class for MotorCycle"""

    def __init__(self): 
        self.name = self.__class__.__name__


    def TwoWheeler(self): 
        return 'TwoWheeler'


    def __str__(self):
        return self



class Car:
    """Class for Car"""

    def __init__(self): 
        self.name = self.__class__.__name__


    def FourWheeler(self): 
        return 'FourWheeler'


    def __str__(self):
        return self




class Truck: 
    """Class for Truck"""

    def __init__(self): 
        self.name = self.__class__.__name__


    def EightWheeler(self): 
        return 'EightWheeler'


    def __str__(self):
        return self



class Adapter: 
    """ 
    Adapts an object by replacing methods. 
    Usage: 
    motorCycle = MotorCycle() 
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler) 
    """
  
    def __init__(self, obj, **adapted_methods): 
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)


    def __getattr__(self, attr): 
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)
        
  
    def original_dict(self): 
        """Print original object dict"""
        return self.obj.__dict__



if __name__ == '__main__':

    objects = []

    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels = truck.EightWheeler))

    car = Car()
    objects.append(Adapter(car, wheels = car.FourWheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))

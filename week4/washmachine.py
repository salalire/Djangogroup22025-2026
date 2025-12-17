from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turnOn(self):
        pass
    def turnOff(self):
        pass
class WashngMachine(Appliance):
    def turnOn(self):
        print("Washing machine is turned on")
    def turnOff(self):
        print("washing machine is turned on ")
machine1=WashngMachine()
machine1.turnOn()
machine1.turnOff()
from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("turn on Washing Machine")
class Fridge(Appliance):
    def turn_on(self):
        print("turn On Fridge")
wm=WashingMachine()
fr=Fridge()
wm.turn_on()
fr.turn_on()
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class lion(ABC):
    def sound(self):
        print("lion is roaring")

class tigar(ABC):
    def sound(self):
        print("tigar is roaring")

an=lion()
an.sound()

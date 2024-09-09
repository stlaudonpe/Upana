from mammal import Mammal
from head import Head

class Dog(Mammal):
    def __init__(self, name, type, head_size):
        super().__init__(type)  # Llama a Mammal
        self._name = name
        self._head = Head(head_size)  #el perro tiene una cabeza

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def goForWalk(self):
        print(f"{self._name} va a un paseo")

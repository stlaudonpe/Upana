class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.gasoline = 0
        self.distance = 0
        self.next_service = 25

    def __str__(self) -> str:
        return f"Un carro hecho por {self.make}, modelo {self.model} con gasolina {self.gasoline}"

    def __repr__(self) -> str:
        return f"""
            Car 
            Make {self.make}, 
            Model {self.model}"""

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def fill(self, gasoline):
        self.gasoline = gasoline

    def drive(self, distance=10):
        print('Manejando')
        if self.gasoline >= 0:
            self.gasoline = self.gasoline - 1
            self.distance += distance
            if self.next_service < self.distance:
                print("Need service")

    def make_service(self):
        if self.distance > self.next_service:
            print("Servicing")
            self.next_service += 25
        else:
            print("Not servicing")


class Person:
    def __init__(self, name, age, car=None):
        self.name = name
        self.age = age
        self.car = car

    def __str__(self):
        if self.car:
            return f"Persona: {self.name} con edad {self.age} con carro: \n{self.car}"
        return f"Persona: {self.name} con edad {self.age}"

    def modificar_carro(self, car):
        self.car = car

    def manejar_carro(self, car=None):
        if car:
            car.drive()
        if self.car:
            self.car.drive()


corolla = Car("Toyota", "Corolla")
juanito = Person("Juanito", 30, corolla)
pedrito = Person('Pedrito', 15)

pedrito.manejar_carro(corolla)

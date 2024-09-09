from dog import Dog

class Owner:
    def __init__(self, name):
        self._name = name
        # El dueño puede tener varios perros
        self._dogs = []  
        

    def getName(self):
        return self._name

    def walkDog(self):
        for dog in self._dogs:
            dog.goForWalk()

    def addDog(self, dog):
        self._dogs.append(dog)

    def removeDog(self, dog):
        self._dogs.remove(dog)

from owner import Owner
from dog import Dog

if __name__ == "__main__":
    owner = Owner("Luis Audon")
    dog1 = Dog("Dogi", "Chihuahua", "Pequenio")
    dog2 = Dog("Max", "Shitzu", "Mediano")

    owner.addDog(dog1)
    owner.addDog(dog2)

#llama a los metodos 
    owner.walkDog()  

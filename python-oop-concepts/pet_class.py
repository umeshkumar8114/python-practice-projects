# Umesh Kumar U95237454 (Driver)
# Ebin Abraham U52630521 (Navigator)
# ASSIGNMENT 7
# Participation % = 50/50
# Exercise (Pet class and object)


class Pet:
    def __init__(self):  # attributes of the class
        self.__name = 'Not provided'
        self.__type = 'Not provided'
        self.__age = 0

    def set_Name(self, name):  # setter methods
        self.__name = name

    def set_Type(self, type):
        self.__type = type

    def set_Age(self, age):
        self.__age = age

    def get_Name(self):  # getter methods
        return self.__name

    def get_Type(self):
        return self.__type

    def get_Age(self):
        return self.__age


def main():
    pet = Pet()  # creating a object pet
    print("A pet object has been created. Here is the initial information about the pet:")
    print("Name of pet:", pet.get_Name())
    print("Type of pet:", pet.get_Type())
    print("Age of pet:", pet.get_Age())
    print("Let's update the information for a pet!")
    name = input("Enter the pet's name: ")  # take input from the user
    type = input("Enter the type of animal: ")
    age = input("Enter the pet's age: ")
    pet.set_Name(name)
    pet.set_Type(type)
    pet.set_Age(age)
    print("Here is the updated information about the pet:")
    print("Name of pet:", pet.get_Name())
    print("Type of pet:", pet.get_Type())
    print("Age of pet:", pet.get_Age())


main()

from solutionmodels import *


def print_animal_names_in_enclosure_1() -> None:
    query = Animal.select().where(Animal.enclosure == 1)

    for animal in query:
        print(animal.animal_type)


def print_animal_names_alphabetically() -> None:
    """
    Prints the names of the animals alphabetically.
    """
    query = Animal.select(Animal.name).order_by(Animal.name.desc()).limit(1)

    for animal in query:
        print(animal.name)


def print_animal_names_in_savanna_enclosure() -> None:
    """
    Prints all the names of the animals in the savanna enclosure. (savanna_enclosure)
    """
    query = Animal.select().join(Enclosure).where(Enclosure.name == "savanna_enclosure")

    for animal in query:
        print(animal.name)
        print(animal.enclosure.name)


def print_animal_names_in_given_enclosure(enclosure_name: str) -> None:
    """
    Print all the names of the animals in the given enclosure
    """
    query = Animal.select().join(Enclosure).where(Enclosure.name == enclosure_name)

    for animal in query:
        print(animal.name)
        print(animal.enclosure.name)


def add_new_animal(name, animal_type, enclosure):
    Animal.create(name=name, animal_type=animal_type, enclosure=enclosure)


def delete_animal():
    Animal.delete().where(Animal.name == "Sander").execute()


def move_animal_to_new_enclosure(animal: str, new_enclosure: int):
    Animal.update(enclosure=new_enclosure).where(Animal.name == animal).execute()


if __name__ == "__main__":
    # print_animal_names_in_enclosure_1()
    # print_animal_names_alphabetically()
    # print_animal_names_in_savanna_enclosure()
    # print_animal_names_in_given_enclosure("savanna_enclosure")
    # add_new_animal("Sander", 3, 2)
    # delete_animal()
    move_animal_to_new_enclosure("Sander", 3)

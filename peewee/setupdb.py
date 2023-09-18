from models import *
import os
from rich.traceback import install

install()


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_database():
    db.connect()
    db.create_tables(
        [
            ZooKeeper,
            Enclosure,
            DietCategory,
            AnimalType,
            Animal,
            Customer,
            Photo,
            PhotoCaptureAnimal,
        ]
    )
    # ZooKeeper.create(name="peter")

    zookeepers = ["dude", "klaas", "pannekoek", "nicola", "Tesla"]

    for zookeeper in zookeepers:
        ZooKeeper.create(name=zookeeper)

    enclosures = [
        ["dessert", 1],
        ["jungle", 2],
        ["aquarium", 0],
        ["forrest", 3],
        ["lake", 4],
    ]

    for enclosure in enclosures:
        Enclosure.create(name=enclosure[0], feeder=enclosure[1])

    diets_categories = [
        ["herbivore", True, False],
        ["carnivore", False, True],
        ["omnivore", True, True],
    ]

    for category in diets_categories:
        DietCategory.create(name=category[0], plant=category[1], meat=category[2])

    animal_types = [["tiger", 1], ["dog", 2], ["cattle", 0]]

    for animal in animal_types:
        AnimalType.create(name=animal[0], diet_category=animal[1])

    animals = [["siberian tiger", 0, 3], ["labrador", 1, 1], ["cow", 2, 0]]

    for animal in animals:
        Animal.create(name=animal[0], animal_type=animal[1], enclosure=animal[2])

    customers = ["stan", "kyle", "kenny", "cartman", "butters"]

    for customer in customers:
        Customer.create(name=customer)

    photos = [0, 3, 1, 4, 2]

    for i in photos:
        Photo.create(creator=i)

    photo_captured_animals = [[0, 0], [1, 1], [2, 2]]

    for photo_captured_animal in photo_captured_animals:
        PhotoCaptureAnimal.create(
            photo=photo_captured_animal[0], animal=photo_captured_animal[1]
        )

    db.close()


if __name__ == "__main__":
    delete_database()
    populate_database()

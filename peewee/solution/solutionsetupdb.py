from models import *
import os


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

    zookeepers = ["Sander", "Han", "Rik", "Anastasia"]
    for zookeeper in zookeepers:
        ZooKeeper.create(name=zookeeper)

    enclosures = [
        ["barrel", 1],
        ["desert_enclosure", 1],
        ["savanna_enclosure", 3],
        ["jungle_enclosure", 2],
    ]
    for enclosure in enclosures:
        Enclosure.create(name=enclosure[0], feeder=enclosure[1])

    diets = [
        ["carnivore", False, True],
        ["herbivore", True, False],
    ]
    for diet in diets:
        DietCategory.create(name=diet[0], plant=diet[1], meat=diet[2])

    animal_types = [
        ["feline", 1],
        ["reptile", 1],
        ["bird", 2],
    ]
    for animal_type in animal_types:
        AnimalType.create(name=animal_type[0], diet_category=animal_type[1])

    animals = [
        ["phil", 3, 1],
        ["wendy", 3, 1],
        ["simon", 3, 3],
        ["johny", 3, 2],
        ["bob", 1, 3],
        ["carly", 2, 3],
    ]
    for animal in animals:
        Animal.create(name=animal[0], animal_type=animal[1], enclosure=animal[2])

    customers = ["Piet", "Jan"]
    for customer in customers:
        Customer.create(name=customer)

    photos = [2, 1, 1, 2, 1, 2]
    for photo in photos:
        Photo.create(creator=photo)

    photo_captures = [
        [1, 2],
        [5, 4],
        [2, 1],
        [3, 1],
        [1, 1],
    ]
    for photo_capture in photo_captures:
        PhotoCaptureAnimal.create(photo=photo_capture[0], animal=photo_capture[1])

    db.close()


if __name__ == "__main__":
    # delete_database()
    populate_database()

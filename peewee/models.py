from peewee import *

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class ZooKeeper(BaseModel):
    id = AutoField()  # not needed peewee does it automatic
    name = CharField()


class Enclosure(BaseModel):
    name = CharField()
    feeder = ForeignKeyField(ZooKeeper)


class DietCategory(BaseModel):
    name = CharField()
    plant = BooleanField()
    meat = BooleanField()


class AnimalType(BaseModel):
    name = CharField()
    diet_category = ForeignKeyField(DietCategory)


class Animal(BaseModel):
    name = CharField()
    animal_type = ForeignKeyField(AnimalType)
    enclosure = ForeignKeyField(Enclosure, backref="inhabitants")


class Customer(BaseModel):
    name = CharField()


class Photo(BaseModel):
    creator = ForeignKeyField(Customer)


# many to many relatie tussen photo enAnimal, dit is tussen tabel
class PhotoCaptureAnimal(BaseModel):
    photo = ForeignKeyField(Photo, backref="photos")
    animal = ForeignKeyField(Animal)

# Models go here
import peewee

db = peewee.SqliteDatabase("betsy-database.db")


class Tag(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


class Product(peewee.Model):
    name = peewee.CharField()
    description = peewee.TextField(null=True)
    price_in_cents = peewee.IntegerField()
    quantity = peewee.IntegerField()
    # tag = peewee.ForeignKeyField()

    class Meta:
        database = db


class User(peewee.Model):
    name = peewee.CharField()
    address = peewee.CharField()
    billing_info = peewee.CharField()
    # owned_products = peewee.ManyToManyField(Product, null=True)

    class Meta:
        database = db


# class Transaction(peewee.Model):
#     buyer = peewee.ForeignKeyField(User)
#     product = peewee.ForeignKeyField(Product)
#     quantity = peewee.IntegerField()

#     class Meta:
#         database = db

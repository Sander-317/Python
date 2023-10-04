import models
import os
import csv
from rich.traceback import install

install()


def main():
    # get_user_data()
    # print("test")
    delete_database()
    # print("database deleted")
    setup_data()
    # print("database started")


# def get_user_data():
#     with open("betsy-webshop/users.csv", "r") as user_csv:
#         csv_reader = csv.reader(user_csv, delimiter=",")
#         for i in csv_reader:
#             print(i)
#         return csv_reader


def setup_data():
    models.db.connect()
    models.db.create_tables(
        [
            models.Tag,
            models.User,
            models.Product,
            models.ProductTags,
            models.OwnedProducts,
            models.Transaction,
        ]
    )

    # for user, products in user_data:
    #     user = models.User.create(name=user[0], address=user[1], billing_info=user[2])
    #     for product in products:
    #         new_product = models.Product.create(
    #             name=product[0],
    #             description=product[1],
    #             price_in_cents=product[2],
    #             quantity=product[3],
    #             tag=[],
    #         )
    #         for i in product[4]:
    #             current_tags = []
    #             [
    #                 current_tags.append(i.name)
    #                 for i in models.Tag.select(models.Tag.name)
    #             ]
    #             if i not in current_tags:
    #                 models.Tag.create(name=i)
    #             print(models.Tag.get(models.Tag.name == i).id)
    #             new_product.tag.add(models.Tag.get(models.Tag.name == i).id)

    product_data = [
        (
            "Battlefield 9",
            "large scale multiplayer game",
            10000,
            10,
            (["first person shooter", "war simulator", "3d"]),
        ),
        (
            "stardew valley",
            "build your own farm and explore",
            40000,
            10,
            (["farming simulator", "2d top down"]),
        ),
        ("mario 1", "you now what mario is", 60000, 10, (["2d", "nintendo"])),
        ("mario 2", "you now what mario is", 60000, 10, (["2d", "nintendo"])),
        ("mario 3", "you now what mario is", 60000, 10, (["2d", "nintendo"])),
        ("mario 4", "you now what mario is", 60000, 10, (["2d", "nintendo"])),
        (
            "city skyline 2",
            "build your own city",
            60000,
            10,
            (["top down", "city builder"]),
        ),
    ]

    for product in product_data:
        new_product = models.Product.create(
            name=product[0],
            description=product[1],
            price_in_cents=product[2],
            quantity=product[3],
            tag=[],
        )
        for i in product[4]:
            current_tags = []
            [current_tags.append(i.name) for i in models.Tag.select(models.Tag.name)]
            if i not in current_tags:
                models.Tag.create(name=i)
            print(models.Tag.get(models.Tag.name == i).id)
            new_product.tag.add(models.Tag.get(models.Tag.name == i).id)

    user_data = [
        ("dude", "moon 1", "bitcoin", ([])),
        (
            "dudio",
            "mars 1",
            "paypal",
            ([]),
        ),
        (
            "pannekoek",
            "supermarkt 1",
            "paypal",
            ([]),
        ),
        (
            "koek",
            "supermarkt 2",
            "paypal",
            ([]),
        ),
    ]

    for user in user_data:
        new_user = models.User.create(
            name=user[0], address=user[1], billing_info=user[2]
        )
        # for i in user[3]:
        #     new_user.owned_products.add(i)
        # print(user[3])

    transaction = [
        ("dude", "stardew valley", 1),
        ("dude", "mario 4", 1),
        ("dude", "Battlefield 9", 1),
        ("dudio", "Battlefield 9", 1),
        ("dudio", "mario 1", 1),
        ("dudio", "mario 3", 1),
        ("koek", "mario 2", 1),
        ("koek", "city skyline 2", 1),
        ("koek", "mario 4", 1),
        ("pannekoek", "stardew valley", 1),
    ]

    for i in transaction:
        buyer_id = models.User.get(models.User.name == i[0]).id
        product_id = models.Product.get(models.Product.name == i[1]).id
        # print("test buyer: ", test_buyer)
        models.Transaction.create(buyer=buyer_id, product=product_id, quantity=i[2])
        user = models.User.get(models.User.name == i[0])
        user.owned_products.add(i[1])
        user.save()
        product = models.Product.get(models.Product.name == i[1])
        print(product.quantity)
        product.quantity = product.quantity - 1
        product.save()


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy-webshop/betsy-database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()

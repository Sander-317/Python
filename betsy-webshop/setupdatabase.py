import models
import os
from rich.traceback import install

install()


def main():
    print("test")
    setup_data()
    # delete_database()


def setup_data():
    models.db.connect()
    models.db.create_tables(
        [
            models.Tag,
            models.User,
            models.Product,
            #  models.Transaction
        ]
    )

    # tag_data = [("hats"), ("shirt"), ("pants")]

    user_data = [
        (
            ("dude", "moon 1", "bitcoin"),
            [
                (
                    "top hat",
                    "ferry fancy hat",
                    10000,
                    2,
                ),
            ],
        ),
        (
            ("dudio", "mars 1", "paypal"),
            [
                (
                    "polo",
                    "ferry fancy shirt",
                    60000,
                    1,
                ),
            ],
        ),
    ]

    for user, products in user_data:
        user = models.User.create(name=user[0], address=user[1], billing_info=user[2])
        for product in products:
            product = models.Product.create(
                name=product[0],
                description=product[1],
                price_in_cents=product[2],
                quantity=product[3],
            )

    # product_data = [
    #     (
    #         "top hat",
    #         "ferry fancy hat",
    #         10000,
    #         2,
    #     ),
    #     (
    #         "cargo pants",
    #         "ferry roomy pants",
    #         40000,
    #         5,
    #     ),
    #     (
    #         "polo",
    #         "ferry fancy shirt",
    #         60000,
    #         1,
    #     ),
    # ]

    # user_data = [
    #     ("dude", "moon 1", "bitcoin"),
    #     [
    #         (
    #         "top hat",
    #         "ferry fancy hat",
    #         10000,
    #         2,
    #     ),
    #     ]
    #     ("dudio", "mars 1", "paypal"),
    #     ("pannekoek", "supermarkt 1", "paypal"),
    #     ("koek", "supermarkt 2", "paypal"),
    # ]
    # product_data = [
    #     (
    #         "top hat",
    #         "ferry fancy hat",
    #         10000,
    #         2,
    #     ),
    #     (
    #         "cargo pants",
    #         "ferry roomy pants",
    #         40000,
    #         5,
    #     ),
    #     (
    #         "polo",
    #         "ferry fancy shirt",
    #         60000,
    #         1,
    #     ),
    # ]

    # for tag in tag_data:
    #     add_tag = models.Tag.create(name=tag)
    #     print(add_tag.name)

    # for user in user_data:
    #     add_user = models.User.create(
    #         name=user[0], address=user[1], billing_info=user[2]
    #     )
    #     print(add_user.name, add_user.address, add_user.billing_info)

    # for product in product_data:
    #     add_product = models.Product.create(
    #         name=product[0],
    #         description=product[1],
    #         price_in_cents=product[2],
    #         quantity=product[3],
    #     )
    #     print(
    #         add_product.name,
    #         add_product.description,
    #         add_product.price_in_cents,
    #         add_product.quantity,
    #     )


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy-database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()

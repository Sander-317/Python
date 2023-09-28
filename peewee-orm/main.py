import models
import peewee
from typing import List
from rich.traceback import install

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"

install()


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """

    return (
        models.Dish.select(models.Dish.id, models.Dish.price_in_cents)
        .order_by(models.Dish.price_in_cents.asc())
        .first()
    )


def find_dish_diet_preference(dish_ingredient_dict, preference):
    preferred_dish = []
    for dish in dish_ingredient_dict:
        if all(i[preference] == True for i in dish_ingredient_dict[dish]):
            preferred_dish.append(
                {
                    "id": dish.id,
                    "name": dish.name,
                    "served at": dish.served_at_id,
                    "price in cents": dish.price_in_cents,
                }
            )
    return preferred_dish


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    #"""

    all_dishes = models.Dish.select()

    dish_ingredient_dict = {}
    for dish in all_dishes:
        dish_ingredient_dict[dish] = []
        ingredients = models.DishIngredient.select().where(
            models.DishIngredient.dish_id == dish.id
        )
        for ingredient in ingredients:
            ingredient_dict = (
                models.Ingredient.select()
                .where(models.Ingredient.id == ingredient.ingredient_id)
                .dicts()
            )
            for i in ingredient_dict:
                dish_ingredient_dict[dish] += [i]

    vegetarian_dish = []
    for dish in dish_ingredient_dict:
        if all(i["is_vegetarian"] == True for i in dish_ingredient_dict[dish]):
            vegetarian_dish.append(dish)

    # EXTRA
    print("VEGETARIAN")
    print(
        [
            i["name"]
            for i in find_dish_diet_preference(dish_ingredient_dict, "is_vegetarian")
        ]
    )
    print("VEGAN")
    print(
        [i["name"] for i in find_dish_diet_preference(dish_ingredient_dict, "is_vegan")]
    )
    print("GLUTENFREE")
    print(
        [
            i["name"]
            for i in find_dish_diet_preference(dish_ingredient_dict, "is_glutenfree")
        ]
    )

    return vegetarian_dish


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    restaurants = models.Restaurant.select()
    restaurant_rating_dict = {}
    for i in restaurants:
        restaurant_rating_dict[i] = (
            models.Rating.select(peewee.fn.AVG(models.Rating.rating))
            .where(models.Rating.restaurant_id == i)
            .scalar()
        )

    return max(restaurant_rating_dict, key=restaurant_rating_dict.get)


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """

    models.Rating.create(restaurant=4, rating=5, comment="it works yeeey")


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    restaurants = models.Restaurant.select().where(
        models.Restaurant.closing_time > "18:59:00"
    )

    possible_restaurants = []
    for restaurant in restaurants:
        if any(
            [
                all([i.is_vegan for i in dish.ingredients])
                for dish in restaurant.dish_set.select()
            ]
        ):
            possible_restaurants.append(restaurant)

    return possible_restaurants


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """

    dish = models.Dish.create(
        name="A Crappy Dish",
        served_at=4,
        price_in_cents=1000,
    )
    dish.ingredients.add([7, 5, 8])

    return dish

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

    query = (
        models.Dish.select(models.Dish.id, models.Dish.price_in_cents)
        .order_by(models.Dish.price_in_cents.asc())
        .limit(1)
    )
    for dish in query:
        return dish
    # return query.id
    ...


# cheapest_dish()


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    #"""
    not_vegetarian_ingredients = models.Ingredient.select().where(
        models.Ingredient.is_vegetarian == False
    )
    not_vegetarian_ingredients_list = []
    for i in not_vegetarian_ingredients:
        not_vegetarian_ingredients_list.append(i.id)

    dishes_ingredients = models.DishIngredient.select()
    not_vegetarian_dish_id = []
    for i in dishes_ingredients:
        if i.ingredient_id in not_vegetarian_ingredients_list:
            not_vegetarian_dish_id.append(i.dish_id)

    all_dishes = models.Dish.select()
    vegetarian_dish_only = []
    for i in all_dishes:
        if i.id not in not_vegetarian_dish_id:
            vegetarian_dish_only.append(i)

    print(vegetarian_dish_only)
    return vegetarian_dish_only


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    restaurants = models.Restaurant.select()
    ratings = models.Rating.select()
    restaurant_rating_dict = {}
    for restaurant in restaurants:
        restaurant_rating_dict[restaurant.id] = []
        for rating in ratings:
            if rating.restaurant_id == restaurant.id:
                restaurant_rating_dict[restaurant.id] += [rating.rating]
        restaurant_rating_dict[restaurant.id] = sum(
            restaurant_rating_dict[restaurant.id]
        ) / len(restaurant_rating_dict[restaurant.id])
    best_rating = max(restaurant_rating_dict, key=restaurant_rating_dict.get)

    print(best_rating)
    final_answer = models.Restaurant.get(best_rating)
    return final_answer


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """

    models.Rating.create(restaurant=4, rating=5, comment="it works yeeey")

    ...


# add_rating_to_restaurant()


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    vegan_ingredients = models.Ingredient.select().where(
        models.Ingredient.is_vegan == True
    )
    vegan_ingredients_ids = []
    for i in vegan_ingredients:
        vegan_ingredients_ids.append(i.id)

    restaurants = models.Restaurant.select().where(
        models.Restaurant.closing_time > "18:59:00"
    )
    dishes = models.Dish.select()
    dish_ingredients = models.DishIngredient.select()
    test = []
    for restaurant in restaurants:
        for dish in dishes:
            if restaurant.id == dish.served_at_id:
                test.append(dish)

    dish_dict = {}
    for dish in test:
        dish_dict[dish] = []
        for ingredient in dish_ingredients:
            if ingredient.dish_id == dish.id:
                dish_dict[dish] += [ingredient.ingredient_id]

    vegan_dish = ""
    for dish in dish_dict:
        if all(i in vegan_ingredients_ids for i in dish_dict[dish]):
            vegan_dish = dish
    print("test", vegan_dish)
    restaurant_id = models.Dish.get(12)
    print(restaurant_id.served_at_id)
    final_answer = []
    final_answer.append(models.Restaurant.get(restaurant_id.served_at_id))

    return final_answer


dinner_date_possible()


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    print("test")

    dish = models.Dish.create(
        name="A Crappy Dish",
        served_at=4,
        price_in_cents=1000,
    )
    dish.ingredients.add([7, 5, 8])

    return dish

    ...


# add_dish_to_menu()

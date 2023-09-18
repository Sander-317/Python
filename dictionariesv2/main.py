# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport


def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []
        passport["stamps"].append(country)
    else:
        if country not in passport["stamps"]:
            passport["stamps"].append(country)
    print(passport)
    return passport


def add_biometric_data(passport, bio_data_type, bio_data_value, add_date):
    if "biometric" not in passport:
        passport["biometric"] = {}
        passport["biometric"].update(
            {bio_data_type: {"value": bio_data_value, "date": add_date}}
        )
    else:
        passport["biometric"].update(
            {bio_data_type: {"value": bio_data_value, "date": add_date}}
        )
    return passport


# print(add_stamp(create_passport("test", "2020-4-5"," moon", 1.9, "dutch"), "mars"))
omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
print(add_stamp(omari, "amsterdam"))
print(add_stamp(omari, "moon"))
print(add_stamp(omari, "amsterdam"))
print(add_stamp(omari, "mars"))

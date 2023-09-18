# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"


# Add your code after this line
# print(" L8 into dic opdr 1xxxxxxxxxxxxxxx")
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passPort_Items = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": float(height),
        "nationality": nationality,
        # "biometric":{" "}
    }
    return passPort_Items


# {"name":str(name_arg),"date_of_birth":date_of_birth_arg}
print_create_passport = create_passport(
    "Omari Muchumba", "1995-07-16", "Kampala", "184.31", "Uganda"
)
# print (f'R26 {print_create_passport}')#w?y good job
# the end opdr 1, 5 juni 2023 works? y good job
# here start excercise 2:add_stamp: works? yes 6-6-2023 also wincpy check : y good job
# print("opdr 2 Start add_stampxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
list_country = ["china", "japan"]


# print(f'R28: {stamp_list[0]}')
def add_stamp(passport_arg, country):
    # list_country = ["china","japan"]
    # print w? well done
    passPort_dic = {
        "name": passport_arg["name"],  # w?y
        "date_of_birth": passport_arg["date_of_birth"],  # w?y
        "place_of_birth": passport_arg["place_of_birth"],
        "height": passport_arg["height"],
        "nationality": passport_arg["nationality"],  # w?y
        # "stamps":list_country
    }
    if country == passport_arg["nationality"]:  # 1
        print("R 43:Truthy dus stop hier")  # 2
    else:  # 3
        key_stamp = "stamps"
        if key_stamp in passPort_dic.keys():  # 3
            # print("r47 truthy: #5country niet toevoegen aan list_country")#4 w?y
            if country in list_country:
                print(f"r49:country NIET toevoegen in list_country")  # w?y
            else:
                # print(f'r51 voeg country WEL toe aan list_country')#w/y
                list_country.append(country)  # w?y
        else:  # 6
            # print("r 49 falsy")#6
            list1_country = []
            list1_country.append(country)
            # print(f'r59{list1_country}')#w?y
            passPort_dic["stamps"] = list1_country  # w? not yet
            # print(f'r60 {passPort_dic}')#w?not yet
        return passPort_dic


print_add_stamp_return = add_stamp(print_create_passport, "Aruba")
# print(f'r56:{print_add_stamp_return}')#w?
# the end add_stamp
# start: oef/dic/opdr 3:biometric data
print("start opdr 3 :biomatric dataxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
##start: oef/dic/opdr 3:biometric data
print("start opdr 3 :biomatric dataxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


def add_biometric_data(
    print_create_passport_arg1, biometric_data_type, date_arg3, value_arg4
):  # ,eye_color_value_arg2,date_arg3,value_arg4):#w?y
    # voeg toe in regel 11 pasPort_Items dictionary de key met naam:biomatric de type is dictionary
    # biometric_dic={"biometric":{" "}}
    biometric_dic = {
        "biometric": {
            "eye_color_left": {"date": " ", "value": " "},
            "eye_color_right": {"date": "2021_02-02 ", "value": "green "},
        }  # eye_color
    }
    if "biometric" not in print_create_passport_arg1.keys():  # w?y
        # vul biometric_data_type met gegevens: key:date met als waarde date_arg3, idem voor value
        biometric_dic["biometric"][biometric_data_type]["date"] = date_arg3
        # print(f'r93: {biometric}')#w?y
        biometric_dic["biometric"][biometric_data_type]["value"] = value_arg4
        # print(f'r95:{biometric}')#w?y
        print_create_passport_arg1.update(biometric_dic)
        print(f"r98:{print_create_passport_arg1}")
        return print_create_passport_arg1
    else:
        # print("r105 into else")#w?y
        return print_create_passport_arg1


print_return = add_biometric_data(
    print_create_passport, "eye_color_left", "1020-01-01", "pink"
)
print(f"r105:{print_return}")
# print(f'r 112 {print_create_passport}')

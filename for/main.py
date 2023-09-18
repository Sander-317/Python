from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(old_list):
    old_list.sort(key=len)
    shortest_length = len(old_list[0])
    new_list = []
    for item in old_list:
        if len(item) == shortest_length:
            new_list.append(item)
        else:
            continue

    return new_list

def count_vowels(word):
    vowels = [item for item in word if item in "aAeEiIoOuU" ]
    total = len(vowels) + 1
    return total    

def most_vowels(old_list):
    for item_one in range(0, len(old_list)):
        for item_two in range(item_one+1, len(old_list)):
            if count_vowels(old_list[item_one]) < count_vowels(old_list[item_two]):
                old_list[item_one], old_list[item_two] = old_list[item_two], old_list[item_one]
        # print(l)
    
    print("sorted list")
    # print(l)
    print([old_list[0], old_list[1], old_list[2],])
    new_list = [old_list[0], old_list[1], old_list[2]]
    return new_list 

def alphabet_set(old_list):
    new_list = []
    for item in old_list:
        if  "x" in item:
            new_list.append(item[item.index("x")].upper())
        else:
            new_list.append(item[0])
    
    
    return sorted(set(new_list))

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)

    """ Write the calls to your functions here. """

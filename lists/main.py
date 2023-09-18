# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(list):
    list.sort()
    return list


def won_golden_globe(movie):
    winners = ["jaws", "star wars: episode iv - a new hope", "e.e. the extra-terrestrial", "memoirs of a geisha", ]
    if movie.lower() in winners:
        return True
    else: 
        return False



def remove_toto_albums(input_list):
    toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Toto XIV", "Old Is New" ]
    new_list = []
    for item in input_list:
        if item in toto_albums:
            input_list.remove(item)
            print("in toto album")
        else:
            new_list.append(item)
   
    return new_list


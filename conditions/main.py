# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


# def main():
#     print("main")

def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    action = ""
    # take cows to cowshed
    if location_of_cows == "pasture" and time_of_day == "night":
        # return "take cows to cowshed"
        # action.append("take cows to cowshed") 
        action = action + "take cows to cowshed\n" 
    elif weather == "rainy" and location_of_cows == "pasture":
        # return "take cow to cowshed"
        # action.append("take cow to cowshed") 
        action = action + "take cow to cowshed\n" 
    # milk cows
    # elif cow_milking_status == True and location_of_cows == "cowshed":
    #     # return "milk cows"
    #     # action.append("milk cows") 
    #     action = action +  "milk cows\n" 
    elif cow_milking_status == True:
        if location_of_cows == "pasture":
            action = action + "take cows to cowshed\n"
            action = action + "milk cows\n"
            action = action + "take cows back to pasture\n"
        elif location_of_cows == "cowshed":
            action = action +  "milk cows\n" 
    # fertilize pasture
    elif slurry_tank == True and location_of_cows == "cowshed" and weather != "sunny" and weather != "windy":
        # return "fertilize pasture"
        # action.append("fertilize pasture") 
        action = action +  "fertilize pasture\n" 
    # mow grass
    elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "cowshed":
        # return "mow grass"
        # action.append("mow grass") 
        action = action +  "mow grass\n" 
    # wait
    else:
        # return "wait"
        # action.append("wait")
        action = action +  "wait\n"

    return action[:-1]     

    
# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
# print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
# print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False,True))
# print(farm_action('sunny', 'night', True, 'pasture', 'spring', False,True))
# if __name__ == '__main__':
#     main()
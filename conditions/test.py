
def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    weather2 = weather
    time_of_day2 = time_of_day
    cow_milking_status2 = cow_milking_status
    location_of_cows2 = location_of_cows
    season2 = season
    slurry_tank2 = slurry_tank
    grass_status2 = grass_status
    action = ""
    # take cows to cowshed
    if location_of_cows2 == "pasture" and time_of_day2 == "night":
        # return "take cows to cowshed"
        # action.append("take cows to cowshed") 
        location_of_cows2 = "cowshed"
        action = action + "take cows to cowshed\n" 
    elif weather2 == "rainy" and location_of_cows2 == "pasture":
        # return "take cow to cowshed"
        # action.append("take cow to cowshed") 
        action = action + "take cow to cowshed\n" 
    # milk cows
    elif cow_milking_status2 == True and location_of_cows2 == "cowshed":
        # return "milk cows"
        # action.append("milk cows") 
        action = action +  "milk cows\n" 
    # fertilize pasture
    elif slurry_tank2 == True and location_of_cows2 == "cowshed" and weather2 != "sunny" and weather2 != "windy":
        # return "fertilize pasture"
        # action.append("fertilize pasture") 
        action = action +  "fertilize pasture\n" 
    # mow grass
    elif grass_status2 == True and season2 == "spring" and weather2 == "sunny" and location_of_cows2 == "cowshed":
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
print(farm_action('sunny', 'night', True, 'pasture', 'spring', False,True))
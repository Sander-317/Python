# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_goal_one = "Ruud Gullit"
scorer_goal_two = "Marco van Basten" 

goal_0 = 32
goal_1 = 54

scorers = scorer_goal_one + " " + str(goal_0) +", " + scorer_goal_two + " " + str(goal_1)
report = f"{scorer_goal_one} scored in the {goal_0}nd minute\n{scorer_goal_two} scored in the {goal_1}th minute"

player = "Igor Belanov"
# first_name = slice(0 , player.find(" ", 0, len(player)) ) 
first_name = player[slice(0 , player.find(" ", 0, len(player)) )] 
last_name = player[slice(player.find(" ", 0, len(player)) ,len(player)  )] 
last_name_len = len(last_name) - 1 
name_short = f"{first_name[0]}.{last_name}"
chant_name = f"{first_name}! " * len(first_name)
chant = chant_name[:-1]
good_chant = chant[len(chant) -1 ] != " "
print (good_chant)


# print(player[first_name])
print(first_name + last_name +  " " + str(last_name_len))
print(name_short)
print(chant)
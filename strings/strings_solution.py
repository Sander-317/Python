# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line

# --Part 1--

# 1
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
# Use parenthesis to create 'string' variables

# 2
goal_0 = 32
goal_1 = 54
# Use plain numbers to create 'integer' variables

# 3
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
# When using the + operator, use casting to change integer to string.


# 4
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"
# F-strings do not require casting.
# \n starts a next line immediately, avoid using spaces around this.

# --Part 2--

# 1
player = "Hennadiy Lytovchenko"

# 2
first_name = player[: player.find(" ")]
# By looking for the space the code will work with any name.

# 3
last_name_len = len(player[player.find(" ") + 1 :])
# Use '+ 1' here to start the slice at the character after the space"

# 4
name_short = f"{player[0]}.{player[player.find(' '):]}"

# 5
chant_with_space = f"{first_name}! " * len(first_name)
chant = chant_with_space[:-1]
# Use slicing to remove the space from the end.

# 6
good_chant = chant[-1] != " "

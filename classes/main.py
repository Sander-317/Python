# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        
        if 0 <= speed <= 1:
                self.speed = speed
        else:
            raise ValueError("needs to be a number between 0 and 1")
       
        if 0 <= endurance <= 1:
            self.endurance = endurance
        else:
            raise ValueError("needs to be a number between 0 and 1")
        
        if 0 <= accuracy <= 1:
                self.accuracy = accuracy
        else:
            raise ValueError("needs to be a number between 0 and 1")

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."
    
    def strength(self):
        new_list = []
        new_list.append(("speed", self.speed))
        new_list.append(("endurance", self.endurance))
        new_list.append(("accuracy", self.accuracy))
        new_list.sort(key=lambda x: x[1], reverse=True )
        print(new_list)
        return new_list[0]

class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        attributes = ("speed", "endurance", "accuracy")
        total = 0 
        breakpoint()
        for i in attributes:
            total = getattr(player, i) + total 
            print(getattr(player, i))
        return total
    
    def compare_players(self, player1, player2, attribute):
        # breakpoint()
        if getattr(player1, attribute) > getattr(player2, attribute):
            return str(player1.name)
        elif getattr(player1, attribute) == getattr(player2, attribute):
             
             if getattr(player1, str(player1.strength()[0])) > getattr(player2, str(player2.strength()[0])):
                 return str(player1.name)
             elif getattr(player1, str(player1.strength()[0])) == getattr(player2, str(player2.strength()[0])):
                 if  str(self.sum_player(player1)) == str(self.sum_player(player2)):
                    return "These two players might as well be twins!"
                 elif getattr(player1, str(self.sum_player(player1))) > getattr(player2, str(self.sum_player(player2))):
                     return str(player1.name)
                 else:
                    return str(player2.name) 
             else:
                 return str(player2.name)
        else:
            return str(player2.name)




test_player = Player("dude", 0.3, 0.5, 0.2)
test_commentators = Commentator("harry")
alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)
print("test",test_commentators.compare_players(alice, bob, 'speed'))

print(test_commentators.sum_player(test_player))
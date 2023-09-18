class Homeowner:
    def __init__(self, name, address, needs):
        if isinstance(name, str):
            if len(name) > 0:
                self.name = name
            else:
                raise ValueError("enter valid name please")
        else:
            raise ValueError("enter valid name please")

        if isinstance(address, str):
            if len(address) > 0:
                self.address = address
            else:
                raise ValueError("enter valid address please")
        else:
            raise ValueError("enter valid address please")

        if isinstance(needs, list):
            self.needs = needs
        else:
            raise ValueError("please enter a list")

    def find_specialist(self, specialists_dict):
        new_list = []
        for need in self.needs:
            new_list.append(specialists_dict[need].name)
            continue

        return new_list


class Specialist:
    def __init__(self, name, price):
        if isinstance(name, str):
            if len(name) > 0:
                self.name = name
            else:
                raise ValueError("enter valid name please")
        else:
            raise ValueError("enter valid name please")

        if isinstance(price, (int, float)):
            if price > 0:
                self.price = price
            else:
                raise ValueError("enter valid price please")
        else:
            raise ValueError("enter valid price please")


class Electrician(Specialist):
    Specialist.specialty = "electrician"


class Painter(Specialist):
    Specialist.specialty = "painter"


class Plumber(Specialist):
    Specialist.specialty = "plumber"


# Homeowners
alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner(
    "Candice Candicedottir", "Candicelane 312", ["electrician", "painter"]
)

# Specialists
alice = Electrician("alice von Wonderland", 50)
bob = Painter("bob the Builder", 50)
craig = Plumber("craig smith", 50)

specialists_dict = {
    "electrician": alice,
    "painter": bob,
    "plumber": craig,
}

print("Alfred's contracts:", alfred.find_specialist(specialists_dict))
print("Bert's contracts:", bert.find_specialist(specialists_dict))
print("Candice's contracts:", candice.find_specialist(specialists_dict))

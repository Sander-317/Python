import csv
import os
from rich import print
from rich.console import Console
from rich.table import Table

# reading and writing csv file
with open("csv_rich_test/data.csv", "r") as csv_list_file:
    with open("csv_rich_test/data2.csv", "w") as new_data_file:
        csv_reader = csv.reader(csv_list_file)  # read the file
        csv_writer = csv.writer(
            new_data_file, delimiter=";"
        )  # create new file with new delimiter default is ,

        # remove the header from csv file
        # next(csv_reader)

        for row in csv_reader:  # print the row as list and print the index of list
            csv_writer.writerow(row)
            print(
                f"print the row as list: {row} print index of the row {row[0]} {row[1]}"
            )
with open("csv_rich_test/data.csv", "r") as csv_dict_file:
    with open("csv_rich_test/data3.csv", "w") as new_file:
        csv_reader = csv.DictReader(csv_dict_file)
        fieldnames = ["firstname", "lastname", "email", "age"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        for row in csv_reader:
            print(row["firstname"])
            print(row)
            csv_writer.writerow(row)


class Contact:
    def __init__(self, firstname, lastname, email, age):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age

    def add_to_list(self):
        to_add = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "age": self.age,
        }
        with open("csv_rich_test/contacts.csv", "a", newline="") as new_file:
            fieldnames = ["firstname", "lastname", "email", "age"]
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow(to_add)


# Contact("dude", "von dudenstein", "dude@gmail.com", 37).add_to_list()
print(os.path.isfile("csv_rich_test/contacts.csv"))
if os.path.isfile("csv_rich_test/contacts.csv") == False:
    with open("csv_rich_test/contacts.csv", "w", newline="") as new_file:
        fieldnames = ["firstname", "lastname", "email", "age"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()


with open("csv_rich_test/MOCK_DATA_small.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("mock data")
    for i in csv_reader:
        Contact(i["firstname"], i["lastname"], i["email"], i["age"]).add_to_list()

table = Table(title="Contacts")

table.add_column("name")
table.add_column("email")
table.add_column("age")

with open("csv_rich_test/contacts.csv", "r") as new_file:
    csv_reader = csv.DictReader(new_file)
    for i in csv_reader:
        table.add_row(i["firstname"] + " " + i["lastname"], i["email"], i["age"])
        # table.add_row(i["email"])
        # table.add_row(i["age"])

console = Console()
console.print(table)

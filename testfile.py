# print(type(3))
# print(type(3.14))
# print(type("pi"))

# text = "Lorem ipsum \\ dolor sit amet, 'consectetur' adipiscing elit. Etiam venenatis ipsum et sapien viverra aliquet. Mauris egestas porta elit, ac finibus tellus porta at. \n NEWLINE Ut tellus justo, tempor eu porttitor \t NEWTAB auctor, posuere quis eros. Donec dapibus quam fringilla, facilisis odio ut, pharetra magna. Ut mollis lorem in nisl volutpat, non."
# print(text)

# print('Hello, ' + 'world!')
# print('Jump! ' * 5)

# print('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.')
# print('Shane' in 'We went out for dinner with with Anne, Samuel and Bob.')
# print(str(5) in 'We were lucky that they had a table for 5.')
# print(5 in 'We were lucky that they had a table for 5.') #gives error

# letter_grades = 'ABCDF'
# print(letter_grades[0])
# print(letter_grades[3])
# print(letter_grades[-1])
# print(letter_grades[-2])
# print(letter_grades[-2] == letter_grades[3])

# waltz = 'onetwothree'
# print(waltz[0:3])
# print(waltz[:3])
# print(waltz[3:6])
# print(waltz[6:11])
# print(waltz[6:])
# print(waltz[0:11:2])

# sentence = 'The length of this string is:'
# print(sentence, len(sentence))
# print('Wait.. You just made it longer!')

# answer = 42
# qa = f'The answer is.. {answer}'
# print(qa)

# print(True is False)
# print(True or False)
# print(not True)
# print(not False)


# nice_weather = False
# going_outside = True if nice_weather else False
# print(going_outside)

# nice_weather_odds = .7
# party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
# print(party_location)

# party_location2 = 'inside' if 1 + 2 == 5 or 3 ** 3 == 9 else 'yard' if bool(2//5) is True else False if True else 'restaurant'
# print(party_location2)

# example_list = ['zeroth', 'first', 'second', 'third']
# # Get the zeroth item.
# print(example_list[0])

# # Get the second item.

# print(example_list[2])
# # Get a slice of the list

# print(example_list[0::2])

# example_list_a = [1, 2, 3]
# example_list_b = [3, 2, 1]
# print(example_list_a == example_list_b)

# example_list = ['this', 'is', 'fun']
# print(str(example_list))
# print(list(str(example_list)))
# print(str(list(str(example_list))))
# print(list(str(list(str(example_list)))))
# print(str(list(str(list(str(example_list))))))
# # Et cetera :-)

# a = [1, 2, 3, 4, 5]
# b = [9, 8, 7, 6, 5]
# print( set(a) & set(b))
# {5}

# names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
# print(f'Hello, {names[0]}!')
# print(f'Hello, {names[1]}!')
# print(f'Hello, {names[2]}!')
# print(f'Hello, {names[3]}!')

# names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
# for name in names:
#     print(f'Hello, {name}!')

#     question = 'How many roads must one walk down?'
# for c in question:
#     print(c)

# for i in range(10):
#     print(i)

# list(range(10))

# for i in range(900,1000, 5):
#     print(i)
# for i in range(1000,900, -5):
#     print(i)


# print('We have a long road ahead.')
# for i in range(1000):
#     print(i)
#     if i == 10:
#         break
#     print('Almost there...')
# print("That wasn't so bad after all.")

# print('We have a long road ahead.')
# for i in range(1000):
#     if i % 2 == 0:
#         print(i)
#         continue
#     print('Almost there...')
# print("That wasn't half bad.")

# example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']
# example_last_names = [n.split(' ')[-1] for n in example_names]
# print(example_last_names)

# txns = [1.09, 23.56, 57.84, 4.56, 6.78]
# TAX_RATE = .08
# def get_price_with_tax(txn):
#     return txn * (1 + TAX_RATE)
# final_prices = map(get_price_with_tax, txns)
# print('regular way', list(final_prices))

# final_prices2 = [get_price_with_tax(i) for i in txns]
# print("fancy way", final_prices2)

# # Hit control + c on your keyboard to unstuck from this :-)
# while True:
#     print('Woop woop, an infinite loop.')

# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# a = ['foo', 'bar', 'baz']
# while a:
#     print(a.pop(-1))

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('Loop ended.')

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('Loop ended.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#    print('Loop done.')

# a = ['foo', 'bar', 'baz', 'qux']
# s = 'corge'

# i = 0
# while i < len(a):
#      if a[i] == s:
#          # Processing for item found
#          break
#      i += 1
# else:
#     # Processing for item not found
#      print(s, 'not found in list.')

# for i in range(9):
#     print("Hey!")
#     print("Ho!")

# print("Start")
# for i in range(9):
#     print("Hey!")
#     print("Ho!")
# print("End")

# student_ages = {
#     'bob': 10,
#     'sharon': 9,
#     'eli': 10,
#     'preeti': 11
# }

# print(student_ages['bob'])
# print(student_ages['eli'])

# product = {
#     "name": "tofu",
#     "price": 2,
#     "producer": {
#         "name": "Tofu Company Limited",
#         "country_of_origin": "France"
#     },
# }

# print(product["producer"]["country_of_origin"])

# students = [
#     {
#         "name": "Ali",
#         "family_name": "Khan",
#         "skills": {
#             "Python": "beginner",
#             "JavaScript": "expert",
#         },
#         "certificates": [
#             {
#                 "name": "Back-end Development",
#                 "date_of_completion": "2022-01-17",
#             },
#             {
#                 "name": "Back-end Development",
#                 "date_of_completion": "2022-01-17",
#             },
#             {
#                 "name": "Data Analytics with Python",
#                 "date_of_completion": "",
#             },
#         ],
#     },
#     {
#         "name": "Jessica",
#         "family_name": "van Alphen",
#         "skills": {
#             "Python": "advanced beginner",
#             "JavaScript": "beginner",
#         },
#         "certificates": [
#             {
#                 "name": "Front-end Development",
#                 "date_of_completion": "",
#             },
#             {
#                 "name": "Back-end Development",
#                 "date_of_completion": "2022-01-17",
#             },
#             {
#                 "name": "Data Analytics with Python",
#                 "date_of_completion": "2020-01-17",
#             },
#         ],
#     },
# ]

# print(students[1]["skills"]["Python"])  # "advanced beginner"
# print(students[0]["certificates"][1]["name"])  # "Back-end Development"


# list_a = [1,2,3]
# list_b = [3,2,1]
# print(list_a == list_b)
# print(set(list_a))
# print(set(list_b))
# print(set(list_a) == set(list_b))

# set_a = set([1,2,3,6])
# set_b = set([3,4,5,6])

# # Union
# # You can read this as 'set_a or set_b', so: 'any element that is in set a or set b'
# print("union",set_a | set_b)

# # Difference
# print("difference",set_a - set_b)
# print("difference reverse",set_b - set_a)

# # Intersection
# print("intersection",set_a.intersection(set_b))

# # Checking if a set is a subset of another.
# # In other words: if the other set includes all of its own elements.
# small = set([2,3])
# big = set([1,2,3,4])

# print("is subset of another",small.issubset(big))

# # Creating a tuple
# alice = ('Alice', 5)

# # Tuples can contain any number of elements
# bob = ('Bob', 3, 9)

# # A list of tuples
# persons = [alice, bob]
# print(persons)

# a = 'foo'
# b = 42
# print(a, 3.14159, b)
# a, 3.14159, b

# input list of date strings
# inputDateList = ["06-2014", "08-2020", "4-2003", "04-2005", "10-2002", "12-2021"]


# # creating a function that accepts the input list as an argument
# def sortDates(datesList):
#     # splitting the list of elements based on the '-' separator(as the date is separated by - symbol ex 06-2014)
#     split_up = datesList.split("-")

#     # returning the year, the month of input list elements
#     # Here split_up[1] gives the year and split_up[0] gives month
#     return split_up[1], split_up[0]


# # sorting the input list of date strings using the sort() function
# # here the key is the function name
# inputDateList.sort(key=sortDates)

# # Printing the input list after sorting
# print("The input list of date strings after sorting:\n", inputDateList)

# from datetime import datetime


# def sort_dates(dates):
#     # Define a key function that converts a date string to a datetime object
#     def date_key(date_string):
#         return datetime.strptime(date_string, "%d %b %Y")

#     # Use the sorted function to sort the list of dates, using the date_key function as the key
#     return sorted(dates, key=date_key)


# # Example usage
# dates = [
#     "24 Jul 2017",
#     "25 Jul 2017",
#     "11 Jun 1996",
#     "01 Jan 2019",
#     "12 Aug 2005",
#     "01 Jan 1997",
# ]
# sorted_dates = sort_dates(dates)
# print(
#     sorted_dates
# )  # Output: ["11 Jun 1996", "01 Jan 1997", "12 Aug 2005", "24 Jul 2017", "25 Jul 2017", "01 Jan 2019"]


# live les exercise


def fahrenheit_to_celsius(number):
    return (number - 32) * 5 / 9


print(fahrenheit_to_celsius(70))

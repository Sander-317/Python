from datetime import datetime, date, time
from rich import print

# DOCS https://docs.python.org/3/library/datetime.html

today = date.today()
print("today is: ", today)
print("day: ", today.day)
print("month: ", today.month)
print("year:", today.year)

print(today.strftime("%A %dth of %B %Y "))
print(today.strftime("%a %dth of %b %y "), "test")

next_year = today.replace(year=today.year + 1)
print(next_year)

difference = abs(next_year - today)
print("only {} days until next year".format(difference.days))

nikola_tesla = date(1856, 7, 10)
nikola_tesla = date.fromisoformat("1856-07-10")

print("Nikola Tesla was born on:", nikola_tesla)
print("(monday = 0) (sunday = 6) day =", nikola_tesla.weekday())

now = datetime.now()
print("right now it's:", now)
print(
    "it's the {} minute of the {} hour, of the {} day of the {} month".format(
        now.minute,
        now.hour,
        now.day,
        now.month,
    )
)

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
print("the nuclear disaster in Chernobyl occured on:", chernobyl)
print(
    chernobyl.strftime(
        "the chernobyl disaster occured on %A %B %dth, %Y at %X MSD(%Z) "
    )
)
print("MSD is actually:", chernobyl.tzinfo)

my_time = time(15, 33, 8)
my_time2 = time.fromisoformat("15:33:08-07:00")
print(my_time)
print(my_time2)
print(my_time2.strftime("%I:%M %p"))

my_date = date(2023, 5, 4)
my_bday = datetime.combine(my_date, my_time2)
print(my_bday)

from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

# link to rich tutorial https://calmcode.io/rich/introduction.html
# to see more rich features run the main script
# python -m rich


install()
import time


custom_theme = Theme(
    {
        "good": "green",
        "bad": "red",
    }
)

console = Console(theme=custom_theme, record=True)
console.print(f"I wonder what this looks like 1 + 1 = {1+1} ")
console.print({"a": [1, 2, 3], "b": {"c": 1}})

console.print("this is some text")
console.print("this is some text", style="good")
console.print("this is some text", style="bold")
console.print("this is some text", style="bold underline")
console.print("this is some text", style="bold underline blue")
console.print("this is some text", style="bold underline red on yellow")
console.print("[bold]this [underline][bad]is[/][/] some text[/]")
console.print("no were are you save from emoji :thumbs_up:")

for i in range(10):
    console.log(f"I am about to sleep={i}")
    time.sleep(0.2)
    console.log(f"but i am briefly awake now.")


def add_two(n1, n2):
    console.log("add two numbers", log_locals=True)
    return n1 + n2


try:
    for i in range(10):
        time.sleep(0.2)
        add_two(1, i)
    # uncomment next line for awsome traceback
    # add_two(1, "a")
except:
    console.print_exception()
# creates an html or text file of the console output
# console.save_html("rich_test.html")

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import time
from datetime import datetime 
import math
from greet import supergreeting
import sys


def wait(seconds):
    time.sleep(seconds)
    print("test")

def my_sin(float):
    return math.sin(float)

def iso_now():
    now = datetime.now()
    output = now.strftime("%Y-%m-%dT%H:%M")
    return output

def platform():
    return sys.platform

def supergreeting_wrapper(name):
    return supergreeting(name)
    

if __name__ == "__main__":
    wait(1)
    my_sin(1.5)
    print(iso_now())
    print(platform())
    supergreeting_wrapper("Bob")
import sys
import os
import pyjokes
import subprocess


def main():
    bash_command = "pyjoke"
    # test =
    # os.system(bash_command)
    # print(test)
    # print("did it work")
    result = subprocess.run([bash_command], stdout=subprocess.PIPE)
    # print(result.stdout[:-2])
    test_list = []
    for i in range(5):
        joke = subprocess.run([bash_command], stdout=subprocess.PIPE)
        test_list.append(joke.stdout)

    print(test_list[0].decode("utf-8"))


if __name__ == "__main__":
    main()

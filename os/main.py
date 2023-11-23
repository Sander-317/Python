import os


print("print", os.getcwd())

if "testdir" not in os.listdir(os.getcwd()):
    os.mkdir("testdir")  # makes dir
os.makedirs(
    "testdirs/extratest/test", exist_ok="True"
)  # makes dir and checks if exists
os.mkdir(
    "deletedir",
)  # makes dir and checks if exists
os.rmdir("deletedir")  # makes dir and checks if exists

os.chdir("./testdir")
os.chdir("../")
print("print", os.getcwd())

files = os.listdir(
    "/Users/sander/Desktop/coding 2/projects/python/"
)  # list all files in dir
print(files)

# [print(i) for i in files]


current_directory = os.getcwd()
file1 = "testfile1.txt"
if file1 not in os.listdir(current_directory):
    with open(file1, "w") as new_file:
        new_file.write("python made this file nice")
        new_file.close

combined = os.path.join(current_directory, file1)  # joins paths

print("combined", combined)
print("print", os.getcwd())
print(os.path.exists(combined))  # checks if path exists
print(os.path.isfile(combined))  # checks if it's a file
print(os.path.isdir(combined))  # checks if it's a directory'
print(os.stat(combined))  # gets the stats
print(os.stat(combined).st_size)  # gets the stats

v1 = os.environ.get("PATH")
print("v1", v1)

print(os.getlogin())  # gets current user

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
from zipfile import ZipFile

def clean_cache():
    path = "/Users/sander/Desktop/coding/learning/Winc_academy_back_end/python/files/cache"
    if os.path.exists(path) == True:
        print(os.listdir(path))
        files = os.listdir(path)
        for file in files:
            # print(os.path.exists(f"{path}/{file}"))
            os.remove(f"{path}/{file}")
    else:
        os.mkdir(path)

def cache_zip(zip_file, directory):
    with ZipFile(zip_file, "r" ) as file:
        file.extractall(directory)

def cached_files():
    path = "/Users/sander/Desktop/coding/learning/Winc_academy_back_end/python/files/cache"
    files = os.listdir(path)
    files_absolute_path = []
    for file in files:
        files_absolute_path.append(f"{path}/{file}")

    print(files_absolute_path)
    return files_absolute_path

def find_password(files_list):
    target_file = []
    for file in files_list:
         with open(file, "r") as new_file:
            file_content = new_file.read()
            if "password" in file_content:
                print("found" , file)
                target_file.append(file)
                
            else:
                print("try again")


    for file in target_file:
        password = ""
        with open(file, "r") as new_file:
            file_content = new_file.read()
            index_of_password_is = file_content.index("password:")
            start = index_of_password_is + 10
            print(file_content[start:start + 28])
            password = file_content[start:start + 28]
            # print(index_of_password_is)
            # print(file_content[index_of_password_is: index_of_password_is + 10])
            # split_list = file_content.split("password:")
            # print(split_list[1].split(" ")[1])

    print(target_file)

    return password


    
    
if __name__ == "__main__":
    # clean_cache()
    # cache_zip("/Users/sander/Desktop/coding/learning/Winc_academy_back_end/python/files/data.zip", "/Users/sander/Desktop/coding/learning/Winc_academy_back_end/python/files/cache")
    # cached_files()
    find_password(cached_files())

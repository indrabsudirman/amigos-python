import os.path

#check if file exist
filename = "./data.txt"

if os.path.isfile(filename):
    # with this way you don't need to file.close() because it automatically close, done by this code 
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")
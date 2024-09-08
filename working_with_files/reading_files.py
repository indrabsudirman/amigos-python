# w writing, a appending, r reading, r+ reading/writing
file = open("./data.txt", "r")
print(file.readline())
# print(file.readline())
# for line in file:
#     print(f"Ini {line}")
file.close()
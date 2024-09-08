# w writing, a appending, r reading, r+ reading/writing
file = open("./data.txt", "r+")
file.write("Hello Indra, this is generated with Pyhton\n")
file.write("Hello Haby, this is generated with Pyhton\n")
file.close()
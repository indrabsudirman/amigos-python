person = {
    "name": "Indra Bayu Sudirman",
    "address": "Tangerang Selatan",
    "age": 100
}

for k in person:
    #print(k) #print only the key
    print(f"key is {k} and value is {person[k]}")

#other way to print dictionaries
for key, value in person.items():
    print(f"key is : {key} and value is {value}")
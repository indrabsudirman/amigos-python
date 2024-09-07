names = ["Indra", "Haby", "Lubna", "Nury", "Nenek"]

#for loop
for n in names:
    print(n)

number1 = [1, 2, 3, 4, 5, 6]
number2 = [7, 2, 3, 8, 9, 6]

result = []

#for loop
for n1 in number1:
    for n2 in number2:
        if n1 == n2 and n2 not in result:
            result.append(n2)

print(result)
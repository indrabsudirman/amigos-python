number1 = 1
number = 1

while number < 10:
    print(f"number while and break {number}")
    if number == 5:
        break
    number += 1

while number1 < 10:
    number1 += 1
    if number1 < 5:
        continue
    print(number1)

    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if n == 5:
            break
        print(f"n value is : {n}")
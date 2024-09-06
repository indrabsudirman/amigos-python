numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"numbers value is {numbers}")

del numbers[0:3]
print(f"numbers value after deleted index 0-2 is {numbers}")

numbers.pop()
print(f"numbers value after pop() is {numbers}")

print(1 in numbers)
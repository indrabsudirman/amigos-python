numbers = [1, 4, 5, 6, -1, 0]
numbers.reverse()

numbers.append(10)
print(numbers)

print(len(numbers)- 2)

print(0 in numbers)

numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
def main():
    x = [1, 2, 3, 4,  0]
    print(type(x))
    while x:
        print(x)
        print(x.pop())
    print(f"x now is {x}")
main()
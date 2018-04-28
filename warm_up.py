numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 10
numbers[-1] = 1
print(numbers[2:])
print(numbers)
count = 0
for element in numbers:
    if element == 9:
        count = count + 1
print("There are {} nine in the list".format(count))
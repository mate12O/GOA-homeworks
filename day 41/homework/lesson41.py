sum = 0
numbers = [1, 5, 40, 15, 13, 100, 76, 30, 300, 20, 15, 34]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        sum += numbers[i]
print(sum)
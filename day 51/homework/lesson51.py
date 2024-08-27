my_list = []

for i in range(10):
    my_list.append(i + 1) 

print(my_list)






even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

merged_list = even_numbers.copy()
merged_list.extend(odd_numbers)

print("Merged List:", merged_list)






my_list = [i + 1 for i in range(20)]

for element in my_list:
    print(element)







numbers = list(range(1, 21))

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)






numbers = [5, 12, 7, 9, 3, 8, 14, 11, 2, 6]

print("Sum of all elements:", sum(numbers))






numbers = [5, 12, 7, 9, 3, 8, 14, 11, 2, 6]

mean = sum(numbers) / len(numbers)

print("Arithmetic Mean:", mean)

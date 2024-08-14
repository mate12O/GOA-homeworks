def print_min_max(numbers):
    if not numbers:
        print("The list is empty")
        return

    min_num = numbers[0]
    max_num = numbers[0]
    
    for number in numbers:
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
            
    print("Minimum:", min_num)
    print("Maximum:", max_num)

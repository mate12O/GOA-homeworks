def calculator():
    num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
    operation = input("შეარჩიეთ ოპერაცია (მიმატება, გამოკლება, გამრავლება, გაყოფა): ").strip().lower()
    
    if operation == "მიმატება":
        result = num1 + num2
    elif operation == "გამოკლება":
        result = num1 - num2
    elif operation == "გამრავლება":
        result = num1 * num2
    elif operation == "გაყოფა":
        if num2 != 0:
            result = num1 / num2
        else:
            return "გაყოფა ნულით შეუძლებელია!"
    else:
        return "არასწორი ოპერაცია!"
    
    print(f"{num1} {operation} {num2} = {result}")

calculator()











def sum_of_numbers(numbers):
    return sum(numbers)

numbers_list = [1, 2, 3, 4, 5]  # მაგალითი სია
print("ჯამი:", sum_of_numbers(numbers_list))










def average_of_numbers(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

numbers_list = [1, 2, 3, 4, 5]  # მაგალითი სია
print("შედარებითი საშუალო:", average_of_numbers(numbers_list))














def check_odd_even():
    number = int(input("შეიტანეთ რიცხვი: "))
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")

check_odd_even()











def time_travel():
    current_age = int(input("შეიტანეთ თქვენი ასაკი: "))
    current_year = int(input("შეიტანეთ მიმდინარე წელი: "))
    years_to_travel = int(input("რამდენი წლით გსურთ დროში მოგზაურობა? "))
    direction = input("გსურთ წარსულში ან მომავალში მოგზაურობა? (წარსული/მომავალი): ").strip().lower()
    
    if direction == "მომავალი":
        future_year = current_year + years_to_travel
        future_age = current_age + years_to_travel
    elif direction == "წარსული":
        future_year = current_year - years_to_travel
        future_age = current_age - years_to_travel
    else:
        return "არასწორი მიმართულება!"
    
    print(f"{future_year}-ში თქვენ იქნებით {future_age} წლის")

time_travel()

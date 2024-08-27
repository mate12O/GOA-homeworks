def add_one():
    number = int(input("შეიტანეთ რიცხვი: "))
    return number + 1

print("შედეგი:", add_one())








def check_number():
    number = int(input("შეიტანეთ რიცხვი: "))
    if number > 10:
        return "მაგარია!"
    else:
        return "რიცხვი 10-ზე ნაკლებია"

print(check_number())









def min_of_two():
    num1 = int(input("შეიტანეთ პირველი ციფრი: "))
    num2 = int(input("შეიტანეთ მეორე ციფრი: "))
    return min(num1, num2)

print("უმცირესი ციფრი:", min_of_two())








def text_length():
    text = input("შეიტანეთ ტექსტი: ")
    return len(text)

print("ტექსტის სიგრძე:", text_length())







def sum_of_two_numbers():
    num1 = int(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = int(input("შეიტანეთ მეორე რიცხვი: "))
    return num1 + num2

print("ჯამი:", sum_of_two_numbers())







def positive_or_negative():
    number = int(input("შეიტანეთ რიცხვი: "))
    if number >= 0:
        return "დადებითი"
    else:
        return "უარყოფითი"

print(positive_or_negative())










def is_even():
    number = int(input("შეიტანეთ რიცხვი: "))
    return number % 2 == 0

print("ლუწია?" , is_even())










def sum_plus_five():
    num1 = int(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = int(input("შეიტანეთ მეორე რიცხვი: "))
    return num1 + num2 + 5

print("ჯამი დამატებული 5:", sum_plus_five())

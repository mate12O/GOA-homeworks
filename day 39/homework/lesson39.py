numbers = [] # ახალი ცარიელი სია

for i in range(10):
    number = int(input("შემოიტანეთ რიცხვი: "))
    numbers.append(number) # ახალი რიცხვი შევინახოთ სიაში

greater_than_100 = [] # ცარიელი სია რომელშიც ჩავამატებთ 100-ზე მეტ რიცხვებს
less_than_100 = [] # ცარიელი სია რომელშიც ჩავამატებთ 100-ზე ნაკლებ რიცხვებს

for number in numbers:
    if number > 100:
        greater_than_100.append(number)
    else:
        less_than_100.append(number)


print("100-ზე მეტი რიცხვები: ", greater_than_100)
print("100-ზე ნაკლები რიცხვები: ", less_than_100)
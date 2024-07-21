for i in range (0,21):
    print(i)

for i in range (0,10):
    print(i)

for i in range (0,100):
    if i % 2 == 0:
        print("the even is " + str(i))
    else:
        print("the odd is " + str(i))

for i in range (10):
    number = int(input("შეიყვანეთ რიცხვი: "))

sum_of_numbers = 0
for i in range(1, number + 1):
    sum_of_numbers += i

print("რიცხვების ჯამი: " + str(sum_of_numbers))
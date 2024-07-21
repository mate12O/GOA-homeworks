numbers = [1,2,3,4,5,6,7,8,9,10]
upside_down_list = []
for i in range (len(numbers)):
    upside_down_list.append(numbers[-i-1])
print(upside_down_list)
my_list = []
idx = 1
while idx < 1000:
    if idx % 2 != 0:
        my_list.append(idx ** 3)
    idx += 1


def calc(my_list):
    sum = 0
    for numbers in my_list:
        result = 0
        # print(numbers)
        while numbers != 0:
            result += numbers % 10
            numbers = numbers // 10
        # print(result)
        if result % 7 == 0:
            sum += result
            # print(sum)
    # print (result)
    print(sum)


calc(my_list)
my_new_list = []
i = 0

while i < len(my_list):
    my_new_list.append(my_list[i] + 17)
    i += 1

calc(my_new_list)

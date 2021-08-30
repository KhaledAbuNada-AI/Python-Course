def max_fun(list_num):
    largest = 0
    for i in range(0, len(list_num)):
        if list_num[i] > largest:
            largest = list_num[i]

    return largest


print(max_fun([1, 2, 3, 4]))


def max_fun(list_num):
    largest = 0
    for i in range(0, len(list_num)):
        if list_num[i] < largest:
            largest = list_num[i]

    return largest


print(max_fun([-1, 2, 3, 4]))
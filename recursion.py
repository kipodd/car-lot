nums = [12, 34, 5, 7, 8]
iter_nums = iter(nums)


# def sum_numbers(nums):
#     for n in nums:
#         n += sum_numbers(nums)
#     return n


# print(sum_numbers(iter_nums))


def sum_list(list_to_sum, index):
    if len(list_to_sum) == 0:
        return 0
    if index == 0:
        return list_to_sum[0]
    return list_to_sum[index] + sum_list(list_to_sum, index - 1)


# list_to_sum = [1, 2, 3, 4, 5]
# print(sum_list(list_to_sum, len(list_to_sum) - 1))


# def sum_string(string_of_numbers, index):
#     # index = len(string_of_numbers) - 1  # last index
#     if len(string_of_numbers) == 0:
#         return 0
#     if index == 0:
#         return int(string_of_numbers[0])
#     return int(string_of_numbers[index]) + int(sum_list(string_of_numbers, index - 1))


# my_string = "123"
# print(sum_string(my_string, len(my_string) - 1))

string = "123"


def recursive_sum_string(list, index):
    if len(list) == 0:
        return 0
    if index == 0:
        return list[0]
    return int(list[index]) + int(recursive_sum_string(list, index - 1))


# print(recursive_sum_string(string, len(string) - 1))


# def get_change(number, coins):
#     return number /


def get_change(number):
    change = [15, 10, 5, 1]
    if number == 0 or number == 1:
        print(str(number), ",")
        return number
    for i in change:
        if (number - i) > 0:
            print("," + str(i))
            return get_change(number - i)


coins = []
get_change(66)  # = 1, 5, 10, 25


66 - 25 > 25
41 - 25 > 25
66 - 10 > 10

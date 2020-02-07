import math


# region Functions for values​of continuous type


def minimum(lst):
    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value = item

    return min_value


def maximum(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item

    return max_value


def median(lst):
    sorted_list = sorted(lst)
    return sorted_list[int((len(lst) + 1) / 2) - 1]


def quartile_1(lst):
    sorted_list = sorted(lst)
    return sorted_list[int((len(lst) + 1) / 4) - 1]


def quartile_3(lst):
    sorted_list = sorted(lst)
    return sorted_list[int(3 * (len(lst) + 1) / 4) - 1]


def average(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum / len(lst)


def standard_deviation(lst):
    sum = 0
    avg = average(lst)
    for item in lst:
        sum += math.pow(item - avg, 2)
    return math.sqrt(sum / len(lst))


def count_distinct_values(lst):
    """:returns: cardinality"""
    distinct_count = 1
    n = len(lst)
    for i in range(1, n):
        if lst[i] != lst[i - 1]:
            distinct_count = distinct_count + 1
    return distinct_count

# endregion
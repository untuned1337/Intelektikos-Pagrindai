import FileOperations
import math
import Data
from Data import Data

filename = './Database/WorkingHours.csv'
data_list = FileOperations.readfile(filename)
cdata_list = FileOperations.read_continuous_data(filename)

# region Functions for values​of continuous type


def minimum():
    min_value = data_list[0]
    for item in data_list:
        if item.hours < min_value.hours:
            min_value.hours = item.hours
        if item.income < min_value.income:
            min_value.income = item.income
        if item.age < min_value.age:
            min_value.age = item.age
        if item.education < min_value.education:
            min_value.education = item.education
        if item.child5 < min_value.child5:
            min_value.child5 = item.child5
        if item.child13 < min_value.child13:
            min_value.child13 = item.child13
        if item.child17 < min_value.child17:
            min_value.child17 = item.child17
        if item.unemployed < min_value.unemployed:
            min_value.unemployed = item.unemployed
    return min_value


def maximum():
    max_value = data_list[0]
    for item in data_list:
        if item.hours > max_value.hours:
            max_value.hours = item.hours
        if item.income > max_value.income:
            max_value.income = item.income
        if item.age > max_value.age:
            max_value.age = item.age
        if item.education > max_value.education:
            max_value.education = item.education
        if item.child5 > max_value.child5:
            max_value.child5 = item.child5
        if item.child13 > max_value.child13:
            max_value.child13 = item.child13
        if item.child17 > max_value.child17:
            max_value.child17 = item.child17
        if item.unemployed > max_value.unemployed:
            max_value.unemployed = item.unemployed
    return max_value


def min2(lst):
    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value = item

    return min_value


def max2(list):
    max_value = list[0]
    for item in list:
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


print(max2(cdata_list.income_list))
print(quartile_1(cdata_list.income_list))
print(median(cdata_list.income_list))
print(quartile_3(cdata_list.income_list))
print(standard_deviation(cdata_list.income_list))
print(count_distinct_values(cdata_list.income_list))

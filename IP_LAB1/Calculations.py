import math
import Data

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
    sorted_lst = sorted(lst)
    for i in range(1, n):
        if sorted_lst[i] != sorted_lst[i - 1]:
            distinct_count = distinct_count + 1
    return distinct_count
# endregion


def most_frequent(lst, first: bool):
    dictionary = {}
    for item in lst:
        if item in dictionary.keys():
            dictionary[item] += 1
        else:
            dictionary.setdefault(item, 1)
    temp_list = sorted(dictionary, key=dictionary.get, reverse=True)
    if first:
        return temp_list[0], dictionary[temp_list[0]]
    else:
        return temp_list[1], dictionary[temp_list[1]]


def count(lst: list):
    return len(lst)


def build_dictionary(lst):
    dictionary = {}
    for item in lst:
        if item in dictionary.keys():
            dictionary[item] += 1
        else:
            dictionary.setdefault(item, 1)
    return dictionary


def remove_from_list(data_lst: list, removable_items):
    new_lst = data_lst.copy()
    for item in removable_items[:]:
        new_lst.remove(item)
    return new_lst


def remove_rows_cont(data_struct: Data.ContinuousData, removable_items, which):
    result_struct = data_struct
    for item in removable_items[:]:
        try:
            if which == 'hours':
                if item in result_struct.hours_list:
                    index = result_struct.hours_list.index(item)
                else:
                    continue
            elif which == 'unemp':
                if item in result_struct.unemployed_list:
                    index = result_struct.unemployed_list.index(item)
                else:
                    continue
            else:
                if item in result_struct.income_list:
                    index = result_struct.income_list.index(item)
                else:
                    continue

            del result_struct.hours_list[index]
            del result_struct.unemployed_list[index]
            del result_struct.income_list[index]
            del result_struct.age_list[index]
            del result_struct.child13_list[index]
            del result_struct.child17_list[index]
            del result_struct.education_list[index]
            del result_struct.child5_list[index]
            result_struct.count -= 1
        except ValueError:
            pass
    return result_struct

def normalization(data: Data.ContinuousData):
    for i in range(len(data.child5_list)):
        data.child5_list[i] =\
            (data.child5_list[i]-minimum(data.child5_list))/(maximum(data.child5_list-minimum(data.child5_list)))
    for i in range(len(data.education_list)):
        data.education_list[i] =\
            (data.education_list[i]-minimum(data.education_list))/(maximum(data.education_list-minimum(data.education_list)))
    for i in range(len(data.child17_list)):
        data.child17_list[i] =\
            (data.child17_list[i]-minimum(data.child17_list))/(maximum(data.child17_list-minimum(data.child17_list)))
    for i in range(len(data.child13_list)):
        data.child13_list[i] =\
            (data.child13_list[i]-minimum(data.child13_list))/(maximum(data.child13_list-minimum(data.child13_list)))
    for i in range(len(data.unemployed_list)):
        data.unemployed_list[i] =\
            (data.unemployed_list[i]-minimum(data.unemployed_list))/(maximum(data.unemployed_list-minimum(data.unemployed_list)))
    for i in range(len(data.age_list)):
        data.age_list[i] =\
            (data.age_list[i]-minimum(data.age_list))/(maximum(data.age_list-minimum(data.age_list)))
    for i in range(len(data.income_list)):
        data.income_list[i] =\
            (data.income_list[i]-minimum(data.income_list))/(maximum(data.income_list-minimum(data.income_list)))
    for i in range(len(data.hours_list)):
        data.hours_list[i] =\
            (data.hours_list[i]-minimum(data.hours_list))/(maximum(data.hours_list-minimum(data.hours_list)))

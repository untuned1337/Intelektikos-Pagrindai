import math
import Data
from matplotlib.cbook import boxplot_stats

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
            (data.child5_list[i]-minimum(data.child5_list))/(maximum(data.child5_list)-minimum(data.child5_list))
    for i in range(len(data.education_list)):
        data.education_list[i] =\
            (data.education_list[i]-minimum(data.education_list))/(maximum(data.education_list)-minimum(data.education_list))
    for i in range(len(data.child17_list)):
        data.child17_list[i] =\
            (data.child17_list[i]-minimum(data.child17_list))/(maximum(data.child17_list)-minimum(data.child17_list))
    for i in range(len(data.child13_list)):
        data.child13_list[i] =\
            (data.child13_list[i]-minimum(data.child13_list))/(maximum(data.child13_list)-minimum(data.child13_list))
    for i in range(len(data.unemployed_list)):
        data.unemployed_list[i] =\
            (data.unemployed_list[i]-minimum(data.unemployed_list))/(maximum(data.unemployed_list)-minimum(data.unemployed_list))
    for i in range(len(data.age_list)):
        data.age_list[i] =\
            (data.age_list[i]-minimum(data.age_list))/(maximum(data.age_list)-minimum(data.age_list))
    for i in range(len(data.income_list)):
        data.income_list[i] =\
            (data.income_list[i]-minimum(data.income_list))/(maximum(data.income_list)-minimum(data.income_list))
    for i in range(len(data.hours_list)):
        data.hours_list[i] =\
            (data.hours_list[i]-minimum(data.hours_list))/(maximum(data.hours_list-minimum(data.hours_list)))


def covariance(data1: list, data2: list):
    cov = 0
    n = len(data1)
    avg1 = average(data1)
    avg2 = average(data2)
    for i in range(n):
        cov += (data1[i]-avg1)*(data2[i]-avg2)
    return cov


def correlation(data1: list, data2: list):
    sd1 = standard_deviation(data1)
    sd2 = standard_deviation(data2)
    return covariance(data1, data2)/(sd1*sd2)


def build_corr_matrix(data: Data.ContinuousData):
    pass



def cat_to_cont(cat_data: Data.CategoricalData, cont_data: Data.ContinuousData):
    dictionary = {}
    counter = 0
    for item in cat_data.occupation_list:
        if item in dictionary.keys():
            cont_data.occupation_list.append(dictionary[item])
        else:
            dictionary.setdefault(item, counter)
            counter += 1
            cont_data.occupation_list.append(dictionary[item])
    cont_data.categorical_meanings = dictionary
    return cont_data


def covariation(data1: list, data2: list):
    sum = 0
    a_average = average(data1)
    b_average = average(data2)
    for i in range(len(data1)):
        sum += (data1[i]-a_average)*(data2[i]-b_average)
    return sum/(len(data1)-1)

def correliation(data1: list, data2: list):
    return covariation(data1, data2)/(standard_deviation(data1)*standard_deviation(data2))


def remove_outliers(all_data: Data.AllData):
    outlier_dict = {'hours': boxplot_stats(X=all_data.continuousData.hours_list)[0]["fliers"],
                    'unemp': boxplot_stats(X=all_data.continuousData.unemployed_list)[0]["fliers"],
                    'income': boxplot_stats(X=all_data.continuousData.income_list, whis=6)[0]["fliers"]}

    modified_data = remove_rows_all(all_data, outlier_dict['hours'], 'hours')
    modified_data = remove_rows_all(modified_data, outlier_dict['unemp'], 'unemp')
    modified_data = remove_rows_all(modified_data, outlier_dict['income'], 'income')

    return modified_data


def remove_rows_all(data_struct: Data.AllData, removable_items, which):
    result_struct = data_struct
    for item in removable_items[:]:
        try:
            if which == 'hours':
                if item in result_struct.continuousData.hours_list:
                    index = result_struct.continuousData.hours_list.index(item)
                else:
                    continue
            elif which == 'unemp':
                if item in result_struct.continuousData.unemployed_list:
                    index = result_struct.continuousData.unemployed_list.index(item)
                else:
                    continue
            else:
                if item in result_struct.continuousData.income_list:
                    index = result_struct.continuousData.income_list.index(item)
                else:
                    continue
            ''' Delete continuous data '''
            del result_struct.continuousData.hours_list[index]
            del result_struct.continuousData.unemployed_list[index]
            del result_struct.continuousData.income_list[index]
            del result_struct.continuousData.age_list[index]
            del result_struct.continuousData.child13_list[index]
            del result_struct.continuousData.child17_list[index]
            del result_struct.continuousData.education_list[index]
            del result_struct.continuousData.child5_list[index]
            result_struct.continuousData.count -= 1
            ''' Delete categorical data'''
            del result_struct.categoricalData.occupation_list[index]
            del result_struct.categoricalData.mortgage_list[index]
            del result_struct.categoricalData.owned_list[index]
            del result_struct.categoricalData.nonwhite_list[index]
            result_struct.categoricalData.count -= 1
        except ValueError:
            pass
    return result_struct


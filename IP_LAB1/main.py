import Reader
import math
import Data
from Data import Data

filename = './Database/WorkingHours.csv'
data_list = Reader.readfile(filename)
cdata_list = Reader.read_continuous_data(filename)

kazkas = 5;

# For values​of continuous type
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



def min2(list):
    minimum = list[0]
    for item in list:
        if(item < minimum):
            minimum = item

    return minimum

def max2(list):
    maximum = list[0]
    for item in list:
        if(item > maximum):
            maximum = item

    return maximum

def median(list):
    sorted_list = sorted(list)
    return sorted_list[int((len(list)+1)/2)-1]

def quartile_1(list):
    sorted_list = sorted(list)
    return sorted_list[int((len(list)+1)/4)-1]

def quartile_3(list):
    sorted_list = sorted(list)
    return sorted_list[int(3*(len(list) + 1) / 4) - 1]

def average(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)

def standart_deviation(list):
    sum = 0
    avg = average(list)
    for item in list:
        sum += math.pow(item-avg, 2)
    return math.sqrt(sum/len(list))

print(max2(cdata_list.income_list))
print(quartile_1(cdata_list.income_list))
print(median(cdata_list.income_list))
print(quartile_3(cdata_list.income_list))
print(standart_deviation(cdata_list.income_list))
#print(max(cdata_list.hours_list, key=int))
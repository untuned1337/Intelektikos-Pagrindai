import Reader
import Data
from Data import Data

filename = './Database/WorkingHours.csv'
data_list = Reader.readfile(filename)


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

print('reiksmiu sk : ', len(data_list))
print(minimum().age)
print(maximum().age)





import csv
import Data
from Data import Data
from Data import ContinuousData
from Data import CategoricalData
import Calculations
from Calculations import *


def read_continuous_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        fail_count = 0
        data_list = [[], [], [], [], [], [], [], []]
        test_list = [[], [], [], [], [], [], [], []]
        for row in csv_reader:
            if line_count != 0:
                fail_count = 0
                try:
                    data_list[0].append(int(row[1]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[1].append(int(row[2]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[2].append(int(row[3]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[3].append(int(row[4]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[4].append(int(row[5]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[5].append(int(row[6]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[6].append(int(row[7]))
                except ValueError:
                    fail_count += 1
                try:
                    data_list[7].append(int(row[12]))
                except ValueError:
                    fail_count += 1
                if fail_count == 0:
                    test_list[0].append(int(row[1]))
                    test_list[1].append(int(row[2]))
                    test_list[2].append(int(row[3]))
                    test_list[3].append(int(row[4]))
                    test_list[4].append(int(row[5]))
                    test_list[5].append(int(row[6]))
                    test_list[6].append(int(row[7]))
                    test_list[7].append(int(row[12]))
            line_count = line_count + 1
    cdata_list = ContinuousData(line_count-1, *data_list)
    tdata_list = ContinuousData(len(test_list[0]), *test_list)
    return cdata_list, tdata_list


def read_categorical_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        data_list = [[], [], [], []]
        for row in csv_reader:
            if line_count != 0:
                try:
                    data_list[0].append(int(row[8]))
                except ValueError:
                    pass
                try:
                    data_list[1].append(int(row[9]))
                except ValueError:
                    pass
                try:
                    data_list[2].append(int(row[10]))
                except ValueError:
                    pass
                try:
                    if row[11] != '':
                        data_list[3].append(row[11])
                except ValueError:
                    pass
            line_count = line_count + 1
        cdata_list = CategoricalData(line_count-1, *data_list)
        return cdata_list


def write_continuous_data(lst: ContinuousData, filename):
    with open(filename, mode='w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        hours = lst.hours_list
        incomes = lst.income_list
        ages = lst.age_list
        educations = lst.education_list
        child5s = lst.child5_list
        child13s = lst.child13_list
        child17s = lst.child17_list
        unemployed = lst.unemployed_list

        writer.writerow(['Atributo pavadinimas', 'Kiekis', 'Trukstamos reiksmes', 'Kardinalumas', 'Minimali reiksme',
                      'Maksimali reiksme', '1-asis kvartilis', '3-asis kvartilis', 'Vidurkis', 'Mediana',
                      'Standartinis nuokrypis'])
        writer.writerow(['Hours', len(hours), lst.count-len(hours), count_distinct_values(hours), minimum(hours),
                         maximum(hours), quartile_1(hours), quartile_3(hours), average(hours), median(hours),
                         standard_deviation(hours)])
        writer.writerow(['Income', len(incomes), lst.count-len(incomes), count_distinct_values(incomes),
                         minimum(incomes), maximum(incomes), quartile_1(incomes), quartile_3(incomes), average(incomes),
                         median(incomes), standard_deviation(incomes)])
        writer.writerow(['Age', len(ages), lst.count-len(ages), count_distinct_values(ages), minimum(ages),
                         maximum(ages), quartile_1(ages), quartile_3(ages), average(ages), median(ages),
                         standard_deviation(ages)])
        writer.writerow(['Education', len(educations), lst.count-len(educations), count_distinct_values(educations),
                         minimum(educations), maximum(educations), quartile_1(educations), quartile_3(educations),
                         average(educations), median(educations), standard_deviation(educations)])
        writer.writerow(['Child5', len(child5s), lst.count-len(child5s), count_distinct_values(child5s),
                         minimum(child5s), maximum(child5s), quartile_1(child5s), quartile_3(child5s), average(child5s),
                         median(child5s), standard_deviation(child5s)])
        writer.writerow(['Child13', len(child13s), lst.count-len(child13s), count_distinct_values(child13s),
                         minimum(child13s), maximum(child13s), quartile_1(child13s), quartile_3(child13s),
                         average(child13s), median(child13s), standard_deviation(child13s)])
        writer.writerow(['Child17', len(child17s), lst.count-len(child17s), count_distinct_values(child17s),
                         minimum(child17s), maximum(child17s), quartile_1(child17s), quartile_3(child17s),
                         average(child17s), median(child17s), standard_deviation(child17s)])
        writer.writerow(['Unemployed', len(unemployed), lst.count-len(unemployed), count_distinct_values(unemployed),
                         minimum(unemployed), maximum(unemployed), quartile_1(unemployed), quartile_3(unemployed),
                         average(unemployed), median(unemployed), standard_deviation(unemployed)])
        csv_file.close()


def write_categorical_data(lst: CategoricalData, filename):
    with open(filename, mode='w', newline='', encoding="utf-8") as csv_file:
        fieldnames = ['Atributo pavadinimas', 'Kiekis', 'Trukstamos reiksmes', 'Kardinalumas', 'Minimali reiksme',
                      'Maksimali reiksme', '1-asis kvartilis', '3-asis kvartilis', 'Vidurkis', 'Mediana',
                      'Standartinis nuokrypis']
        writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        nonwhites = lst.nonwhite_list
        owned_list = lst.owned_list
        mortgage_list = lst.mortgage_list
        occupations = lst.occupation_list

        writer.writerow(['Atributo pavadinimas', 'Kiekis', 'Trukstamos reiksmes', 'Kardinalumas', 'Moda',
                      'Modos daznumas', 'Moda, %', '2-oji Moda', '2-osios Modos daznumas', '2-oj Moda, %'])

        writer.writerow(['Non-White', len(nonwhites), lst.count-len(nonwhites), count_distinct_values(nonwhites),
                         most_frequent(nonwhites, True)[0], most_frequent(nonwhites, True)[1],
                         (100*most_frequent(nonwhites, True)[1])/len(nonwhites), most_frequent(nonwhites, False)[0],
                         most_frequent(nonwhites, False)[1], (100*most_frequent(nonwhites, False)[1])/len(nonwhites)])

        writer.writerow(['Owned', len(owned_list), lst.count-len(owned_list), count_distinct_values(owned_list),
                         most_frequent(owned_list, True)[0], most_frequent(owned_list, True)[1],
                         (100 * most_frequent(owned_list, True)[1]) / len(owned_list),
                         most_frequent(owned_list, False)[0], most_frequent(owned_list, False)[1],
                         (100 * most_frequent(owned_list, False)[1]) / len(owned_list)])

        writer.writerow(['Mortgage', len(mortgage_list), lst.count-len(mortgage_list), count_distinct_values(mortgage_list),
                         most_frequent(mortgage_list, True)[0], most_frequent(mortgage_list, True)[1],
                         (100 * most_frequent(mortgage_list, True)[1]) / len(mortgage_list),
                         most_frequent(mortgage_list, False)[0], most_frequent(mortgage_list, False)[1],
                         (100 * most_frequent(mortgage_list, False)[1]) / len(mortgage_list)])

        writer.writerow(['Occupation', len(occupations), lst.count-len(occupations), count_distinct_values(occupations),
                         most_frequent(occupations, True)[0], most_frequent(occupations, True)[1],
                         (100 * most_frequent(occupations, True)[1]) / len(occupations),
                         most_frequent(occupations, False)[0], most_frequent(occupations, False)[1],
                         (100 * most_frequent(occupations, False)[1]) / len(occupations)])
        csv_file.close()

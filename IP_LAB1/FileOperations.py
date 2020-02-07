import csv
import Data
from Data import Data
from Data import ContinuousData

def readfile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        data_list = []
        for row in csv_reader:
            if line_count != 0:
                data = Data(*row)
                data_list.append(data)
            line_count = line_count + 1

    return data_list


def read_continuous_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        data_list = [[], [], [], [], [], [], [], []]
        for row in csv_reader:
            if line_count != 0:
                data_list[0].append(int(row[1]))
                data_list[1].append(int(row[2]))
                data_list[2].append(int(row[3]))
                data_list[3].append(int(row[4]))
                data_list[4].append(int(row[5]))
                data_list[5].append(int(row[6]))
                data_list[6].append(int(row[7]))
                data_list[7].append(int(row[12]))
            line_count = line_count + 1
    cdata_list = ContinuousData(*data_list)
    return cdata_list
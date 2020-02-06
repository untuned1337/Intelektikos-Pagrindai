import csv


def readfile(filename):
    import main
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        data_list = []
        for row in csv_reader:
            if line_count != 0:
                data = main.Data(*row)
                data_list.append(data)
            line_count = line_count + 1

    return data_list

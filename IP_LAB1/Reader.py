import csv
import main

def readFile(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count!=0:
                print(row[0])
            line_count = line_count + 1

        print(line_count)

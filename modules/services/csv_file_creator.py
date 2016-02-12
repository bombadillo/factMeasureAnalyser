import os
import json
from modules.common.config import Config
import modules.services.column_file_loader as column_file_loader
import modules.services.count_file_loader as count_file_loader

columns = []

def create():
    global columns
    filePath = "{0}{1}".format(Config.csv_file_directory, Config.csv_file_name)
    if os.path.exists(filePath):
        os.remove(filePath)
    columns = column_file_loader.load()
    columns += '\n'
    write_columns()
    parse_counts()

def write_columns():
    global columns
    writeToFile(columns)

def parse_counts():
    global columns
    parsedColumns = columns.replace('\n', '')
    measures = json.loads(count_file_loader.load())
    sorted_list = {}
    for measure in measures:
        split = measure.split('-')
        name = split[0]
        time_code = split[1]
        value = measures[measure]
        column_split = parsedColumns.split(',')
        del column_split[0]
        if time_code not in sorted_list:
            sorted_list[time_code] = [None] * len(column_split)
        column_index = column_split.index(name)
        print 'setting sorted_list[{0}][{1}] to {2}'.format(time_code, column_index, value)
        sorted_list[time_code][column_index] = value
    write_counts(sorted_list)

def write_counts(sorted_list):
    csv_string = ''
    for i in sorted_list:
        csv_string += "{0},".format(i)
        for count in sorted_list[i]:
            csv_string += "{0},".format(count)
        csv_string = csv_string[:-1]
        csv_string += '\n'

    writeToFile(csv_string)

def writeToFile(string):
    filePath = "{0}{1}".format(Config.csv_file_directory, Config.csv_file_name)
    f = open(filePath,'a')
    f.write(string)
    f.close()

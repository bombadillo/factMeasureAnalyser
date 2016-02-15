import os
import json
from modules.common.config import Config
import modules.services.column_file_loader as column_file_loader
import modules.services.count_file_loader as count_file_loader

COLUMNS = ''

def create():
    global COLUMNS
    file_path = "{0}{1}".format(Config.csv_file_directory, Config.csv_file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    COLUMNS = column_file_loader.load()
    COLUMNS += '\n'
    write_columns()
    parse_counts()

def write_columns():
    write_to_file(COLUMNS)

def parse_counts():
    parsed_columns = COLUMNS.replace('\n', '')
    measures = json.loads(count_file_loader.load())
    sorted_list = {}
    for measure in measures:
        split = measure.split('-')
        name = split[0]
        time_code = split[1]
        value = measures[measure]
        column_split = parsed_columns.split(',')
        del column_split[0]
        if time_code not in sorted_list:
            sorted_list[time_code] = [None] * len(column_split)
        column_index = column_split.index(name)
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

    write_to_file(csv_string)

def write_to_file(string):
    file_path = "{0}{1}".format(Config.csv_file_directory, Config.csv_file_name)
    file_writer = open(file_path,'a')
    file_writer.write(string)
    file_writer.close()

import modules.services.column_file_loader as column_file_loader
from modules.common.config import Config

def update(column):
    columns = column_file_loader.load()
    if column not in columns:
        columns = "{0},{1}".format(columns, column)
        filePath = "{0}{1}".format(Config.temp_file_directory, Config.temp_column_file_name)
        f = open(filePath,'w')
        f.write(columns)
        f.close()

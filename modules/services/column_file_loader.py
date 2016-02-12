from modules.common.config import Config

def load():
    filePath = "{0}{1}".format(Config.temp_file_directory, Config.temp_column_file_name)
    with open(filePath, 'r') as f:
        return f.readline()

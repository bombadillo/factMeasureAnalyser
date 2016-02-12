import os
import shutil
from modules.common.config import Config

def create_files():
    directory = Config.temp_file_directory
    if not os.path.exists(directory):
        os.makedirs(directory)
    open("{0}{1}".format(directory, Config.temp_count_file_name), 'a')
    open("{0}{1}".format(directory, Config.temp_column_file_name), 'a')

def delete_files():
    directory = Config.temp_file_directory
    shutil.rmtree(directory)

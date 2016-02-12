import json
from modules.common.config import Config
import modules.services.count_file_loader as count_file_loader

def update(measure_list):
    measures_count = count_file_loader.load()
    if measures_count:
        print 'update count'
        measures_count = json.loads(measures_count)
        for measure in measure_list:
            if measure not in measures_count:
                measures_count[measure] = measure_list[measure]
            else:
                measures_count[measure] += measure_list[measure]
        measure_list = measures_count
    filePath = "{0}{1}".format(Config.temp_file_directory, Config.temp_count_file_name)
    f = open(filePath,'w')
    f.write(json.dumps(measure_list))
    f.close()

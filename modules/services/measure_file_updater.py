import modules.services.column_file_updater as column_file_updater
import modules.services.count_file_updater as count_file_updater

def update(fact_measure_list):
    measure_list_summed = {}
    for measure in fact_measure_list:
        column_file_updater.update(measure['name'])
        key = "{0}-{1}".format(measure['name'], measure['timeCode'])
        if key not in measure_list_summed:
            measure_list_summed[key] = measure['value']
        else:
            measure_list_summed[key] += measure['value']

    count_file_updater.update(measure_list_summed)

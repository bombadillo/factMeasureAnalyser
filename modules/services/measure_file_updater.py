import modules.services.column_file_updater as column_file_updater
import modules.services.count_file_updater as count_file_updater

measure_names_encountered = ''

def update(chunk):
    global measure_names_encountered
    measure_list_summed = {}
    for measure in chunk.itertuples():
        name = measure[4]
        value = measure[5]
        if name not in measure_names_encountered:
            measure_names_encountered += name
            column_file_updater.update(name)
        key = name + '-' + str(measure[3])
        try:
            measure_list_summed[key] += value
        except KeyError:
            measure_list_summed[key] = value
    count_file_updater.update(measure_list_summed)

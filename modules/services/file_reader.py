import pandas as panda
import modules.services.measure_file_updater as measure_file_updater

fact_measure_list = []

def parse(file):
    print 'parsing file {0}'.format(file)

    chunksize = 10 ** 6
    for chunk in panda.read_csv(file, sep='|', chunksize=chunksize):
        chunk.columns = ['measureCode', 'locationCode', 'timeCode', 'name', 'value']
        for row in chunk.iterrows():
            process_line(row[1])
        call_measure_updater()

def process_line(line):
    global max_line_read
    global fact_measure_list
    global lines_iterated
    fact_measure_list.append(line)

def call_measure_updater():
    global fact_measure_list
    print 'processing'
    measure_file_updater.update(fact_measure_list)
    fact_measure_list = []

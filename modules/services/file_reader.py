import pandas as panda
import modules.services.measure_file_updater as measure_file_updater

def parse(file):
    chunksize = 10 ** 6
    for chunk in panda.read_csv(file, sep='|', chunksize=chunksize):
        chunk.columns = ['measureCode', 'locationCode', 'timeCode', 'name', 'value']
        call_measure_updater(chunk)

def call_measure_updater(chunk):
    measure_file_updater.update(chunk)

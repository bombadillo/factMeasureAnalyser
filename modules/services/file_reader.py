import modules.services.line_parser as line_parser
import modules.services.measure_file_updater as measure_file_updater

max_line_read = 4
fact_measure_list = []
lines_iterated = 0

def parse(file):
    print 'parsing file {0}'.format(file)
    with open(file, 'r') as f:
        for line in f:
            process_line(line)

def process_line(line):
    global max_line_read
    global fact_measure_list
    global lines_iterated
    lines_iterated += 1
    print 'lines iterated {0}'.format(lines_iterated)
    fact_measure_list.append(line_parser.parse(line))
    if lines_iterated % max_line_read == 0:
        measure_file_updater.update(fact_measure_list)
        fact_measure_list = []

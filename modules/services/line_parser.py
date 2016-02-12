def parse(line):
    line = line.replace('\n', '')
    line_split = line.split('|')
    fact_measure = {'name': line_split[2], 'timeCode': line_split[3],'value': float(line_split[4]) }
    return fact_measure

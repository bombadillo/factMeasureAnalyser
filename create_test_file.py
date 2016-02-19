import random, string, calendar, time, sys
from time import gmtime, strftime

rows_to_create = 20000
per_iteration = 500
timestamp = calendar.timegm(time.gmtime())
output_file_path = './test_measures_{0}.txt'.format(timestamp)
argument = sys.argv[1]

def start():
    iteration = iter(xrange (0,rows_to_create))
    string_to_write = ''
    for i in iteration:
        random_fact = get_random_fact()
        random_number = random.randint(0, 20)
        if random_number == 6 and argument == 'dups':
            string_to_write += random_fact
        string_to_write += random_fact
        if i % per_iteration == 0:
            write_to_file(string_to_write)
            string_to_write = ''

def get_random_fact():
    product_code = random_product_code()
    location_code = 'Company'
    week_number = random_week_number()
    measure_name = random_measure_name()
    value = random_value(measure_name)
    fact_measure = '{0}|{1}|{2}|{3}|{4}{5}'.format(product_code, location_code,
                                                week_number, measure_name,
                                                value, '\n')
    return fact_measure

def random_product_code():
   return random.randint(1000000000000, 9000000000000)

def random_week_number():
    return random.randint(2013,2015)

def random_measure_name():
    measures_list = ['Sls_R_Act', 'Sls_U_Act', 'Sls_C_Act', 'Sls_V_Act',
                     'Rtn_R_Act', 'Rtn_U_Act', 'Rtn_C_Act', 'Rtn_V_Act'
                    ]
    random_index = random.randint(0, len(measures_list) - 1)
    return measures_list[random_index]

def random_value(measure_name):
    if '_C_' in measure_name:
        return random.randint(1,12)
    else:
        return round(random.uniform(0.99, 40), 2)

def write_to_file(fact_measure):
    global output_file_path
    f = open(output_file_path,'a')
    f.write(fact_measure)
    f.close()

print strftime("%Y-%m-%d %H:%M:%S", gmtime())
start()
print strftime("%Y-%m-%d %H:%M:%S", gmtime())

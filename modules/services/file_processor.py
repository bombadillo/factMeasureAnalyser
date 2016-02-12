import modules.services.file_reader as file_reader

def process(files):
    print 'processing files'
    for file in files:
        print "processing file {0}".format(file)
        file_reader.parse(file)

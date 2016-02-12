import modules.services.temp_file_handler as temp_file_handler
import modules.services.files_to_process_retriever as files_to_process_retriever
import modules.services.file_processor as file_processor
import modules.services.csv_file_creator as csv_file_creator

def start(arguments):
    temp_file_handler.create_files()
    files_to_process = files_to_process_retriever.retrieve(arguments[1])
    file_processor.process(files_to_process)
    csv_file_creator.create()
    temp_file_handler.delete_files()

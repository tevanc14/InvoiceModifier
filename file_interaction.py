import os

input_file_directory = 'input_file/'
output_file_directory = 'output_file/'
output_name_tag = ' - invoices'


def get_input_file():
    files = os.listdir(input_file_directory)
    if len(files) > 1 or len(files) == 0:
        print(
            'There must be one and only one file in the "input_file" directory'
        )
        exit(1)
    else:
        return files[0]


def get_output_file_name(input_file_name):
    input_file_name_without_extension = os.path.splitext(input_file_name)[0]
    input_file_extension = os.path.splitext(input_file_name)[1]
    return input_file_name_without_extension + output_name_tag + input_file_extension

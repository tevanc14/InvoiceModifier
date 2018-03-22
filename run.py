import pandas as pd

from edit import perform_edits
from file_interaction import *


def modify_file():
    input_file_name = get_input_file()
    file_to_edit = pd.read_excel(
        os.path.join(input_file_directory, input_file_name))
    output = perform_edits(file_to_edit)
    output_file_name = get_output_file_name(input_file_name)
    output.to_excel(
        os.path.join(output_file_directory, output_file_name), index=False)


if __name__ == "__main__":
    modify_file()

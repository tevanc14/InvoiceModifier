# Invoice Modifier
A set of python modules to take in an excel file, make desired modifications,
and return a modified excel file.

### Current modifications

> * Remove any line items that do not include either an amount or a
    sales price
> * Split a name cell by a hyphen surrounded by two spaces and keep
    only the first token

### Usage

> * Install requirements by executing `pip install -r requirements.txt`
> * Place the (strictly one) file to be modified in the `input_file` directory
> * Run the project by executing `python run.py`
> * Retrieve the modified file from the `output_file` directory
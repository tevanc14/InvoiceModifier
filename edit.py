import pandas as pd

from header_enum import Headers
from validation import is_valid_nonzero


def perform_edits(input_file):
    trimmed = remove_zero_amounts(input_file)
    return remove_extra_name(trimmed)


def remove_zero_amounts(df):
    df1 = pd.DataFrame(data=None, columns=df.columns, index=None)

    for _, row in df.iterrows():
        if is_valid_nonzero(row[Headers.amount.value]) or is_valid_nonzero(
                row[Headers.sales_price.value]):
            df1 = df1.append(row)

    return df1


def remove_extra_name(df):
    delimiter = ' - '
    df1 = pd.DataFrame(data=None, columns=df.columns, index=None)

    for _, row in df.iterrows():
        row.at[Headers.name.value] = row[Headers.name.value].split(delimiter)[
            0]
        df1 = df1.append(row)

    return df1

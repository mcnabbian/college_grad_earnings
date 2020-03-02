# take in a pandas dataframe and list of columns, iterate through list of columns, edit, return dataframe
import pandas as pd


def format_pd(frame, columns):
    """formats objects into floats and returns df"""
    for col in columns:
        frame[col] = frame[col].astype(str)  # cast as string

        # remove non-numeric characters
        frame[col] = frame[col].str.replace(',', '')
        frame[col] = frame[col].str.replace('$', '')

        frame[col] = frame[col].astype(float).round(decimals=0)  # cast back to float

    return frame

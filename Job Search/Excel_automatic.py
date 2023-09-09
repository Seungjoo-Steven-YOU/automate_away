import os
import pandas as pd
from openpyxl import load_workbook
### Everytime cv_letter.py runs, automatically insert the tedious data into
### the excelsheet.


def new_line(name: str, pos: str, date, loc: str, site: str) \
        -> None:
    """Append a new line at the end of an excel file. The line should include
    organization name, position name, the date, and the location."""
    os.chdir(r'D:\Resume')
    result = [name, pos, date, loc, None, None, site]
    wb = load_workbook("Job-O-Matic.xlsm", read_only=False, keep_vba=True)
    # Select First Worksheet
    ws = wb.worksheets[2]
    # Append new relevant data
    ws.append(result)
    wb.save("Job-O-Matic.xlsm")
    wb.close()

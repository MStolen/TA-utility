"""Helper functions for 3201_utility.py"""
import pathlib
import warnings
import pandas as pd
import math


def fix_column_width(writer: pd.ExcelWriter, sheet_name: str, df: pd.DataFrame, max_last=False) -> None:
    """
Change The width of all columns in an excel sheet to fit the text contained inside.
    :param writer: The excel file writer which has already written the sheet
    :param sheet_name: The name of the sheet to adjust
    :param df: The data frame where sheet was written from
    :param max_last: Whether or not to maximize last width
    """
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]  # pull worksheet object
    total_width = 0
    max_width = 114.33
    idx = 0
    max_len = 0
    cell_format = workbook.add_format({'border': 1})
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
        )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, max_len, cell_format)  # set column width
        total_width += max_len
    if max_last:
        # set width to all fit on one page. 0.65 * idx is the error per column
        worksheet.set_column(idx, idx, max_width - (total_width - max_len) - 0.65 * idx, cell_format)


def max_row_height(writer: pd.ExcelWriter, sheet_name: str, df: pd.DataFrame) -> None:
    """
Make rows as tall as possible while remaining on a single page. Skips first row.
    :param writer: The excel file writer which has already written the sheet
    :param sheet_name: The name of the sheet to adjust
    :param df: The data frame where sheet was written from
    :return:
    """
    worksheet = writer.sheets[sheet_name]
    total_height = 537
    num_rows = df.shape[0]
    row_height = math.floor((total_height - 15)/num_rows)
    for idx in range(1, num_rows + 1):
        worksheet.set_row(row=idx, height=row_height)


def set_landscape(writer: pd.ExcelWriter, sheet_name: str) -> None:
    """
Set a worksheet to landscape
    :param writer: The excel writer to operate on
    :param sheet_name: The name of the sheet to adjust
    :return:
    """
    worksheet = writer.sheets[sheet_name]
    worksheet.set_landscape()


def get_sorted_csv_or_xls(folder_location: pathlib.Path,
                          check_xlsx: bool = False) -> list:
    """
Get the CSV and XLS files in the folder and return sorted file list
    :param folder_location: Location of folder to sort list of CSV and XLS files inside of
    :param check_xlsx: Bool to check for XLSX as well
    :return: Sorted list of files (by file name, not by type)
    """
    file_list = list(folder_location.glob("*.csv")) + list(folder_location.glob("*.xls"))
    if check_xlsx:
        file_list = file_list + list(folder_location.glob("*.xls"))
    if not file_list:
        raise RuntimeError("Expected files with extension '.csv' or '.xls' in location '{0}/'"
                           .format(str(folder_location)))
    file_list.sort()
    return file_list


def read_csv_or_xls(file_location: pathlib.Path) -> pd.DataFrame:
    """
Get CSV or XLS file and return contents as data frame.
    :param file_location: The path to the file to be read
    :return: Dataframe containing contents of the input file
    """
    if (file_location.suffix == '.xls') | (file_location.suffix == '.xlsx'):
        return pd.read_excel(file_location)
    else:
        return pd.read_csv(file_location)


def make_name_sheets(section_list_location: pathlib.Path,
                     output_file: pathlib.Path,
                     column_headers: list,
                     first_name: str,
                     last_name: str
                     ) -> int:
    """
Make an Excel file with a single sheet for each section in the list with name columns as well as the input columns
    :param section_list_location: The location of the files containing section information
    :param output_file: The path to the output file
    :param column_headers: The headers of the columns to include on the sheet
    :param first_name: The name of the column header for first names in the files
    :param last_name: The name of the column header for last names in the files
    :return: 0 for success, otherwise an error.
    """
    section_list = get_sorted_csv_or_xls(section_list_location)

    # Check for incorrect output file extension
    if output_file.suffix != '.xlsx':
        warnings.warn(
            f"The output extension should be '.xlsx', instead of '{output_file.suffix}'. This may cause an error.")

    # Write all first and last names to a sheet per section (sections are defined by individual input files)
    writer = pd.ExcelWriter(output_file)
    for file in section_list:
        if file.suffix == '.xls':
            section_data = pd.read_excel(file)
        else:
            section_data = pd.read_csv(file)
        # determine which columns are needed for name and remove the remainder
        columns_keep = (section_data.columns == last_name) | (section_data.columns == first_name)
        section_data.drop(columns=section_data.columns[~columns_keep], inplace=True)
        empty_column = [None] * section_data.shape[0]

        # add custom columns and write them out
        for header in column_headers:
            section_data[header] = empty_column
        section_data.to_excel(writer, sheet_name=file.stem, index=False)
        fix_column_width(writer=writer, sheet_name=file.stem, df=section_data, max_last=True)
        max_row_height(writer=writer, sheet_name=file.stem, df=section_data)
        set_landscape(writer=writer, sheet_name=file.stem)
    writer.save()

    return 0


if __name__ == '__main__':
    print("This file only contains helper functions for the 3201 utility. Run '3201_utility' to use this utility!")
    exit(0)

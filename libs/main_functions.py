"""The main functions for the utility"""
# Built-in libraries
import pathlib

# External libraries
import pandas as pd

# Internal helper functions
from libs.helper_functions import fix_column_width, get_sorted_csv_or_xls, read_csv_or_xls, make_name_sheets


def create_sign_in_sheets(section_list_location: pathlib.Path,
                          sign_in_file: pathlib.Path,
                          first_name: str,
                          last_name: str
                          ) -> int:
    """
Import students names from section and create sign-in sheet
    :param section_list_location: Folder containing class sections
    :param sign_in_file: File to output all sign-in sheets to (XLSX format)
    :param first_name: The first name column header
    :param last_name: The last name column header
    :return: 0 for success and other for failure
    """
    # section_list = get_sorted_csv_or_xls(section_list_location)
    #
    # # Check for incorrect output file extension
    # if sign_in_file.suffix != '.xlsx':
    #     warnings.warn(
    #         f"The output extension should be '.xlsx', instead of '{sign_in_file.suffix}'. This may cause an error.")
    #
    # # Write all first and last names to a sheet per section (sections are defined by individual input files)
    # writer = pd.ExcelWriter(sign_in_file)
    # for file in section_list:
    #     if file.suffix == '.xls':
    #         section_data = pd.read_excel(file)
    #     else:
    #         section_data = pd.read_csv(file)
    #     # determine which columns are needed for name and remove the remainder
    #     columns_keep = (section_data.columns == last_name) | (section_data.columns == first_name)
    #     section_data.drop(columns=section_data.columns[~columns_keep], inplace=True)
    #     empty_column = [None] * section_data.shape[0]
    #     section_data['Time In'] = empty_column
    #     section_data['Time Out'] = empty_column
    #     section_data['Signature'] = empty_column
    #     section_data['Finished'] = empty_column
    #     section_data.to_excel(writer, sheet_name=file.stem, index=False)
    # writer.save()
    # return 0
    return make_name_sheets(section_list_location=section_list_location,
                            output_file=sign_in_file,
                            column_headers=['Time In', 'Time Out', 'Signature', 'Finished'],
                            first_name=first_name,
                            last_name=last_name,
                            )


def make_checkoffs(section_list_location: pathlib.Path,
                   checkoff_file: pathlib.Path,
                   checkoff_list_file: pathlib.Path,
                   checkoff_header: str,
                   first_name: str,
                   last_name: str
                   ) -> int:
    """
Import students names from section and create checkoff sheet
    :param section_list_location: Folder containing class sections
    :param checkoff_file: File to output all check off sheets to (XLSX format)
    :param checkoff_list_file: A csv or xls or xlsx file that contains a list of checkoff points to use
    :param checkoff_header: The name of the column header to use if more than one list is in the file
    :param first_name: The first name column header
    :param last_name: The last name column header
    :return: 0 for success and other for failure
    """

    # section_list = get_sorted_csv_or_xls(section_list_location)
    #
    # # Check for incorrect output file extension
    # if checkoff_file.suffix != '.xlsx':
    #     warnings.warn(
    #         f"The output extension should be '.xlsx', instead of '{checkoff_file.suffix}'. This may cause an error.")
    #
    # # Write all first and last names to a sheet per section (sections are defined by individual input files)
    # writer = pd.ExcelWriter(checkoff_file)
    # for file in section_list:
    #     if file.suffix == '.xls':
    #         section_data = pd.read_excel(file)
    #     else:
    #         section_data = pd.read_csv(file)
    #     # determine which columns are needed for name and remove the remainder
    #     columns_keep = (section_data.columns == last_name) | (section_data.columns == first_name)
    #     section_data.drop(columns=section_data.columns[~columns_keep], inplace=True)
    #     empty_column = [None] * section_data.shape[0]
    #     section_data['Four-Bit Counter'] = empty_column
    #     section_data['Two-Digit Joystick'] = empty_column
    #     section_data['Grade'] = empty_column
    #     section_data['Notes'] = empty_column
    #     section_data.to_excel(writer, sheet_name=file.stem, index=False)
    # writer.save()
    # return 0

    # Get list of checkoffs to have a column for
    checkoff_table = read_csv_or_xls(checkoff_list_file)
    if checkoff_header:
        checkoff_list = list(checkoff_table[checkoff_header].dropna())
    else:
        checkoff_list = list(checkoff_table[checkoff_table.columns[0]].dropna())

    # Add static grade and notes columns
    checkoff_list.append('Grade')
    checkoff_list.append('Notes')
    return make_name_sheets(section_list_location=section_list_location,
                            output_file=checkoff_file,
                            column_headers=checkoff_list,
                            first_name=first_name,
                            last_name=last_name)


def check_pre_labs(section_list_location: pathlib.Path,
                   file_suffix: str,
                   prelab_location: pathlib.Path,
                   output_location: pathlib.Path,
                   assignment_index: int,
                   first_name: str,
                   last_name: str
                   ) -> int:
    """
Write a report to determine which students have not completed an assignment. This function is designed to check pre-labs
    :param section_list_location: Folder where lab section lists are stored
    :param file_suffix: Output file suffix to be added to input (default: _Report). Output file is always .xlsx file.
    :param prelab_location: Location where pre-lab assignment file is located
    :param assignment_index: Column index where assignment grades/submissions are stored (column H/7 usually)
    :param output_location: Location to save output file(s)
    :param first_name: The first name column header
    :param last_name: The last name column header
    :return: 0 for success and other for failure
    """
    # Get the list of section files and class files
    # The section files contain students in each section
    # The class files are the assignment files from grade center
    section_list = get_sorted_csv_or_xls(section_list_location)
    lab_list = get_sorted_csv_or_xls(prelab_location)

    # Check for wrong output extension (unused)
    # if report_file.suffix != '.xlsx':
    #     warnings.warn("The output extension should be '.xlsx', instead of '{0}'".format(report_file.suffix))
    #     return 2

    # iterate through each class file
    for class_file in lab_list:
        print(f"\nNow checking {str(class_file.name)} for missing submissions")
        class_data = read_csv_or_xls(class_file)
        # Determine which students in class have not submitted
        prelab_bool = pd.isna(class_data[class_data.columns[assignment_index]])
        # Add suffix to file name to save report
        file_name = output_location/pathlib.Path(str(class_file.stem) + file_suffix + ".xlsx")
        writer = pd.ExcelWriter(file_name)  # Open excel writer to write out report to
        # check each section list against the lab list to see if student names match
        for section_file in section_list:
            section_data = read_csv_or_xls(section_file)
            # there is probably a better way to do this :(
            # Initialize lists
            last_list = []
            first_list = []
            missing_list = []
            # Iterate through each student in each the lab and class sections to compare names and if assignment
            # submitted
            for index_class in range(class_data.shape[0]):
                for index_section in range(section_data.shape[0]):
                    # Get the first and last name of the current student for both the class and section
                    lab_first = class_data[first_name][index_class]
                    lab_last = class_data[last_name][index_class]
                    section_first = section_data[first_name][index_section]
                    section_last = section_data[last_name][index_section]
                    # Check for matching name and missing prelab
                    if (section_first == lab_first) & (section_last == lab_last) & prelab_bool[index_class]:
                        # add name to list if matches and prelab is missing
                        last_list.append(lab_last)
                        first_list.append(lab_first)
                        missing_list.append(prelab_bool[index_class])
            # Write new sheet if any missing assignments
            if last_list:
                sheet_name = section_file.stem
                output_data = pd.DataFrame(list(zip(last_list, first_list)),
                                           columns=['Last Name', 'First Name'])
                output_data.to_excel(writer, sheet_name=sheet_name, index=False)
                fix_column_width(writer=writer, sheet_name=sheet_name, df=output_data)
            else:
                print(f"\tNo missing assignments in {str(section_file.stem)}")
        writer.save()
    return 0


if __name__ == '__main__':
    print("These functions can be run individually but it is best to run them from the utility script using proper "
          "argument parsing")
    exit(0)

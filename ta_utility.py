"""
v1.0.2
This script has various utilities to automate TA work for 3201.

This file contains only the argument parsing structure, with the main functions located in "libs/main_functions.py" and
helper functions located in "libs/helper_functions.py".
"""

# Built in libraries
import argparse
import pathlib

# Custom argparse help formatter
from libs.help_formatter import CustomHelpFormatter

# Main functions
from libs.main_functions import create_sign_in_sheets, check_pre_labs, make_checkoffs


def select_function(input_arguments: argparse.Namespace) -> int:
    """
The main function which selects the arguments run
    :param input_arguments: Arguments parsed in
    :return: exit code
    """
    if input_arguments.subcommand == 'sign-in':
        return create_sign_in_sheets(section_list_location=input_arguments.section_lists,
                                     sign_in_file=input_arguments.output_file,
                                     first_name=input_arguments.first_name,
                                     last_name=input_arguments.last_name)
    elif input_arguments.subcommand == 'check-pre-labs':
        return check_pre_labs(section_list_location=input_arguments.section_lists,
                              file_suffix=input_arguments.file_suffix,
                              prelab_location=input_arguments.prelab_location,
                              output_location=input_arguments.output_location,
                              assignment_index=7,  # Default position of assignment in eLearning documents
                              first_name=input_arguments.first_name,
                              last_name=input_arguments.last_name)
    elif input_arguments.subcommand == 'make-checkoffs':
        return make_checkoffs(section_list_location=input_arguments.section_lists,
                              checkoff_file=input_arguments.output_file,
                              checkoff_list_file=input_arguments.list_file,
                              checkoff_header=input_arguments.checkoff_header,
                              first_name=input_arguments.first_name,
                              last_name=input_arguments.last_name)
    else:
        print(f"Command '{input_arguments.subcommand}' is not recognized")
        return 1


"""
The argument parser setup for the utility.
The main functions can be found in libs.main_functions. Some helper functions are located in libs.helper_functions
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Utilities for EE/CE3201")  # , formatter_class=CustomFormatter)

    subparsers = parser.add_subparsers(dest='subcommand',
                                       title='functions',
                                       required=True,
                                       # metavar='subcommand',
                                       help="Each function runs a utility for creating useful documents for labs")
    parser.add_argument('-fc', '--first-name-column-header',
                        dest='first_name',
                        type=str,
                        default='First Name',
                        help="default: 'First Name'")
    parser.add_argument('-lc', '--last-name-column-header',
                        dest='last_name',
                        type=str,
                        default='Last Name',
                        help="default: 'Last Name'")

    # Parser for creating sign in sheets
    # For git
    parser_sign_in = subparsers.add_parser('sign-in', formatter_class=CustomHelpFormatter, help="Make sign in sheets.")
    parser_sign_in.add_argument('-sl', '--section-lists',
                                type=pathlib.Path,
                                default='section_lists/',
                                metavar='/path/to/section/files/',
                                help="default: 'section_lists/'"
                                )
    parser_sign_in.add_argument('-o', '--output-file',
                                type=pathlib.Path,
                                default='output/sign_ins.xlsx',
                                metavar='/path/to/output/file.xlsx',
                                help="default: 'output/sign_ins.xlsx'")

    # Parser for creating check off sheets
    parser_checkoff = subparsers.add_parser('make-checkoffs',
                                            help="Make checkoff sheets for all sections for an individual lab.",
                                            formatter_class=CustomHelpFormatter)
    parser_checkoff.add_argument('-sl', '--section-lists',
                                 type=pathlib.Path,
                                 default='section_lists/',
                                 metavar='/path/to/section/files/',
                                 help="default: 'section_lists/"
                                 )
    parser_checkoff.add_argument('-o', '--output-file',
                                 type=pathlib.Path,
                                 default='output/checkoffs.xlsx',
                                 metavar='/path/to/output/file.xlsx',
                                 help="default: 'output/checkoffs.xlsx'")
    parser_checkoff.add_argument('-cl', '--checkoff-list',
                                 type=pathlib.Path,
                                 default='checkoff_lists/3201_checkoff_lists.csv',
                                 metavar='list_file',
                                 dest='list_file',
                                 help="A file containing a list or table of checkoffs \
                                 (default: 'checkoff_lists/3201_checkoff_lists.csv')")
    parser_checkoff.add_argument('-ch', '--checkoff-header',
                                 type=str,
                                 default=None,
                                 metavar='checkoff_header',
                                 help="By default, the first column in the list file will be selected but any string"
                                      "that matches a column header ni the checkoff file works.")

    # Parser for checking if pre-labs are complete
    parser_prelab = subparsers.add_parser('check-pre-labs',
                                          help="Determine which students in each section have not completed pre-lab.",
                                          formatter_class=CustomHelpFormatter)
    parser_prelab.add_argument('-sl', '--section-lists',
                               type=pathlib.Path,
                               default='section_lists/',
                               metavar='/path/to/section/files/',
                               help="default: 'section_lists/"
                               )
    parser_prelab.add_argument('-su', '--file-suffix',
                               type=str,
                               default='_Report',
                               metavar='file[_suffix].xlsx',
                               help="default: '_Report'")
    parser_prelab.add_argument('-pl', '--prelab-location',
                               type=pathlib.Path,
                               default='pre_lab_lists/',
                               metavar='/path/to/prelab/grade/file.csv',
                               help="default: 'pre_lab_lists/'")
    parser_prelab.add_argument('-o', '--output-location',
                               type=pathlib.Path,
                               default='output/',
                               metavar='/location/to/save/output/',
                               help="Where to save the output (default: 'output/')")

    # args = parser.parse_args(['check-pre-labs'])
    # args = parser.parse_args(['sign-ins', '-o', './output/fall2021_sign_in.xlsx'])
    # args = parser.parse_args(['make-checkoffs', '-o', 'Lab3Checkoffs.xlsx'])
    # args = parser.parse_args(['make-checkoffs', '-ch', 'Lab 12', '-o', 'output/checkoff12.xlsx'])
    args = parser.parse_args()
    exit(select_function(args))

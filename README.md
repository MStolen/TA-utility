<h1>3201 Utility</h1>
<h2>Purpose</h2>
The purpose of this project is to make creating documents for 
EE/CE3201 easier. These documents take the form of Excel files due
to the tabular nature of class lists, checkoffs, etc.

It is recommended to create a virtual environment to run this application.
You can install the dependencies using <code>pip install -r requirements.txt</code>.
Running the setup script <code>./setup.sh</code>, in a UNIX (or UNIX-like) environment
will do this for you.

Use the command <code>python -m 3201_utility --help</code>
for detailed information related to running the program. Alternatively, running the scripts in the [scripts](scripts)
folder will run the programs in their most basic forms. 

<h2>Expected File Formats</h2>
The input files to this program are all expected to be either CSV or XLS files.
Generally, these are expected to be in the format provided by BlackBoard collaborate.
<h3>Lab Checkoffs</h3>
The file input for the checkoffs expects a single column per set of checkoffs
(see the included [3201 checkoff list](checkoff_lists/3201_checkoff_lists.csv) for an example)
The first row should be the name of the file and the following rows should be the names of the checkpoints.

<h3>Sign-In Sheets</h3>
The expected inputs are the BlackBoard class list files. Provide the path to a folder containing the class list 
for each section (the default folder is called <code>section_lists</code>).
The output will be a single Excel file with a different sheet for each section.

<h3>Pre-lab Checks</h3>
This function checks to ensure that students have turned in an assignment. It requires the same section
lists as the sign-in sheets, as well as the download from grade center for the <b>specific assignment</b>. Again, 
provide the script with the correct path to the assignment files (default is a folder named <code>pre_lab_lists</code>)
and the output will be one Excel file per assignment file with a single tab for each section with missing assignments.

<h2>Running Basic Scripts</h2>
The following terminal commands would create the required folders, then run all commands:

<code>./setup.sh</code> Install virtual environment and create default folder structure

<u>Add required files before running the remaining scripts!</u>

<code>./make_sign_ins.sh</code> Create sign-in sheets for each lab section.

<code>./make_checkoffs.sh "Lab 5"</code> Create checkoff sheets for lab 5
(notice that <code>"Lab 5"</code> is added at the end.
This argument should match a column header in the checkoff list file).

<code>./check_prelabs.sh</code> Check for missing pre-lab assignments 
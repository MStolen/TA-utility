<h1>3201 Utility</h1>
<h2>Purpose</h2>
The purpose of this project is to make creating documents for 
EE/CE3201 easier. These documents take the form of Excel files due
to the tabular nature of class lists, checkoffs, etc.

It is recommended to create a virtual environment to run this application.
You can install the dependencies using <code>pip install -r requirements.txt</code>

Use the command <code>python -m 3201_utility --help</code>
for detailed information related to running the program

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
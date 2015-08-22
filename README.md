# latido_batch_progress_report

Utility for instructors using Latido.

This simple program reads a directory of .latido files and produces a progress report showing each student's total score and last completed exercise. Each entry also includes a detail view showing the progress on each exercise.

.latido files are encrypted with an 8-character key which is defined in the Latido module the file was created with. The default module uses the key 'eyesears'. If your students use a different module than the default, you need to enter that module's key (found in the module's .xml file).

There is an option to search subfolders as well. This can be useful if your classroom management software allows you to download all submitted files at once but automatically groups them into separate folders for each student. (LMS does this, and I think Blackboard does too.)

The report can be exported to a text file which can then be easily imported into Excel or other spreadsheet or database program. The field delimiters are commas.

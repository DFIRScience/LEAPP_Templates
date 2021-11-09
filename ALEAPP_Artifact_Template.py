#Edit ilap_artifacts.py
#     from scripts.artifacts.XXFILENAMEXX import get_XXFUNCTIONXX
#     'XXFUNCTIONXX':('XXCATEGORYNAMEXX', 'XXARTIFACT FILEXX'),

# Module Description: XX
# Author: XX
# Date: 202X-XX-XX
# Artifact version: 0.0.X
# Android version tested: XX
# Requirements: none

# Python libraries to include. If they are not from the
# python standard library, put a note in 'requirements'
import XX as XX

# ALEAPP includes for reporting and other functions (no need to change)
from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows, open_sqlite_db_readonly, does_table_exist

# Class to monitor events in ALEAPPGUI (no need to change)
class keyboard_event:
    def __init__(self, id, app, text, textbox_name, textbox_id, event_date, start_date='', end_date=''):
        self.id = id
        self.app = app
        self.text = text
        self.textbox_name = textbox_name
        self.textbox_id = textbox_id
        self.event_date = event_date
        self.start_date = start_date
        self.end_date = end_date

# Main function for the module - should have the same name as entered in ilap_artifacts.py
# files_found is all files matching the search string
# report_folder is the output folder set by the user
def get_get_XXFUNCTIONXX(files_found, report_folder, seeker, wrap_text):
    # Use the following logfunc to initially test the script
    #logfunc("If you can read this, the module is working!")
    #logfunc(files_found)

    ###### Main artifact parser code goes here #######
    for file_found in files_found: # Get a list of matching files
        file_found = str(file_found) # get one file at a time
        # process the file & extract useful info
 
    if artifactsFound == True: # If we found artifacts, write to report
        report = ArtifactHtmlReport('XXREPORT NAMEXX')
        report.start_artifact_report(report_folder, 'XXREPORT FOLDERXX')
        report.add_script()
        data_headers = ('XXCOL1XX','XXCOL1XX') # final , needed for table formatting
        data_list = []
        data_list.append((XXARTIFACT1XX, XXARTIFACT2XX))
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
            
        tsvname = f'XXREPORT NAMEXX'
        tsv(report_folder, data_headers, data_list, tsvname)
    else:
        logfunc('No XXARTIFACT NAMEXX found')

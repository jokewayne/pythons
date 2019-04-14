# $language = "python"
# $interface = "1.0"

# AddCommentToLog.py
#
# Description:
#   This example script allows you to add a custom line of text to your
#   SecureCRT log file.  The user will be prompted for the text to add
#   to the log file; logging will be stopped; the text provided by the
#   user will be appended to the log file; then SecureCRT logging will
#   be restarted.
#    
#   This method only works with connections associated with a Session
#   configuration in which a log file is specified.
#
# Demonstrates:
#   - How to prompt for user input using the SecureCRT InputBox() function.
#   - How to access Session.LogFileName to determine the log file name
#     stored for the current session.
#   - How to use the Session.Logging property to determine if logging
#     is currently active.
#   - How to use the Python replace() method to substitute substrings
#     within an existing string.
#   - How to use the Python file object to open an existing text file
#     and append data.
#

import os
import datetime
from sys import version_info

scriptname = os.path.basename(__file__)
basedir = os.path.abspath("")
daystr = datetime.datetime.now().strftime('%Y%m%d')
datetimestr = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
mystr = str(version_info.major) + "." + str(version_info.minor)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Main():
	# Make this script tab safe
	tab = crt.GetScriptTab()
        crt.Dialog.MessageBox( scriptname + " is running on dir " + basedir + "\n today is " + daystr + " and log file name is " + scriptname + "-" + datetimestr)
        crt.Dialog.MessageBox(mystr + " world!")
Main()

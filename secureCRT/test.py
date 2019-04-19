# $language = "python"
# $interface = "1.0"

# encoding=utf8
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
import sys
sys.path.append('D:/works/secureCRT_python')

import os
import tester

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # Make this script tab safe
    tab = crt.GetScriptTab()
    f = tester.test_a
    str = f()
    crt.Dialog.MessageBox(str)

Main()

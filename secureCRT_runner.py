# $language = "python"
# $interface = "1.0"

szPrompt = "#"
objTab = None

def setPrompt(promptstr):
    global szPrompt
    if (len(str(promptstr)) > 0 ):
        szPrompt = promptstr
'''
自动识别当前提示符
只能是在当前不切换用户，不切换目录时，才好用
任何引起提示符变化的命令，都导致失败
'''
def autosetPrompt():
    global szPrompt, objTab
    if objTab == None:
        objTab = crt.GetScriptTab()
    if objTab.Session.Connected != True:
        return
    objTab.Screen.Synchronous = True
    objTab.Screen.Send("\r\n")
    objTab.Screen.WaitForString("$", 1)
    objTab.Screen.Send("\r\n")
    objTab.Screen.WaitForString("$", 1)
    screenrow = crt.Screen.CurrentRow
    szResult = crt.Screen.Get(screenrow, 1, screenrow, 40)
    newprompt = str(szResult).strip()
    setPrompt(newprompt)
    return szResult

def getcmdresult(cmdstr):
    global szPrompt, objTab
    autosetPrompt()
    if objTab == None:
        objTab = crt.GetScriptTab()
    if objTab.Session.Connected != True:
        return
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True
    if ( len(str(cmdstr)) > 0 ):
        szCommand = str(cmdstr)
    else:
        return
    objTab.Screen.Send(szCommand + "\r\n")
    if (objTab.Screen.WaitForString(szCommand + "\r\n", 1)) != True:
        crt.Dialog.MessageBox("等不到["+szCommand+"]")
    szResult = objTab.Screen.ReadString(szPrompt, 2)
    return szResult

def Main():
    for i in range(0,10):
        cmdstr = crt.Dialog.Prompt("输入命令")
        myresult = getcmdresult(cmdstr)
        crt.Dialog.MessageBox(myresult)

Main()

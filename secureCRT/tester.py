# encoding=utf8
import sys
sys.path.append('D:/works/secureCRT_python')
import os
import util

def scriptname():
    return os.path.basename(__file__)

def scriptdir():
    return os.path.abspath("")

def test_a():
    s_name = scriptname()
    basedir = scriptdir()
    daystr = util.datestr()
    datetimestr = util.timestr()
    ptimestr = util.precisetimestr()
    mystr = util.sysver()
    fancy = u'中文的支持吗？!'.encode('utf8')
    #sl = len(fancy)
    fancystr = util.logstr(fancy)
    return s_name + " is running on dir " + basedir + "\ntoday is " + daystr + "\nlog file name is " + s_name + "-" + datetimestr + "\n ptime" + ptimestr +"\npy ver:" + mystr + fancystr


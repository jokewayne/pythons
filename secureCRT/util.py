# encoding=utf8
import datetime
import sys
import os

def datestr():
    return datetime.datetime.now().strftime('%Y%m%d')

def timestr():
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

def precisetimestr():
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')

def sysver():
    return str(sys.version_info.major) + "." + str(sys.version_info.minor)

def scriptname():
    return os.path.basename(__file__)

def scriptdir():
    return os.path.abspath("")

def logstr( pstr):
    slen = len(str(pstr))
    counttime = slen/2 + 2
    outstr = "\n"
    for i in range(0, counttime):
        outstr = outstr + "c"
    for i in range(0, counttime):
        outstr = outstr + "s"
    outstr = outstr + "\nc "
    outstr = outstr + pstr
    outstr = outstr + " s\n"
    for i in range(0, counttime):
        outstr = outstr + "c"
    for i in range(0, counttime):
        outstr = outstr + "s"
    outstr = outstr + "\n"
    return outstr

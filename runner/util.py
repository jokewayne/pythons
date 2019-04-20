# encoding=utf8
import datetime
import sys
import os

#得到当前年月日的字符串
def datestr():
    return datetime.datetime.now().strftime('%Y%m%d')
#得到当前年月日-时分秒的字符串
def timestr():
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
#得到当前年月日-时分秒-毫秒的字符串
def precisetimestr():
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
#当前python版本号
def sysver():
    return str(sys.version_info.major) + "." + str(sys.version_info.minor)
#本脚本名
def scriptname():
    return os.path.basename(__file__)
#本脚本目录，有时似乎不准确
def scriptdir():
    return os.path.abspath("")

'''
入参：要转换格式的字符串
将字符串转为一个特别的多行格式，多行是以"\n"分隔。
让人可以看出这个是给人看的日志。
大致的输出如下：
cccccccccccccccccccccssssssssssssssssssssss
c 这个就是多行的日志                     s
c 第二行                                  s
c 第三行日志                              s
cccccccccccccccccccccssssssssssssssssssssss

'''
def logstr( pstr):
    tstr = str(pstr)
    strlist = tstr.split("\n")
    maxlen = 0
    for s in strlist:
        if ( maxlen < len(s) ):
            maxlen = len(s)
    slen = maxlen
    counttime = slen/2 + 2
    #另起新行
    outstr = "\n"
    #第一行注释头
    for i in range(0, counttime):
        outstr = outstr + "c"
    for i in range(0, counttime):
        outstr = outstr + "s"
    outstr = outstr + "\n"
    #正式的log文字
    for s in strlist:
        outstr = outstr + "c "
        outstr = outstr + s
        #每行如果不够长，用空格补齐，之后，再用“ s”结尾
        spacelen = 2 * counttime - len(s) - 2
        if ( spacelen > 0):
            for i in range(0, spacelen):
                outstr = outstr + " "
        outstr = outstr + " s\n"
    #最后一行注释尾
    for i in range(0, counttime):
        outstr = outstr + "c"
    for i in range(0, counttime):
        outstr = outstr + "s"
    #log结束，换行
    outstr = outstr + "\n"
    return outstr


if __name__ == "__main__":
    myword = "哈哈\n这就是我想要的换行\n再见咯\nSee you!"
    note = logstr(myword)
    print(note)
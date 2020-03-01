import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
import numpy as np
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
import shutil

#ratelow, 如果highprice> lowprice*ratehigh，且当前价又小于lowprice*ratelow，就卖。

ratehigh = 1.2
ratelow = 1.1

stocksinfo="stocksinfo/"
dict = {}
stockfile = open(stocksinfo+"stock-totalprice.txt","a")
#stockfile_earnprice = open(stocksinfo+"earnprice.txt","a")

def load_stock_data(stock_path="", filename="stock.csv"):
    csv_path = os.path.join(stock_path, filename)
    return pd.read_csv(csv_path)

def test_stockinfo(stock_path="", filename="stock.csv"):
    stocking = load_stock_data(stock_path,filename)
    stocking["year"] = stocking["date"].str[0:4]
    stocking["year"] = stocking["year"].astype("int")
    stocking["month"] = stocking["date"].str[5:7]
    stocking["month"] = stocking["month"].astype("int")
    stocking["day"] = stocking["date"].str[8:10]
    stocking["day"] = stocking["day"].astype("int")
    stocking["x-axis"] = (stocking["month"]-1)*31 + stocking["day"]
    #print("stocking is ",  stocking)
    #print(stocking.head())
    #print(stocking.info())
    #print(stocking.describe())
    print("info done")
    return stocking


def gettotalprice(stock_path="", filename="stock.csv", jpg_path="jpg", jpgfilename="stock.jpg"):
    global stockfile
    print("gettotalprice start")
    x= test_stockinfo(stock_path, filename)
    maxtotal = x.loc[:,"totalprice"].max()
    maxstr = jpgfilename + ", " + str(maxtotal) + "\n"
    print("maxtotal:",maxstr)
    stockfile.write(maxstr)
    print("csvtojpg end")
    del x

def walkdir_gettotalprice(in_path="csv", out_path="jpg"):
    global stockfile
    print("inside walkdir_gettotalprice")
    for root,dirs,files in os.walk(in_path):
        print("inside ",in_path)
        print("root ", root)
        print("dirs ", dirs)
        print("files ", files)
        for file in files:
            #获取文件所属目录
            print("file:",file)
            #获取文件路径
            finname = os.path.join(root,file)
            (filename,extension) = os.path.splitext(file)
            foutname = os.path.join(out_path,filename+".jpg") 
            print("outname:",foutname)
            print("inname:",finname)
            gettotalprice(in_path, file, out_path, filename)
    stockfile.close()

def getearnprice(stock_path="", filename="stock.csv"):
    #global stockfile_earnprice
    print("getearnprice start")
    x= test_stockinfo(stock_path, filename)
    # now x is one stock daily prices info
    # let's get some info out of it.
    lowprice = x.iloc[0]['close']
    highprice = lowprice
    earnprice = 0
    for i in range(0,len(x)):
        cur = x.iloc[i]['close']
        if ( cur > highprice ):
            highprice = cur
            continue
        elif ( cur < lowprice * ratelow ) and ( highprice > lowprice * ratehigh ):
            count += 1
            earnprice = earnprice + highprice - lowprice
            lowprice = cur
            highprice = cur
        elif ( cur < lowprice ):
            lowprice = cur
            highprice = cur
        else:
            continue
    dailyearn = earnprice / len(x)
    meanprice = x.loc[:,"close"].mean()
    earnrate = dailyearn / meanprice
    print("earnrate:",earnrate)
    (filenamenoext,extension) = os.path.splitext(filename)
    writestr = filenamenoext + ", " + str(earnrate) + "\n"
    stockfile_earnprice = open(stocksinfo+"earnprice.txt","a")
    stockfile_earnprice.write(writestr)
    stockfile_earnprice.close()
    del x
    

def walkdir_getearnprice(in_path="csv"):
    global stockfile_earnprice
    print("inside walkdir_get earn price")
    for root,dirs,files in os.walk(in_path):
        print("inside ",in_path)
        print("root ", root)
        print("dirs ", dirs)
        print("files ", files)
        for file in files:
            #获取文件所属目录
            print("file:",file)
            #获取文件路径
            finname = os.path.join(root,file)
            (filename,extension) = os.path.splitext(file)
            getearnprice(in_path, file)


def getearntimes(stock_path="", filename="stock.csv"):
    #global stockfile_earnprice
    print("getearnprice start")
    x= test_stockinfo(stock_path, filename)
    # now x is one stock daily prices info
    # let's get some info out of it.
    lowprice = x.iloc[0]['close']
    highprice = lowprice
    earnprice = 0
    count = 0
    for i in range(0,len(x)):
        cur = x.iloc[i]['close']
        if ( cur > highprice ):
            highprice = cur
            continue
        elif ( cur < lowprice * ratelow ) and ( highprice > lowprice * ratehigh ):
            count += 1
            earnprice = earnprice + highprice - lowprice
            lowprice = cur
            highprice = cur
        elif ( cur < lowprice ):
            lowprice = cur
            highprice = cur
        else:
            continue
    dailyearn = earnprice / len(x)
    meanprice = x.loc[:,"close"].mean()
    earnrate = dailyearn / meanprice
    (filenamenoext,extension) = os.path.splitext(filename)
    writestr = filenamenoext + ", " + str(earnrate) + "\n"
    timesstr = filenamenoext + ", " + str(count) + "\n"
    stockfile_earnprice = open(stocksinfo+"earnprice.txt","a")
    stockfile_earnprice.write(writestr)
    stockfile_earnprice.close()
    stockfile_earnprice = open(stocksinfo+"earntimes.txt","a")
    stockfile_earnprice.write(timesstr)
    stockfile_earnprice.close()
    del x
    

def walkdir_getearntimes(in_path="csv"):
    global stockfile_earnprice
    print("inside walkdir_get earn price")
    for root,dirs,files in os.walk(in_path):
        print("inside ",in_path)
        print("root ", root)
        print("dirs ", dirs)
        print("files ", files)
        for file in files:
            #获取文件所属目录
            print("file:",file)
            #获取文件路径
            finname = os.path.join(root,file)
            (filename,extension) = os.path.splitext(file)
            getearntimes(in_path, file)

def csvtojpg(stock_path="D:/works/hands-on/csv", filename="stock.csv", jpg_path="jpg", jpgfilename="stock.jpg"):
    print("csvtojpg start")
    outjpg = os.path.join(jpg_path,jpgfilename)
    print("outjpg:", outjpg)
    x= test_stockinfo(stock_path, filename)
    maxclose = x.loc[:,"close"].max()
    print("maxclose:",maxclose)
    plist = []
    dict = {}
    for i in range(1999,2020):
        ptmp = x.where(x["year"]==i)
        dict[str(i)]=ptmp
    #drawplot(x)
    plt.figure(figsize=(20,10))
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0.1,wspace=0.1)
    j=1
    for key,pl in dict.items():
        aax =plt.subplot(5,5,j)
        aax.set_ylim(0,maxclose+10)
        aax.set_xlim(0,390)
        j+=1
        pl.plot(ax=aax, kind="scatter",x="x-axis",y="close",alpha=0.7,
                s=pl["totalprice"]/10000000, label=key)
    plt.savefig(outjpg,dip=400)
    plt.close()
    print("csvtojpg end")
    del x

def tocsv(in_path="export", out_path="csv"):
    for root,dirs,files in os.walk(in_path):
        for file in files:
            #获取文件所属目录
            print("file:",file)
            #获取文件路径
            finname = os.path.join(root,file)
            (filename,extension) = os.path.splitext(file)
            foutname = os.path.join(out_path,filename+".csv") 
            print("outname:",foutname)
            print("inname:",finname)
            f = open(finname, "r")
            fout = open(foutname, "w")
            fout.write("date,open,high,low,close,count,totalprice\n")
            lines = f.readlines()
            i = 0
            for line in lines:
                if (line[0] == "1" or line[0] == "2" ):
                    i = i  + 1
                    fout.write(line)
            fout.close()
            f.close()
            if i == 0:
                os.remove(foutname)



def getdict(stockinfofile="stock-totalprice.txt"):
    global dict 
    f = open(stocksinfo+stockinfofile, "r")
    lines = f.readlines()
    for l in lines:
        key, value = l.split(",")
        value=value.strip()
        print("key",key)
        print("value",value)
        dict[key] = float(value)

def dosort(outputfile="stock-totalprice-sorted.txt"):
    global dict
    d2 = sorted(dict.items(), key = lambda x:x[1], reverse=True)
    f = open(stocksinfo+outputfile, "w")
    for key in d2:
        istr = ""
        for x in key:
            istr = istr + str(x) + " "
        istr = istr + "\n"
        f.write(istr) 

def getsortedjpg(sortedfile="stock-totalprice-sorted.txt", filedir = "pickstock"):
    os.makedirs(filedir)
    f = open(stocksinfo+sortedfile, "r")
    lines = f.readlines()
    i = 0
    for l in lines:
        i+= 1
        x = l.split(" ")
        filename = x[0] 
        totalprice = x[1] 
        print("filename:" , filename, " total:", totalprice)
        file = filename + ".jpg"
        csvtojpg("csv", filename + ".csv", "bestjpg", file)
        shutil.copy("bestjpg/" + file, filedir)
        if ( i > 30):
            break

def domaxtotalpick():
    print("you should have the following dirs")
    print("export, csv, bestjpg, pickstock")
    print("now we start")
    print("convert export data to csv format, save into csv dir")
    tocsv()
    print("convert done")
    print("get all stock's totalprice")
    walkdir_gettotalprice()
    print("start sorted totalprice")
    getdict()
    dosort()
    print("sorted done")
    print("convert the top 100 stock to jpg")
    getsortedjpg()
    print("now check pickstock dir")

def doearninfo():
    print("get all stock's earn price")
    walkdir_getearnprice()
    print("start sorted earnprice")
    getdict("earnprice.txt")
    dosort("earnprice-sorted.txt")
    print("sorted done")
    print("convert the top 100 stock to jpg save in bestjpg dir, copy them in pickstock dir")
    getsortedjpg("earnprice-sorted.txt", "pickearnprice")

def doearntimes():
    print("get all stock's earn times")
    walkdir_getearntimes()
    print("start sorted earntimes")
    getdict("earntimes.txt")
    dosort("earntimes-sorted.txt")
    print("sorted done")
    print("convert the top 100 stock to jpg save in bestjpg dir, copy them in pickstock dir")
    getsortedjpg("earntimes-sorted.txt", "pickearntimes")

def justsorted():
    getdict("earnprice.txt")
    dosort("earnprice-sorted.txt")
    print("sorted done")
    print("convert the top 100 stock to jpg save in bestjpg dir, copy them in pickstock dir")
    getsortedjpg("earnprice-sorted.txt", "pickearnprice")

def pickstock(in_path="csv", out_path="jpg"):
    global stockfile
    print("inside pickstock walkdir")
    for root,dirs,files in os.walk(in_path):
        print("inside ",in_path)
        print("root ", root)
        print("dirs ", dirs)
        print("files ", files)
        for file in files:
            #获取文件所属目录
            print("file:",file)
            #获取文件路径
            finname = os.path.join(root,file)
            (filename,extension) = os.path.splitext(file)
            foutname = os.path.join(out_path,filename+".jpg") 
            print("outname:",foutname)
            print("inname:",finname)
            #gettotalprice(in_path, file, out_path, filename)
    stockfile.close()

if __name__ == "__main__":
    #domaxtotalpick()
    #doearninfo()
    #justsorted()
    doearntimes()



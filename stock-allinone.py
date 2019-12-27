import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
import numpy as np
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
import shutil

dict = {}
stockfile = open("stock-totalprice.txt","a")

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

def walkdir(in_path="csv", out_path="jpg"):
    global stockfile
    print("inside walkdir")
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



def getdict():
    global dict 
    f = open("stock-totalprice.txt", "r")
    lines = f.readlines()
    for l in lines:
        key, value = l.split(",")
        value=value.strip()
        print("key",key)
        print("value",value)
        dict[key] = float(value)

def dosort():
    global dict
    d2 = sorted(dict.items(), key = lambda x:x[1], reverse=True)
    f = open("stock-totalprice-sorted.txt", "w")
    for key in d2:
        istr = ""
        for x in key:
            istr = istr + str(x) + " "
        istr = istr + "\n"
        f.write(istr) 

def getsortedjpg():
    filedir = "pickstock"
    f = open("stock-totalprice-sorted.txt", "r")
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
        if ( i > 101):
            break




if __name__ == "__main__":
    print("you should have the following dirs")
    print("export, csv, bestjpg, pickstock")
    print("now we start")
    print("convert export data to csv format, save into csv dir")
    tocsv()
    print("convert done")
    print("get all stock's totalprice")
    walkdir()
    print("start sorted totalprice")
    getdict()
    dosort()
    print("sorted done")
    print("convert the top 100 stock to jpg")
    getsortedjpg()
    print("now check pickstock dir")
    



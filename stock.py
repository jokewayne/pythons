import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
import numpy as np
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

def load_stock_data(stock_path="D:/works/hands-on"):
    csv_path = os.path.join(stock_path, "stock.csv")
    return pd.read_csv(csv_path)

def test_stockinfo():
    stocking = load_stock_data()
    stocking["year"] = stocking["date"].str[0:4]
    stocking["year"] = stocking["year"].astype("int")
    stocking["month"] = stocking["date"].str[5:7]
    stocking["month"] = stocking["month"].astype("int")
    stocking["day"] = stocking["date"].str[8:10]
    stocking["day"] = stocking["day"].astype("int")
    stocking["x-axis"] = (stocking["month"]-1)*31 + stocking["day"]
    print("stocking is ",  stocking)
    print(stocking.head())
    print(stocking.info())
    print(stocking.describe())
    print("info done")
    return stocking

def drawplot(stocking=None):
    fig, drawdata = plt.subplots()
    for key, grp in stocking.groupby["year"]:
        
        drawdata= grp.plot(ax=drawdata, kind="line",x="x-axis",y="closeprice", 
            c=key, label=key)
        """
        stocking.plot(kind="scatter",x="x-axis",y="closeprice",alpha=1,
            s=stocking["totalprice"]/50000000, label="totalprice",
            c="year", cmap=plt.get_cmap("jet"), colorbar=True)
        """
    plt.legend(loc="best")
    plt.show()

def drawdots(stocking=None):
    stocking.plot(kind="scatter",x="x-axis",y="closeprice",alpha=0.7,
            s=stocking["totalprice"]/10000000, label="totalprice",
            c="year", cmap=plt.get_cmap("jet"), colorbar=True)

if __name__ == "__main__":
    print("main start")
    x= test_stockinfo()
    plist = []
    dict = {}
    for i in range(1999,2020):
        ptmp = x.where(x["year"]==i)
        dict[str(i)]=ptmp
    #drawplot(x)
    
    plt.figure()
    j=1
    for key,pl in dict.items():
        aax =plt.subplot(5,5,j)
        aax.set_ylim(0,25)
        j+=1
        pl.plot(ax=aax, kind="scatter",x="x-axis",y="closeprice",alpha=0.7,
                s=pl["totalprice"]/10000000, label=key,
            c="year", cmap=plt.get_cmap("jet"), colorbar=True)
    plt.show()
    print("main end")

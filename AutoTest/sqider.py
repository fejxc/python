from bs4 import BeautifulSoup  #帮助我们数据获取，网页解析
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error #指定URL，获取网页数据,python3的时候 urlbib整合了1和2的版本
import xlwt  #存excell
import sqlite3 #进行sqlite数据库操作

#导包，灰色是因为没有调用，发生调用才会变色
#一个功能就是一个函数


#1、爬取网页
#2、解析数据，一个一个网页的解析
#3、保存数据

def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)  #爬取文件
    savepath=r".\豆瓣电影Top250.xls"
    saveData(savepath)  #保存数据

#爬取网页
def getData(baseurl):
    datalist=[]
    #单个网页的解析
    return datalist



#保存数据
def saveData(savepath):
    print("save+++++++")
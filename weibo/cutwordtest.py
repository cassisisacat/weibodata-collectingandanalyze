# encoding='utf-8'


import jieba
import string
import sys
import os
import csv

jieba.load_userdict("路径\dict_baidu_utf8.txt")
jieba.load_userdict("路径\dict_pangu.txt")
jieba.load_userdict("路径\dict_sougou_utf8.txt")
jieba.load_userdict("路径\dict_tencent_utf8.txt")
jieba.load_userdict("路径\SogouLabDic.txt")

stopwords = {}.fromkeys([ line.rstrip() for line in open('路径\Stopword.txt',encoding='utf-8' )])
with open('路径\如懿抽样.csv',encoding='utf-8')as csvfile:
        reader=csv.reader(csvfile)
        column=[row[0] for row in reader]

index_weibo = len(column)

def get_data(index_weibo):
   
    
    result=[]

    seg = jieba.lcut(column[index_weibo],cut_all=False)

    for i in seg:
        if i not in stopwords:
            result.append(i)
    
    fo=open('路径\data_full.dat','a+',encoding='utf-8')

    for j in result:
        fo.write(j)
        fo.write(' ')
    
    fo.write('\r\n')
    fo.close()
        
    

if __name__=='__main__':

    total_weibo= index_weibo
    print("进程开始...")
    for index_weibo in range(1,total_weibo):
        
        get_data(index_weibo)
       
        
    print("Done!")


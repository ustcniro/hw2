import sqlite3 as sq
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
# 创建数据库连接对象，存储在test.db中
def graph1():
    conn = sq.connect('data.db')
    cursor=conn.cursor()
    cursor.execute("select * from Population")
    dataall=cursor.fetchall()   #0代表年份，1代表总人口，2代表男性人口，3代表女性人口
    a=[0]*20  #年份
    b=[0]*20  #总人口
    c=[0]*20  #男性人口比例
    d=[0]*20  #女性人口比例
    for i in range(20):
       a[i]=dataall[i][0]
       b[i]=dataall[i][1]
       c[i]=round((dataall[i][2]/dataall[i][1])*100,1) #保留小数1位
       d[i]=round((dataall[i][3]/dataall[i][1])*100,1)
    fmt = '%.2f%%'
    yticks = mtick.FormatStrFormatter(fmt)      # 设置百分比形式的坐标轴
    plt.rcParams['font.sans-serif']=['SimHei']  # 设置中文字体，否则标签无法显示中文
    fig = plt.figure(figsize=(12,6), dpi=120)   #大小，像素点个数
    ax1 = fig.add_subplot(111)                  #设置子图
    ax1.plot(range(20),c, 'or-', label=u'男性人口比例',color='red');      #画折线图
    ax1.plot(range(20),d, 'or-', label=u'女性人口比例',color='yellow');
    ax1.yaxis.set_major_formatter(yticks)       #设置纵轴
    for x,y in enumerate(c):
        plt.text(x , y+0.05 , '%s' % round(y,2),ha='center' ,color='blue',fontsize=10 )  # 将数值显示在图形上
    for x, y in enumerate(d):
        plt.text(x , y+0.05, '%s' % round(y,2), ha='center',color='red', fontsize=10)
    ax1.legend(loc=1)              #1表示左边，设置标签
    ax1.set_ylim([48, 51.85]);     #设置y轴范围
    ax1.set_ylabel('男女人口比例（%)',fontproperties='SimHei',fontsize=10)  #设置坐标轴注释
    ax1.set_xlabel('年份（年）', fontproperties='SimHei',fontsize=10)

    ax2 = ax1.twinx()              #设置图中的子图
    plt.bar(range(20), b,label=u'总人口',alpha=0.3)  #画条形图，注意透明度设定
    ax2.legend(loc=2)
    ax2.set_ylim(120000, 145000)  # 设置y轴取值范围
    plt.legend(prop={'family': 'SimHei', 'size': 8}, loc="upper left")    #设置标签参数
    plt.xticks(range(20), a, fontproperties='SimHei', rotation=0)
    plt.ylabel('年末总人口（单位：万人）', fontproperties='SimHei',fontsize=10)
    plt.title('1999-2018总人口条形图及男女人口比例折线图', fontproperties='SimHei',fontsize=20)
    for x, y in enumerate(b):
        plt.text(x , y , '%s' % round(y,1),ha='center', color='green', fontsize=10)  # 将数值显示在图形
    plt.show()

def graph2():
    conn = sq.connect('data.db')
    cursor=conn.cursor()
    cursor.execute("select * from Work")
    dataall=cursor.fetchall()   #0代表年份，1代表总人口，2代表男性人口，3代表女性人口
    a=[0]*8  #年份
    b=[0]*8  #总就业人口
    c=[0]*8  #城镇就业人口
    d=[0]*8  #乡村就业人口
    for i in range(8):
       a[i]=dataall[i+11][0]
       b[i]=dataall[i+11][1]
       c[i]=dataall[i+11][2]
       d[i]=dataall[i+11][3]
    bar_width=0.38
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体，否则标签无法显示中文
    fig = plt.figure(2,figsize=(14,6))
    fig.suptitle('就业人口数据',fontsize=20)

    plt.subplot(121,facecolor='wheat')   #子图
    plt.bar(np.arange(8), c,  label=u'城镇就业人口',color='blue',width=bar_width)       # 画水平交错图
    plt.bar(np.arange(8)+bar_width, d, label=u'乡村就业人口', color='red',width=bar_width)
    for x, y in enumerate(c):
        plt.text(x, y+100, '%s' % round(y, 1), ha='center', color='blue', fontsize=8)  # 将数值显示在图形上
    for x, y in enumerate(d):
        plt.text(x+bar_width, y+100, '%s' % round(y, 1), ha='center', color='red', fontsize=8)  # 将数值显示在图形上
    plt.xticks(np.arange(8)+bar_width/2, a, fontproperties='SimHei', rotation=0)
    plt.ylabel('就业人口（单位：万人）', fontproperties='SimHei', fontsize=10)
    plt.title('城镇乡村就业人口图', fontproperties='SimHei', fontsize=15)
    plt.xlabel('年份',fontproperties='SimHei', fontsize=10)
    plt.ylim(30000,45000)
    plt.legend(loc=1,fontsize=10)

    plt.subplot(243)
    workrate1=[round(dataall[11][2]/dataall[11][1],4),round(dataall[11][3]/dataall[11][1],4)]
    labels=['城镇','乡村']
    explode=[0.1,0]
    plt.pie(workrate1,explode=explode,labels=labels,autopct='%1.2f%%',shadow=True)
    plt.title('2010年', loc='right')

    plt.subplot(244)
    workrate1 = [round(dataall[13][2] / dataall[13][1], 4), round(dataall[13][3] / dataall[13][1], 4)]
    labels = ['城镇', '乡村']
    explode = [0.1, 0]
    plt.pie(workrate1, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True)
    plt.title('2012年', loc='right')

    plt.subplot(247)
    workrate1 = [round(dataall[15][2] / dataall[16][1], 4), round(dataall[15][3] / dataall[16][1], 4)]
    labels = ['城镇', '乡村']
    explode = [0.1, 0]
    plt.pie(workrate1, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True)
    plt.title('2014年', loc='right')

    plt.subplot(248)
    workrate1 = [round(dataall[18][2] / dataall[18][1], 4), round(dataall[18][3] / dataall[18][1], 4)]
    labels = ['城镇', '乡村']
    explode = [0.1, 0]
    plt.pie(workrate1, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True)
    plt.title('2017年', loc='right')
    plt.show()

def main():
     str = input("请选择需要画出来的图（1或2）：")
     if str=='1':
         graph1()
     if str=='2':
         graph2()
     else:
         print("输入错误")

if __name__ == '__main__':

    main()
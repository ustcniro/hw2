import sqlite3 as sq
from obtaindata import Population
class sqlmisson():
    def __init__(self):
        self.db_name={}    #数据库名
        self.table_name={} #表名
        self.conn={}       #连接
        self.year=[0]*20   #相关列表的初始化
        self.total=[0]*20
        self.male=[0]*20
        self.female=[0]*20
        self.year1=[0]*20
        self.total1=[0]*20
        self.city=[0]*20
        self.urban=[0]*20
        self.k=Population()
    def dataclean1(self): #进行人口数据的整理
        self.k.getdata1()
        for i in range(20):
            self.year[i]=int(self.k.result['returndata']['datanodes'][19-i]['wds'][1]['valuecode'])
            self.total[i]=int(self.k.result['returndata']['datanodes'][19-i]['data']['data'])
            self.male[i]=int(self.k.result['returndata']['datanodes'][39-i]['data']['data'])
            self.female[i]=int(self.k.result['returndata']['datanodes'][59-i]['data']['data'])
    def create1(self): #创建人口数据的数据库，存入本地数据库
        # 数据库名
        self.db_name = "data.db"
        # 表名
        self.table_name = "Population"
        self.conn = sq.connect(self.db_name)
        cursor=self.conn.cursor()
        #cursor.execute("CREATE TABLE Population(year int,total int ,male int ,female int)")  #新建的数据库，已经存在电脑里
        for j in range(20):
            sql = 'insert into Population(year,total,male,female) values(%d,%d,%d,%d)' %(
                   self.year[j],self.total[j],self.male[j],self.female[j])
            cursor.execute(sql)
        self.conn.commit() #插入完之后提交
        cursor.close()
        self.conn.close()

    def dataclean2(self):
        self.k.getdata2()
        for i in range(20):
            self.year1[i]=int(self.k.result['returndata']['datanodes'][19-i]['wds'][1]['valuecode'])
            self.total1[i]=int(self.k.result['returndata']['datanodes'][19-i]['data']['data'])
            self.city[i]=int(self.k.result['returndata']['datanodes'][39-i]['data']['data'])
            self.urban[i]=int(self.k.result['returndata']['datanodes'][59-i]['data']['data'])

    def create2(self):
        self.db_name = "data.db"
        self.table_name = "Work"
        self.conn = sq.connect(self.db_name)
        cursor = self.conn.cursor()
        #cursor.execute("CREATE TABLE Work(year int,total int ,city int ,urban int)")
        for j in range(20):
            sql = 'insert into Work(year,total,city,urban) values(%d,%d,%d,%d)' % (
                self.year1[j], self.total1[j], self.city[j], self.urban[j])
            cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()

def  main():  #测试函数
    test = sqlmisson()
    test.dataclean1()
    test.create1()
if __name__ == '__main__':
    main()

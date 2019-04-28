import requests
import time
import json

class  Population():
    def __init__(self):
        # 目标网址
        self.url='http://data.stats.gov.cn/easyquery.htm'
        self.keyvalue = {}   # 用来传递参数的
        self.headers={}      # 用来定义头部
                             # 头部的填充
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /' \
                            'Chrome/73.0.3683.103 Safari/537.36'
        self.result = {}
    def gettime(self):
            return int(round(time.time() * 1000))

    def getdata1(self): #获取总人口，男性女性人口数据
        # 下面是参数的填充
        self.keyvalue['m'] = 'QueryData'
        self.keyvalue['dbcode'] = 'hgnd'
        self.keyvalue['rowcode'] = 'zb'
        self.keyvalue['colcode'] = 'sj'
        self.keyvalue['wds'] = '[]'
        self.keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
        self.keyvalue['k1'] = str(self.gettime())
        # 建立一个Session
        s = requests.session()
        # 在Session基础上进行一次请求
        r = s.get(self.url, params=self.keyvalue, headers=self.headers)
        # 打印返回过来的状态码
        print(r.status_code)
        # 修改dfwds字段内容
        self.keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
        # 再次进行请求，并加入可能发生错误的识别代码
        try:
            r = s.get(self.url, params=self.keyvalue, headers=self.headers)
            r.raise_for_status()
        except  requests.RequestException as e:
            print(e)
        else:
            r.encoding=r.apparent_encoding
            self.result = json.loads(r.text)
            print(type(self.result))
    def getdata2(self):  #
        # 下面是参数的填充
        self.keyvalue['m'] = 'QueryData'
        self.keyvalue['dbcode'] = 'hgnd'
        self.keyvalue['rowcode'] = 'zb'
        self.keyvalue['colcode'] = 'sj'
        self.keyvalue['wds'] = '[]'
        self.keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0403"}]'
        self.keyvalue['k1'] = str(self.gettime())
        s = requests.session()
        r = s.post(self.url, params=self.keyvalue, headers=self.headers)
        self.keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
        try:
            r = s.post(self.url, params=self.keyvalue, headers=self.headers)
            r.raise_for_status()
        except  requests.RequestException as e:
            print(e)
        else:
            r.encoding=r.apparent_encoding
            self.result = json.loads(r.text)
            print(self.result)

    def writedata(self):   #用来将爬到的数据写入txt文件进行分析
        js = json.dumps(self.result, sort_keys=True, indent=4, separators=(',', ';'), ensure_ascii=False)
        with open('1.txt', 'w') as f:    # 设置文件对象
            f.write(js)                  # 将字符串写入文件中

def  main():  #测试函数
    test = Population()
    test.getdata1()
    test.writedata()
if __name__ == '__main__':
    main()

import requests
import json


# headers = {"Content-Type": "application/x-www-form-urlencoded"}
#请求执行结果
class Sendmethod():
    def __init__(self):
        self.urlstart = "http://192.168.6.100:8017/mall/"
        # self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    #post请求
    def send_post(self,url,json=None):
        url = self.urlstart + url

        response = requests.post(url=url,json=json)
        # res = response.status_code
        # response = response.json()
        # r=json.dumps(response,sort_keys=True,indent=4,ensure_ascii=False)
        restext = response.text
        resatus = response.status_code
        return restext,resatus

    #get请求
    def send_get(self,url):
        url = self.urlstart + url
        # print(url)
        response = requests.get(url)
        restext = response.text
        # restext = json.loads(restext)
        resatus = response.status_code
        return restext,resatus

    #put请求
    def send_put(self,url,json=None):
        url = self.urlstart + url


        response = requests.put(url=url, json=json)
        # res = response.status_code
        # response = response.json()
        # r=json.dumps(response,sort_keys=True,indent=4,ensure_ascii=False)
        restext = response.text
        resatus = response.status_code
        return restext, resatus



#打开文件
class Openfile():
    def __init__(self,file_path):
        self.file_path=file_path
    def openfile(self):
        with open(self.file_path, 'r',encoding='utf-8') as f:
            L=[]
            for line in f:
                line=line.split('|')
                L.append(line)
        return L





# import os
#
# file_path=os.path.abspath(os.path.dirname(__file__))+'/casefile/test_getDicList'
# openf=Openfile(file_path)
# t=openf.open_csv()
# api='http://10.168.17.181/rx_api/api_app/getVerificationCode/'
#
#
# for i in t:
#     url = api + i[0] + ',' + i[1]
#     method = 'POST'
#     print(i[-1])
#     run = Sendmethod(url,i[-1])
#     print('公共类获取字典数据接口'+run.send_post())



# # url = 'http://10.168.17.181/rx_api/api_app/1554973051,1'
# url = 'http://10.168.17.181/rx_api/api_app/merchantBankcard/1,1'
# data={
#         "id": "1",
#         "username": "1554973051",
#         "telphone": "1554973051"
#     }
# # method='POST'
# method='GET'
# sendmethod=Sendmethod(url,data)
# run=Runmethod(method)
# print(run.run_main())
# # print(sendmethod.send_post())
# # run=Runmethod(method)
'''
9.商品历史兑换信息
接口方法： GET
接口地址：privilegeExchange/history?driverId=1589

'''

from send_method import *
api = 'privilegeExchange/history?driverId='#按需更改
file_path = './mallParameter/test_homePage.txt'#txt文件统一建在casefile下
f = Openfile(file_path)
t = f.openfile()

L = []
error = []
ok = 0
for i in t:
    url = api + i[0]  + "&" +i[1]   #按需拼接参数

run = Sendmethod() # get参数 不用传
r, res = run.send_get(url)  # 按需选择请求方式
if res == 200:
    ok += 1
    # print(type(r))
    if "系统错误，请联系管理员" in r:
        error.append(r)
    else:
        L.append(r)
else:
    L.append(res)

if error == []:
    pass
else:
    with open('./mallApiTest/error.txt',"a+",encoding="utf-8") as f:
        f.write('商品历史兑换信息接口，出现“系统错误，请联系管理员”返回结果如下：'+"\n" + str(error) + "\n" + "===============" + "\n")  # 按需更改汉字

with open('./mallApiTest/report.txt', 'a+', encoding="utf-8") as f:
    f.write('商品历史兑换信息接口，成功运行%s次，成功与失败返回如下：'%ok+"\n"+str(L)+"\n"+"==============="+"\n")  # 按需更改汉字
import requests
from bs4 import BeautifulSoup
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }
# content = requests.get("https://movie.douban.com/top250",headers=headers).text
# soup = BeautifulSoup(content,"heml.parser")

#UA伪装：请求载体的身份标识
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# url = "https://www.sogou.com/web"
# #处理url携带的参数：
# kw = input("输入想搜索的")
# param ={
#     "query":kw
# }
# responce = requests.get(url=url,params=param,headers=headers)
# responce.encoding="UTF-8"
# #对指定的url发起请求是对应url是携带参数的，并且在请求过程中处理了参数
# page = responce.text
# print(page)
# #将数据存入文件中
# filename = kw+".html"
# with open(filename,"w",encoding="utf-8")as fp:
#     fp.write(page)
# print("已爬")

import urllib.request,urllib.error


#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8")) #对获取到的网页进行utf-8的解码


#post方式，发送表单加密

#用http://httpbin.org/post 模拟post请求
# import urllib.parse
data = bytes(urllib.parse.urlencode({"age":"55","name":"sunyun"}),encoding="utf-8")  #转换2进制数据包
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))  #decode解码


# try:   #超时处理 timeout参数
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.8)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#对网页做简单的解析
# response = urllib.request.urlopen("http://httpbin.org/get")
# response = urllib.request.urlopen("http://douban.com")  #418发现被爬虫了
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)  #status 状态码
# print(response.getheader("Server"))

#用headers 伪装浏览器
headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
url = "http://httpbin.org/post"
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
#Pyhton2中的urllib2工具包，在Python3中分拆成了urllib.request和urllib.error两个包
#在python3中，如何使用urllib2.urlopen()：urllib.request.urlopen()
import urllib
from urllib import request,parse,error
#----------------------------最简版------------------------------
response = request.urlopen("http://www.baidu.com")

print(response.read())#read方法，可以返回获取到的网页内容

#----------------------------访问网页时需传递数据------------------------------
#如登录时
#----------------------------POST方式数据传送-----------------------------------------
values1 = {"username":"******","password":"********"}
data1 = parse.urlencode(values1).encode("UTF8")#POST data时，若没有.encode("UTF8")，会报错：TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
url1 = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
response1 = request.urlopen(url1,data1)

#----------------------------GET方式数据传送--------------------------------------------
#GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可
values2 = {}
values2['username'] = "1016903103@qq.com"
values2['password']="XXXX"
data2 = parse.urlencode(values2)
url2 = "http://passport.csdn.net/account/login"
geturl = url2 + '?' + data2
#HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
#如果捕获到了HTTPError，则输出code，不会再处理URLError异常。如果发生的不是HTTPError，则会去捕获URLError异常，输出错误原因
try:
    response2 = request.urlopen(geturl)
except error.HTTPError as e:
    print(e.code)
except error.URLError as e:
    print(e.reason)

print(response2.read())
# 百度凤巢API 拓词工具.
## 背景:
最近百度凤巢api又可以申请`token`了。

并且凤巢后台的接口加了~~好多恶心的玩意~~防爬的机制，导致了获取数据困难。

所以先用`python`封装了一个`API`,直接调用函数返回数据，

再用`tkinter`写一个`GUI`界面，可以给不会`python`程序的SEOer使用。

## 说明:
### 一.注册凤巢账号
注册地址:https://cas.baidu.com/?tpl=www2&fromu=http%3A%2F%2Fwww2.baidu.com%2Fcommon%2Fappinit.ajax

### 二.注册凤巢api并获取token
注册地址:https://dev2.baidu.com/content?sceneType=0&pageId=100369&nodeId=16&subhead=

### 三.工具使用
一共包含两个文件:
> py2fcapi.py
> 
> tkGUI.py

#### py2fcapi.py
封装了凤巢api的拓词功能,只给出了一个`getKeywords`函数作为主功能.
返回的结果是一个包含了`dict`的`list`,

其中`dict`里有
> `word`:关键词
> 
> `pcPv`:pc浏览量
>
> `mobPv`:移动浏览量
>
> `pv`:浏览量总和

同时在类中,还有一个`status`的变量，是请求`api`时的返回状态，便于DEBUG

代码示例:
```python
用法:
acc='123'
psw='***'
token='1h2h4h5j6j7jk8'
a= FCAPI(acc,psw,token)
result = a.getKeywords('keyword')
print(result)

>>> [{word:'keyword',pcPV:1,mobPV:2,pv:3}]

如果需要打印请求状态
a= FCAPI(acc,psw,token)
result = a.getKeywords('keyword')
print(a.status)


>>> keyword success
```
#### tkGUI.py
直接运行python文件即可

### 下载地址
[点我下载](https://github.com/iloveyby/BaiduFengchaoAPI/releases/tag/v0.5-beta)

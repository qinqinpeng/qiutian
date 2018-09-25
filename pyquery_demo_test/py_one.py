from pyquery import PyQuery as pq
from beautiful_soup.constant import HTML_TEXT

"""
pyquery需要传入一个html文本来初始化PyQuery对象
初始化可以是字符串 url 文件名等
"""

doc = pq(url='https://baidu.com')
print(doc('title'))

doc1 = pq(HTML_TEXT)
print(doc1("li"))

doc2 = pq(filename="demo.html")
print(doc2("title"))
"""
css选择器 # id  .class
"""
print(doc1(".city-container .city-selected div"))

"""
查找节点
find()传入的参数是css选择器  范围内的所有子孙节点  只查找子节点可以使用children()方法
parent()获取某个节点的父节点
"""

items = doc1(".header-inner")
print(items.find("li"))
print(items.children())
print(items.parent())
"""
获取属性 attr()  text()获取文本
"""

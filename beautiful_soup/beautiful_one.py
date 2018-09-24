from beautiful_soup.constant import HTML_TEXT

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(HTML_TEXT, 'lxml')
# 将html文件以标准的格式输出, 会自动补全缺失的HTML结构
print(soup.prettify())
# 获取title标签的内容
print(soup.div.string)
# 获取名称
print(soup.div.name)
# 获取属性 属性值多个，所以返回值为list列表
print(soup.div.attrs)
# 元素选择可以嵌套 ,这样的方式在多个的情况下，只取第一个，
# 比如body中有多个div,这里取了第一个
print(soup.body.div.a.attrs)

# contents 属性获取直接的子节点 children属性也是如此
# parents 属性获取某个元素的父节点

# next_sibling和pervious_sibling分别获取节点的上一个和下一个兄弟节点元素
print(list(soup.a.parents)[0].attrs['class'])

# find_all 查询所有符合条件的元素
# find_all(name, attrs, recursive, text, **kwargs)
# name是属性名  attrs是属性
print(soup.find_all(name="ul"))

for ul in soup.find_all(name="ul"):
    print(ul.find_all(name="li"))
# 属性传入夫人参数为字典格式
print(soup.find_all(attrs={"class": "js-geo-city"}))

# text
print(soup.find_all(text=re.compile("热")))

# find() 用法和find_all()一致，只不过返回的是单个元素，匹配到的第一个

# 其他方法
# find_parents() # 返回所有的祖先节点
# find_parent() # 直接返回父节点

# find_next_siblings() # 返回后面所有的兄弟节点
# find_next_sibling()  # 返回后面第一个兄弟节点

# find_previous_siblings() # 返回前面所有的兄弟节点
# find_pervious_sibling() # 返回前面第一个兄弟节点

# css选择器 select()
print(soup.select("ul li"))


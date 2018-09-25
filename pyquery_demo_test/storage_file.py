from pyquery import PyQuery as pq
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                  'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.106 Safari/537.36'
}
url_get = "https://www.zhihu.com/explore"
html_data = requests.get(url=url_get, headers=headers).text

doc = pq(html_data)
items = doc(".explore-tab .feed-item").items()
for item in items:
    question = item.find("h2").text()
    author = item.find(".author-link-line").text()
    answer = pq(item.find(".content").html()).text()
    with open('explore.txt', "a", encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write("\n" + "*" * 50 + "\n")

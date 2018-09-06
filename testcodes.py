import requests

url1 = 'https://www.jianshu.com/search?q=%E6%B1%BD%E8%BD%A6%E9%94%80%E5%94%AE&page=70&type=note'
url2 = 'https://www.jianshu.com/search/do?q=%E6%B1%BD%E8%BD%A6%E9%94%80%E5%94%AE&type=note&page=66&order_by=default'
url3 = 'https://www.jianshu.com/p/49bf7260e224'

h1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; rv:57.0) Gecko/20100101 Firefox/57.0'}
h2 = {
'X-CSRF-Token': 'CdGW2KGZ66/SFsDyStpitYlyLN4hR+7/6wjtJCi00KC2Wf8RM79AQsYKwg7U2C/OpK0yb9QpgoNWMMz5gwGdng==', 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; rv:57.0) Gecko/20100101 Firefox/57.0', 
}

a = requests.get(url1, headers = h1)

with open('a.html', 'w') as tt:
    tt.write(a.text)

b = requests.post(url2, headers = h2)

with open('b.json', 'w') as tt:
    tt.write(b.text)

c = requests.get(url3, headers = h1)

with open('c.html', 'w', encoding = 'utf-8') as tt:
    tt.write(c.text)



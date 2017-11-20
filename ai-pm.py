# coding:utf-8
import urllib.request, json
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://zhaopin.baidu.com/api/quanzhiasync?query=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86+%E6%8B%9B%E8%81%98&sort_type=1&city_sug=%E4%B8%8A%E6%B5%B7&detailmode=close&rn=20&pn=0'

m1 = []
m2 = []
content = {}

req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
#html = (res.read()).decode()

jd = json.loads(res.read())
for i in jd['data']['main']['data']['disp_data']:
	m1.append(i['age'])
	m2.append(i['district'])

content['m1'] = m1
content['m2'] = m2

jt = pd.DataFrame(content)
print(jt)

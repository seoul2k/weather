from bs4 import BeautifulSoup
import requests
import pinyin

city = pinyin.get(input("请输入城市名:"), format="strip")
header = {
    "user-agent": "Mozilla/5.0"
}
res = requests.get("https://www.tianqi.com/{}/".format(city), headers=header)
if res.status_code == 200:
    context = res.text
    soup = BeautifulSoup(context, 'lxml')
    dd = soup.find("dd", attrs={"class": "weather"})
    p = dd.p
    span = dd.span
    b = span.b.string
    print("天气："+b)
    print("温度："+span.b.next_sibling)
    print("当前温度："+p.b.string+'℃')

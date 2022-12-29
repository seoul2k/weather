from bs4 import BeautifulSoup
import requests
city = input('请输入城市名称（拼音）:')
headers = {
    "user-agent": "Mozilla/5.0"
}
try:
    rep = requests.get(f"https://www.tianqi.com/{city}/", headers=headers)
    context = rep.text
    soup = BeautifulSoup(context, "lxml")
    weather = soup.find("dd", attrs={"class": 'weather'}).span
    print("天气："+weather.b.string)
    print("温度："+weather.b.next_sibling.string)
except:
    print('城市名错误')

from bs4 import BeautifulSoup
import requests
import pinyin
import tkinter as t
from tkinter.ttk import Button
from tkinter.messagebox import showerror
b0 = '0'
b = ''
text = ''


def enter():
    global b0, b, text
    city = pinyin.get(v.get(), format="strip")
    header = {
        "user-agent": "Mozilla/5.0"
    }
    rep = requests.get(
        "https://www.tianqi.com/{}/".format(city), headers=header)
    if rep.status_code == 200:
        try:
            context = rep.text
            soup = BeautifulSoup(context, 'lxml')
            dd = soup.find("dd", attrs={"class": "weather"})
            b0 = dd.p.b.string
            span = dd.span
            b = span.b.string
            text = span.b.next_sibling
        except:
            showerror("错误！", '您输入的城市有误！')
    l1.configure(text="天气:"+b)
    l2.configure(text="当前温度:"+b0+"℃")
    l3.configure(text="温度:"+text)


window = t.Tk()
window.title("获取天气")
window.configure(bg="white")
window.geometry("500x200+200+200")

l = t.Label(window, text='城市名称:')
l.pack()
v = t.StringVar(window)
entry = t.Entry(window, border=2, textvariable=v)
entry.pack()
btn = Button(window, text="确定", command=enter)
btn.pack()
l1 = t.Label(window, text="天气:"+b)
l2 = t.Label(window, text="当前温度:"+b0+"℃")
l3 = t.Label(window, text="温度:"+text)
l1.pack()
l2.pack()
l3.pack()
window.mainloop()

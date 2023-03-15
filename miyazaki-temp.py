import requests
from bs4 import BeautifulSoup

def temp(url,n):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    high = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high")[0].text
    low = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low")[0].text
    temp = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img")[0].get("alt")
    return high,low,temp

class SetUrl:

    def __init__(self,url,day):
        self.url = url
        self.day = day
        self.high,self.low,self.temp = temp(self.url,self.day)

    def print_result(self):
        print("宮崎市の" + self.day + "の天気は" + self.temp + "最高気温は" + self.high + "度、最低気温は、" + self.low + "度です。")

today = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=1","今日")
today.print_result()

another_day = input("明日以降の天気を知りたい場合は知りたい日にちを今日から数えた日数で入力してください（例）明日なら1\n")

if another_day == "1":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=2","明日")
    another_temp.print_result()

elif another_day == "2":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=3","明後日")
    another_temp.print_result()

elif another_day == "3":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=4","3日後")
    another_temp.print_result()

elif another_day == "4":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=5","4日後")
    another_temp.print_result()

elif another_day == "5":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=6","5日後")
    another_temp.print_result()

elif another_day == "6":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=7","6日後")
    another_temp.print_result()

elif another_day == "7":
    another_temp = SetUrl("https://weather.yahoo.co.jp/weather/jp/45/?day=8","7日後")
    another_temp.print_result()

else:
    print("1週間分しか見ることができません")
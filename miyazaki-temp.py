import requests
from bs4 import BeautifulSoup

url = "https://weather.yahoo.co.jp/weather/jp/45/?day=1"
res = requests.get (url)

soup = BeautifulSoup(res.text, "html.parser")

miyazaki_high = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high")[0].text
miyazaki_low = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low")[0].text
miyazaki_temp = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img")[0].get("alt")
print("宮崎市の天気は" + miyazaki_temp + "最高気温は" + miyazaki_high + "度、最低気温は、" + miyazaki_low + "度です。")

another_day = input("明日以降の天気を知りたい場合は知りたい日にちを今日から数えた日数で入力してください（例）明日なら1\n")
if another_day == "1":
    url = "https://weather.yahoo.co.jp/weather/jp/45/?day=2"
    an_res = requests.get(url)
    an_soup = BeautifulSoup(an_res.text,"html.parser")
    an_miyazaki_high = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high")[0].text
    an_miyazaki_low = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low")[0].text
    an_miyazaki_temp = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img")[0].get("alt")
    print("宮崎市の" + another_day + "日後の天気は" + an_miyazaki_temp + "最高気温は" + an_miyazaki_high + "度、最低気温は、" + an_miyazaki_low + "度です。")

elif another_day == "2":
    url = "https://weather.yahoo.co.jp/weather/jp/45/?day=3"
    an_res = requests.get(url)
    an_soup = BeautifulSoup(an_res.text,"html.parser")
    an_miyazaki_high = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high")[0].text
    an_miyazaki_low = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low")[0].text
    an_miyazaki_temp = an_soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img")[0].get("alt")
    print("宮崎市の" + another_day + "日後の天気は" + an_miyazaki_temp + "最高気温は" + an_miyazaki_high + "度、最低気温は、" + an_miyazaki_low + "度です。")
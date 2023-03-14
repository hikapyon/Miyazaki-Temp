import requests
from bs4 import BeautifulSoup

url = "https://weather.yahoo.co.jp/weather/jp/45/?day=1"
res = requests.get (url)

soup = BeautifulSoup(res.text, "html.parser")

miyazaki_high = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.high")[0].text
miyazaki_low = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.temp > em.low")[0].text
miyazaki_temp = soup.select("#map > ul > li.point.pt8710 > a > dl > dd > p.icon > img")[0].get("alt")
print("宮崎市の天気は" + miyazaki_temp + "最高気温は" + miyazaki_high + "度、最低気温は、" + miyazaki_low + "度です。")
from bs4 import BeautifulSoup
import requests


url = "https://www.accuweather.com/en/us/salt-lake-city/84101/weather-forecast/331216"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}
response = requests.get(url, headers=headers)

bs = BeautifulSoup(response.text, "lxml")
temp = bs.find("div", class_="temp").text
location = bs.find("h1", class_="header-loc").text
result = "{} in {}".format(temp, location)

print(result)

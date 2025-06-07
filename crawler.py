import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/kfootball/schedule/index"  # 예시 URL

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
matches = soup.select(".sch_table tr")

for match in matches:
    date = match.select_one(".date")
    teams = match.select(".team")
    time = match.select_one(".time")
    if date and teams and time:
        home = teams[0].text.strip()
        away = teams[1].text.strip()
        print(f"{date.text.strip()} | {home} vs {away} | {time.text.strip()}")

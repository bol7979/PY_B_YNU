import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.yu.ac.kr/main/intro/yu-news.do?mode=list&&articleLimit=100&article.offset=0")
soup = BeautifulSoup(response.text, "html.parser")
lis = soup.find("div", class_ = "b-top-info-wrap").find_all("tr")

print(lis)
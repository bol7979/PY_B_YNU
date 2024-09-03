import requests
from bs4 import BeautifulSoup

def search_yunews():
    events = []

    response = requests.get("https://www.yu.ac.kr/main/intro/yu-news.do?mode=list&&articleLimit=100&article.offset=0", 
                            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"})
    soup = BeautifulSoup(response.text, "html.parser")
    lis = soup.find_all("tr")

    for li in lis:
        try:
            title = li.find("div", class_ = "b-title-box").find("span").text
            date = li.find_all("td")[3].text.strip()
            link = li.find("div", class_ = "b-title-box").find("a").get("href")
            
            event_data = {
                "title": title,
                "date": date,
                "link": f"https://www.yu.ac.kr/main/intro/yu-news.do{link}"
            }

            events.append(event_data)

        except:
            pass

        print("영대소식 스크랩 완료")
    return events

events = []
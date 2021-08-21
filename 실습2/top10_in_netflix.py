# 실습2. beautifulsoup을 이용해 오늘의 국내 넷플릭스 인기 top 10 프로그램 리스트를 추출해 csv 파일에 저장하기
import requests
import csv
from bs4 import BeautifulSoup

### flixpatrol 사이트 접근
url = "https://flixpatrol.com/top10/netflix/south-korea/2021-08-16/"
res = requests.get(url) # res = respond, 응답 객체를 의미함
res.raise_for_status() # 웹 사이트 접근 중 에러 발생 시 에러 코드 출력
print("웹 스크래핑을 시작합니다.")

# 영화 리스트를 담을 csv 파일 생성
filename = "오늘의_넷플릭스_top10_영화목록.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 열(column) 생성 -> writerow
column = "N 순위변동 영화제목".split(" ")
writer.writerow(column)


### 웹 스크래핑 
# 뷰티풀숲 객체 생성
# lxml parser(문자열 분석)를 이용해 res.text 문자열을 파싱
soup = BeautifulSoup(res.text, "lxml")

movie_list = soup.find("table", attrs={"class":"card-table"}).find("tbody").find_all("tr")
print(movie_list)

for movie in movie_list:
    rows = movie.find_all("td")
    # if len(columns) <= 1:
    #     continue
    data = [row.get_text().strip() for row in rows]
    print(data)
    writer.writerow(data)

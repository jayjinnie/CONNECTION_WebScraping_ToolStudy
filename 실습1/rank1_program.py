# 실습1. beautifulsoup을 이용해 오늘의 1위 인기 프로그램 정보 추출하며 html 구조 이해하기

import requests
from bs4 import BeautifulSoup

### flixpatrol 사이트 접근
url = "https://flixpatrol.com/title/hospital-playlist/"
res = requests.get(url) # res = respond, 응답 객체를 의미함
print("응답코드 :", res.status_code) # 200이상이면 정상

res.raise_for_status() # 웹 사이트 접근 중 에러 발생 시 에러 코드 출력
print("웹 스크래핑을 시작합니다.")

### 뷰티풀숲 객체 생성
# lxml parser(문자열 분석)를 이용해 res.text 문자열을 파싱
soup = BeautifulSoup(res.text, "lxml")

# 사이트 내 타이틀 정보 추출
print("title:", soup.title.get_text())

# soup 객체에서 처음 발견되는 h1 element 출력: 프로그램 제목
print("h1 tag's text:", soup.h1.get_text())

# tag, class와 text 값을 이용해 프로그램 정보 추출하기
# 줄거리 추출
summary = soup.find("div", attrs={"class": "card-body"}) # atrrs = atrributes, 속성값
print("1위 프로그램 줄거리:", summary.get_text().strip())

# 출연, 연출가 추출
people = summary.find_next_sibling(attrs={"class": "card-body"})
print("1위 프로그램 출연 및 연출가 정보: ", people.get_text().strip())

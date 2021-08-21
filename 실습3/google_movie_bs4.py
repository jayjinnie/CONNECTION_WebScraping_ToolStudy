# 실습3. 구글 무비 동적 페이지 분석 - 할인 중인 영화 추출
import requests
from bs4 import BeautifulSoup

### User Agent
# 구글 무비 우리가 접속하는 한국 페이지와 영어 페이지의 차이점 안내
# user agent 확인 방법 소개
url = "https://play.google.com/store/movies/top"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
"Accept-Language":"ko-KR,ko"}


### Beautiful Soup 
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 태그 확인 
movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# 동적 페이지 확인
# requests의 한계 -> selenium!!
 
# 일단 상위 노출된 영화 10개 제목 추출
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

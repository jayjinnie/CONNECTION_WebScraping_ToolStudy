# 실습3. selenium을 이용해 동적 페이지 구글 무비 사이트에서 인기 영화 리스트 추출하기
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# 동적 페이지
# requests의 한계 -> selenium!!

headless Chrome
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# 크롬 드라이버 열기
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 현재 html 문서 높이를 가져와서 저장, 갱신을 위해서 prev_height로 지정
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 2초간 대기
    time.sleep(2) # 2초에 한번씩 스크롤 내리기

    # 도달한 문서 높이를 현재 문서 높이에 저장하여 높이 상태 갱신
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: # 두 높이가 같다면 스크롤이 완료된 것, 더이상 스크롤을 내릴 수 없으므로 갱신 종료
        break
    prev_height = curr_height
print("스크롤 완료")

# 스크린샷
browser.get_screenshot_as_file("google_movie.png")

# -------------------

soup = BeautifulSoup(browser.page_source, "lxml")

# 영화 패널 찾기
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies)) # 추출 영화 개수 출력

# 페이지 내 모든 인기 차트 영화 타이틀 추출
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

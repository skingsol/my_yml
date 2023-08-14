# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from .models import Chart


# def set_chrome_driver():
#     chrome_options = webdriver.ChromeOptions()
#     # 창을 최대화시킨 후 띄워주기
#     chrome_options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()), options=chrome_options
#     )
#     return driver


# def add_top100_list():
#     driver = set_chrome_driver()

#     url = "https://vibe.naver.com/chart/total"
#     driver.get(url)
#     # print(driver.page_source)
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     # print(soup)

#     # 각 노래 정보 가져오기
#     songs = soup.select(".tracklist tbody > tr")

#     for song in songs:
#         # if counter >= 100:
#         #     break
#         rank = song.select_one("td.rank > span").text
#         title = song.select_one("td.song a").text.strip()
#         artist = song.select_one("td.artist a.link_artist > span").text.strip()
#         img_url = song.select_one("td.thumb img")["src"]

#         # print(rank,title,artist,img_url)

#         # 데이터 저장
#         chart_item = Chart(rank=rank, title=title, artist=artist, album_image=img_url)
#         chart_item.save()

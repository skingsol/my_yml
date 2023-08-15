import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .models import Chart, BillboardChart, JpopChart


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    # 창을 최대화시킨 후 띄워주기
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


# 오늘 top100 가져오기
def get_chart():
    driver = set_chrome_driver()

    url = "https://vibe.naver.com/chart/total"
    driver.get(url)
    # print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 각 노래 정보 가져오기
    songs = soup.select(".tracklist tbody > tr")

    for song in songs:
        rank = song.select_one("td.rank > span").text
        title = song.select_one("td.song a").text.strip()
        artist = song.select_one("td.artist a.link_artist > span").text.strip()
        img_url = song.select_one("td.thumb img")["src"]

        # 데이터 저장
        chart_item = Chart(rank=rank, title=title, artist=artist, album_image=img_url)
        chart_item.save()


# billboard chart 가져오기
def get_billboard_chart():
    driver = set_chrome_driver()

    url = "https://vibe.naver.com/chart/billboardTrack"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 각 노래 정보 가져오기
    songs2 = soup.select(".tracklist tbody > tr")

    for song2 in songs2:
        try:
            rank = song2.select_one("td.rank > span").text
            title = song2.select_one("td.song a").text.strip()
            artist = song2.select_one(
                "div.artist_sub a.link_artist > span"
            ).text.strip()
            img_url = song2.select_one("td.thumb img")["src"]

            chart_item = BillboardChart(
                rank=rank, title=title, artist=artist, album_image=img_url
            )
            chart_item.save()
        except Exception as e:
            print(f"Error in processing song or saving to database: {e}")


# JAPAN HOT 100 가져오기
def get_jpop_chart():
    driver = set_chrome_driver()

    url = "https://vibe.naver.com/chart/lm-songs"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 각 노래 정보 가져오기
    songs3 = soup.select(".tracklist tbody > tr")

    for song3 in songs3:
        try:
            rank = song3.select_one("td.rank > span").text
            title = song3.select_one("td.song a").text.strip()
            artist = song3.select_one(
                "div.artist_sub a.link_artist > span"
            ).text.strip()
            img_url = song3.select_one("td.thumb img")["src"]

            chart_item = JpopChart(
                rank=rank, title=title, artist=artist, album_image=img_url
            )
            chart_item.save()
        except Exception as e:
            print(f"Error in processing song or saving to database: {e}")

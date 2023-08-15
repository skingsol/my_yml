# webdriver
# 방법1) 브라우저에 맞는 드라이버 다운로드 후 폴더에 옮겨놓고 사용하기
# 방법2) 추천방법 - 드라이버 다운로드 하지 않고 사용하는 방법
#          pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    # 창을 최대화시킨 후 띄워주기
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


if __name__ == "__main__":
    driver = set_chrome_driver()
    driver.get("https://vibe.naver.com/chart")

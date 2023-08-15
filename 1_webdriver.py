from chrome import set_chrome_driver
import time

# 모듈 웹드라이버 사용
driver = set_chrome_driver()
driver.get("https://vibe.naver.com/chart")
time.sleep(2)
driver.quit()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


def init_driver():
    driver = uc.Chrome()
    driver.get("https://velog.io")
    return driver


def do_login(driver):
    # 로그인 버튼클릭후 구글 로그인 클릭
    driver.find_element(By.XPATH, '//button[text()="로그인"]').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "sc-hKwDye.ihJtSI").click()
    time.sleep(2)
    # 로그인을 수동으로 입력할 시간 60초 주기 로그인 완료되면 다음작업 시작
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="새 글 작성"]'))
    )
    # music.youtube.com으로 이동
    driver.get("https://music.youtube.com/")
    time.sleep(2)
    # 재생목록 추가 버튼 클릭
    driver.find_element(By.CLASS_NAME, "yt-spec-touch-feedback-shape__fill").click()

    time.sleep(2)
    # 재생목록 제목 입력
    driver.switch_to.active_element.send_keys("top100")
    time.sleep(2)
    # 재생목록 만들기 버튼 클릭
    driver.find_element(
        By.XPATH,
        '//*[@id="general-pane"]/div[2]/yt-button-renderer[2]/yt-button-shape/button',
    ).click()
    time.sleep(2)
    # 여기까지 재생목록 생성 완료

    # 노래 제목과 가수로 함께 검색해서 차트에 노래 넣기
    # 검색창 위치 찾기
    driver.find_element(
        By.XPATH,
        '//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/tp-yt-paper-icon-button[1]',
    ).click()
    # 검색 입력
    driver.switch_to.active_element.send_keys("super shy newjeans")
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    # 엔터키 입력
    time.sleep(2)

    # 검색결과 노래 상세페이지 이동
    driver.find_element(
        By.XPATH,
        '//*[@id="contents"]/ytmusic-card-shelf-renderer/div/div[2]/div[2]/yt-button-shape/button/yt-touch-feedback-shape/div',
    ).click()
    time.sleep(2)
    # 곡상세 메뉴 열기 버튼 클릭
    driver.find_element(
        By.XPATH, '//*[@id="button-shape"]/button/yt-touch-feedback-shape/div'
    ).click()
    time.sleep(1)
    # 재생목록에 추가하기 버튼 클릭
    driver.find_element(
        By.XPATH, '//*[@id="items"]/ytmusic-menu-navigation-item-renderer[3]'
    ).click()
    time.sleep(2)
    # 최근 재생목록중 가장 최근 재생목록 선택하여 클릭
    # driver.find_element(By.XPATH, '//*[@id="img"]')
    # driver.find_element(By.CSS_SELECTOR,'#items > ytmusic-two-row-item-renderer:nth-child(1) > a').click()
    driver.find_element(
        By.XPATH, '//*[@id="items"]/ytmusic-two-row-item-renderer[1]/a'
    ).click()
    # 중복항목이 있다면 제외하고 추가하기
    # driver.find_element(By.XPATH, '//*[@id="cancel-button"]/yt-button-shape/button/yt-touch-feedback-shape/div').click()
    time.sleep(2)
    # 노래 추가가 끝난후에는 music.youtube.com으로 다시 이동
    driver.get("https://music.youtube.com/")


# main에서 실행하지 않으면 오류가 남
if __name__ == "__main__":
    driver = init_driver()
    do_login(driver)

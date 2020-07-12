import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def clipboard_input(user_xpath, user_input):
	temp_user_input = pyperclip.paste()

	pyperclip.copy(user_input)
	driver.find_element_by_xpath(user_xpath).click()
	ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

	pyperclip.copy(temp_user_input)
	time.sleep(1)

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", chrome_options=options)
driver.implicitly_wait(3)

driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
driver.implicitly_wait(3)

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/button[1]").click()
time.sleep(2)

clipboard_input("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", "ID")
driver.find_element_by_id("identifierNext").click()
time.sleep(2)

clipboard_input("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input", "PW")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div").click()
time.sleep(2)

driver.get("https://www.youtube.com")
driver.implicitly_wait(3)

online_ment = "온라인예배 출석 조사를 위한 구글 서베이 링크입니다.\n온라인예배에 참석해주시는 성도님들은 1청, 2청 각각 서베이에 출석 여부를 적어주시면 감사하겠습니다!"
online_ment2 = "온라인예배 출석 조사는 영상 설명란의 주소를 통해 1청, 2청 각각 자신의 청년팀 링크로 부탁드립니다. 감사합니다."

driver.get("BraodCastURL") # Broadcast URL

while(1):
	clipboard_input(driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/iron-pages/div[1]/yt-live-chat-message-input-renderer/div[1]/div[1]/div/yt-live-chat-text-input-field-renderer/label"), online_ment)
	driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/iron-pages/div[1]/yt-live-chat-message-input-renderer/div[1]/div[3]/div[2]/div[2]/yt-button-renderer/a/yt-icon-button/button").click()

	clipboard_input(driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/iron-pages/div[1]/yt-live-chat-message-input-renderer/div[1]/div[1]/div/yt-live-chat-text-input-field-renderer/label"), online_ment2)
	driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/iron-pages/div[1]/yt-live-chat-message-input-renderer/div[1]/div[3]/div[2]/div[2]/yt-button-renderer/a/yt-icon-button/button").click()

	time.sleep(1020)

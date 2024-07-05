import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def valhallaChck(PTT_ID):
	headers = {
		'User-Aggent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
	url = 'https://taiwandreamer.notion.site/PTT-e2ca57714cc34d0dba89ce9d36290ec3'

	driver = webdriver.Chrome()
	driver.get(url)
	time.sleep(3)
	driver.find_element(By.CLASS_NAME, "notion-selectable.notion-file-block").click()
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[1])
	valhallaUrl = driver.current_url
	driver.quit()

	res = requests.get(valhallaUrl, headers=headers)
	valhallaList = res.text.split()

	if res.status_code != 200:
		print(f"抓不到名單！")
	elif PTT_ID in valhallaList:
		print(f"目前共有 {len(valhallaList)} 名勇士在英靈殿，很可惜，{PTT_ID} 也是其中之一，無法升官發財！")
	else:
		print(f"恭喜你！{PTT_ID} 明天請到黨部報到！")


if __name__ == '__main__':
	valhallaChck(input("請輸入你的 PTT ID：").strip().lower())

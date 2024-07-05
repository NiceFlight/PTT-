import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

headers = {'User-Aggent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
url = 'https://taiwandreamer.notion.site/PTT-e2ca57714cc34d0dba89ce9d36290ec3'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element(By.CLASS_NAME, "notion-selectable.notion-file-block").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
valhalla = driver.current_url
driver.quit()

res = requests.get(valhalla, headers=headers).text
valhalla = res.split()

PTT_ID = input("請輸入你的 PTT ID：").strip().lower()

if PTT_ID in valhalla:
	print(f"目前共有 {len(valhalla)} 名勇士在英靈殿，很可惜，{PTT_ID} 在英靈殿榜上，無法升官發財！")
else:
	print(f"恭喜你！{PTT_ID} 明天請到黨部報到上班！")
	

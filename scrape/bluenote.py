from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


print("aaaa")
# ドライバ設定とURL取得
driver = webdriver.Chrome()
driver.get("sampleSelenium.html")
time.sleep(0.5) # 読み込み時間を考慮

# ブラウザの操作
bottum = driver.find_element_by_id("bottun3") # 要素の取得
bottum.click()# ボタンの押下
time.sleep(0.5) # 読み込み時間を考慮

# 要素の取得
fig = driver.find_element_by_xpath("//div[@id='figure']/div[1]") # 要素の取得
name = fig.get_attribute("name") # 属性の取得
print(name)

# WebDriverの終了
driver.close()
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url='https://www.e-typing.ne.jp/roma/check/'
driver = webdriver.Chrome(executable_path='/Users/itsuka/workspace/chromedriver')
driver.get(url)

# 今すぐチェック！をクリック
driver.find_element_by_class_name('edro').click()

time.sleep(1)

# モーダルにスイッチ
driver.switch_to.frame('typing_content')

# スタートをクリック
driver.find_element_by_xpath('//div[@id="start_btn"]').click()

time.sleep(1)

# スペースキーでスタート
driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

time.sleep(4)

while True:
    try:
        sentences = driver.find_element_by_xpath('//div[@id="sentenceText"]').find_elements_by_tag_name('span')[1].text
        for sentence in sentences:
            driver.find_element_by_tag_name("body").send_keys(sentence)
        time.sleep(1)
    except:
        break
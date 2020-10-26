from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import loginInfo

browser = webdriver.Chrome()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')

giris_yap.click()

time.sleep(3)

username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')

password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

username.send_keys(loginInfo.username)

password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')

login.click()

time.sleep(3)

#searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")

searchArea.send_keys("#yazilimayolver")

searchArea.send_keys(Keys.ENTER)

#elements = browser.find_elements_by_css_selector("css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")
#elements = browser.find_elements_by_css_selector("span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")

#print(elements)
for element in elements:
    print("**********************************")
    print(element.text)

time.sleep(3)

browser.back()

time.sleep(3)

browser.close()

"""body = browser.find_element_by_tag_name('body')
for _ in range(100):
   body.send_keys(Keys.PAGE_DOWN)
   time.sleep(0.2)"""
